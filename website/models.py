from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    carts = db.relationship("Cart", backref="user", lazy=True)


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    items = db.relationship("Item", backref="cart", lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    url = db.Column(db.String(100))
    price = db.Column(db.Float)
    cart_id = db.Column(db.Integer, db.ForeignKey("cart.id"))
