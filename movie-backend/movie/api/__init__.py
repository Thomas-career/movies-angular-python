from flask import Blueprint
from flask_restplus import Api, Resource

from movie.api.v1.movie.api import ns as movie_api
from movie.api.auth.user.auth import ns as auth_api
from movie.middleware.restplus import api

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api.init_app(blueprint)

api.add_namespace(movie_api)
api.add_namespace(auth_api)
