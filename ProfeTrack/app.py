from flask import Flask
from dynaconf import FlaskDynaconf

from ProfeTrack.blueprints import init_bps as init_blueprints
from ProfeTrack.service.auth import init_app as init_auth
from ProfeTrack.service.session import init_app as init_session
from ProfeTrack.service.database import init_app as init_database
from ProfeTrack.service.settings import init_app as init_settings

def create_app():
    app = Flask(__name__)

    init_settings(app)
    init_database(app)
    init_blueprints(app)
    init_auth(app)
    init_session(app)
    


    return app
