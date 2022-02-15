from importlib.metadata import requires
import json
from flask import Blueprint, flash, render_template, request, jsonify, redirect, url_for, abort
from sqlalchemy import desc
from .models import Cart, db, Item
from flask_login import current_user, login_required
views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def home():
    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
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


@views.route("/create-cart")
@login_required
def create_cart(name, description):
    new_cart = Cart(name=name, description=description,
                    user_id=current_user.id)
    db.session.add(new_cart)
    db.session.commit()
    flash("Successfully added cart", "success")

    return redirect(url_for("views.home"))


@views.route("/edit-cart/<int:id>", methods=["POST", "GET"])
@login_required
def edit_cart(id):
    cart = Cart.query.get_or_404(id)

    if request.method == "POST":
        name = request.form.get("name")
        url = request.form.get("url")
        price = request.form.get("price")

        if name:
            new_item = Item(name=name, url=url, cart_id=cart.id, price=price)
            db.session.add(new_item)
            db.session.commit()
            flash("Successfully added item", "success")
        else:
            if not name:
                flash("Please enter a name for your item")

    return render_template("edit_cart.html", id=id, cart=cart, title="Edit")


@views.route("/delete-cart", methods=["POST"])
def delete_cart():
    body = json.loads(request.data)
    cartId = body["cartId"]
    cart = Cart.query.get(cartId)

    if cart and cart.user_id == current_user.id:
        db.session.delete(cart)
        db.session.commit()

    return jsonify({})


@views.route("/edit-item/<int:id>", methods=["POST"])
@login_required
def edit_item(id):
    item = Item.query.get(id)
    cart = Cart.query.get(item.cart_id)

    if cart.user_id == current_user.id:
        try:
            item.name = request.form.get("name")
            item.url = request.form.get("url")
            item.price = request.form.get(
                "price") if request.form.get("price") else 0
            db.session.commit()
        except:
            flash("That didn't work")
    else:
        abort(403)

    return redirect(url_for("views.edit_cart", id=item.cart_id))


@views.route("/delete-item", methods=["POST"])
def delete_item():
    body = json.loads(request.data)
    cartId = body["cartId"]
    itemId = body["itemId"]
    cart = Cart.query.get(cartId)
    item = Item.query.filter_by(id=itemId, cart_id=cartId).first()

    if item and cart.user_id == current_user.id:
        db.session.delete(item)
        db.session.commit()

    return jsonify({})
