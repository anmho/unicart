from flask import Flask
from .views import views
from .auth import auth
from .models import db, User
from flask_login import LoginManager
from os import path


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    db.init_app(app)
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    return app


def create_database(app):
    if not path.exists("database.db"):
        db.create_all(app=app)
        print("Database created")
        print(db)
