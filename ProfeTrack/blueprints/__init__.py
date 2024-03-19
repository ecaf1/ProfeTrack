from flask import Flask

from .login import init_app as init_bp_login
from .user import init_app as init_bp_user


def init_app(app: Flask):
    init_bp_login(app)
    init_bp_user(app)
    return app
