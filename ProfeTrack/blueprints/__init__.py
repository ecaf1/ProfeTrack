from flask import Flask

from .login import init_app as init_bp_login
def init_bps(app: Flask):
    init_bp_login(app)
    return app