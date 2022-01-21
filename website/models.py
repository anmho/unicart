from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
