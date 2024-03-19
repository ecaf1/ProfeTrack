from dynaconf import FlaskDynaconf
from flask import Flask

def init_app(app: Flask):
    FlaskDynaconf(app,  settings_file=["settings.toml", ".secrets.toml"])