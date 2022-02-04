import json
from flask import Blueprint, flash, render_template, request, jsonify, redirect, url_for
from sqlalchemy import desc
from .models import Cart, db
from flask_login import current_user
views = Blueprint("views", __name__)


def create_cart(name, description):
    new_cart = Cart(name=name, description=description,
                    user_id=current_user.id)
    db.session.add(new_cart)
    db.session.commit()
    flash("Successfully added cart", "success")


@views.route("/edit-cart", methods=["POST"])
def edit_cart(id):
    flash(id)
    flash("Edit")
    flash(request.form)
    name = request.form.get("name")
    url = request.form.get("url")
    flash(name)
    flash(url)

    return redirect(url_for("views.home"))


@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # if "edit" in request.form:
        #     flash("Edit")
        #     flash(request.form)
        #     name = request.form.get("name")
        #     url = request.form.get("url")
        #     flash(name)
        #     flash(url)
        if "create" in request.form:
            name = request.form.get("name")
            description = request.form.get("description")
            if name and description:
                create_cart(name, description)
            else:
                if not name:
                    flash("Enter a name", "error")
                if not description:
                    flash("Enter a description", "error")

    return render_template("index.html", user=current_user)


@views.route("/delete-cart", methods=["POST"])
def delete_cart():
    body = json.loads(request.data)
    cartId = body["cartId"]
    cart = Cart.query.get(cartId)

    if cart and cart.user_id == current_user.id:
        db.session.delete(cart)
        db.session.commit()

    return jsonify({})
