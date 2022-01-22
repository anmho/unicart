from socket import create_server
from flask import Blueprint, render_template
from .models import User, Cart, db
views = Blueprint("views", __name__)

users = [
    {
        "name": "Joe",
        "carts": [
            {"items": "asdfaf"},
            {"items": "b"},
        ]
    },
    {
        "name": "Mom",
        "carts": [
            {"items": "c"},
        ]
    },
    {
        "name": "jojo",
        "carts": [
            {"items": "c"},
            {"items": "d"},
        ]
    },
]


@views.route("/")
def home():
    for user in users:
        new_user = User(name=user["name"])
        db.session.add(new_user)
        for cart in user["carts"]:
            
            new_cart = Cart(cart["items"])
            db.session.add(cart)

    db.session.commit()

    return render_template("index.html")
