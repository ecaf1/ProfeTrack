from flask import Flask
from flask_login import LoginManager

from ProfeTrack.models.user import User


def init_app(app: Flask):
    login_manager = LoginManager()
    login_manager.login_view = "auth.login" #type: ignore
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

