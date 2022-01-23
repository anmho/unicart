from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    carts = db.relationship("Cart", backref="user", lazy=True)


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.String(100)) # change to backref item
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # add foreignkey cart
