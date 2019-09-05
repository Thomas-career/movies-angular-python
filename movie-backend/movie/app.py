import logging.config
import os
import sys
from logging.handlers import TimedRotatingFileHandler

from flask import Flask

from movie import api
from movie.extensions import db, migrate
from movie.middleware.restplus import api
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

def create_app(
        config=None,
        environment=os.environ.get(
            'FLASK_ENV',
            'development'),
        cli=True):
    """Application factory, used to create application
    """

    app = Flask('movie')
    CORS(app)
    # Setup the Flask-JWT-Extended extension
    app.config['JWT_SECRET_KEY'] = 'moviee-secret'  # Change this!
    jwt = JWTManager(app)
    configure_app(app, environment)
    configure_extensions(app, cli)
    register_blueprints(app)

    return app



def configure_app(app, environment):
    """set configuration for application
    """
    if environment == 'testing':
        app.config.from_object('movie.config.test')
    elif environment == 'production':
        app.config.from_object('movie.config.prod')
    else:
        app.config.from_object('movie.config.dev')


def configure_extensions(app, cli):
    """configure flask extensions
    """
    db.init_app(app)

    if cli is True:
        migrate.init_app(app, db)


def register_blueprints(app=None):
    """register all blueprints for application
    """
    app.register_blueprint(api.blueprint)