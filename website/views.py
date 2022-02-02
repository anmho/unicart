from flask import Blueprint, flash, render_template, request, jsonify
from sqlalchemy import desc
from .models import User, Cart, db
from flask_login import current_user
views = Blueprint("views", __name__)
import json

@views.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")

        if name and description:
            new_cart = Cart(name=name, description=description,
                            user_id=current_user.id)
            db.session.add(new_cart)
            db.session.commit()
            flash("Successfully added cart", "success")
        else:
            if not name:
                flash("Enter a name", "error")
            if not description:
                flash("Enter a description", "error")

    return render_template("index.html", user=current_user)


@views.route("/create-cart", methods=["GET", "POST"])
def create_cart():
    pass

@views.route("/delete-cart", methods=["POST"])
def delete_cart():
    body = json.loads(request.data)
    cartId = body["cartId"]
    cart = Cart.query.get(cartId)

    if cart and cart.user_id == current_user.id:
        db.session.delete(cart)
        db.session.commit()
    
    return jsonify({})