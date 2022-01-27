from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_user, logout_user
import flask_login
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, db

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST", "GET"])
def login():

    return render_template("login.html")


@auth.route("/sign-up", methods=["POST", "GET"])
def sign_up():
    # post request
    if request.method == "POST":
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        # Validate fields
        found_user = User.query.filter_by(email=email).first()
        if not email:
            flash("Please enter an email", "error")
        elif not password1:
            flash("Please enter a password", "error")
        elif not password2:
            flash("Please confirm your password", "error")
        elif found_user:
            flash("Email already in use", "error")
        elif len(email) > 100:
            flash("Email must be less than 100 characters")
        elif password1 != password2:
            flash("Passwords do not match", "error")
        else:
            new_user = User(email=email, password=generate_password_hash(
                password=password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created", "success")
            redirect(url_for("views.home"))

    return render_template("sign_up.html")


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))
