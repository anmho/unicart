from socket import create_server
from flask import Blueprint, flash, render_template
from .models import User, Cart, db
views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@views.route("/create-cart", methods=["GET", "POST"])
def create_cart():
    pass
