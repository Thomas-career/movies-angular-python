from flask import jsonify, request
from flask_restplus import Resource
from marshmallow import fields
from flask_jwt_extended import ( jwt_required, get_jwt_identity)

from movie.data_access.db_models import movie
from movie.data_access.schema_definitions.movie_schema import MovieSchema
from movie.extensions import db, ma
from movie.middleware.restplus import api
from movie.serializers.movie_serializer import movie
from movie.utils.response_code import response_format
from movie.services.movie.service import (delete_movie,
                                                      get_all_movie,
                                                      get_movie, post_movie,
                                                      update_movie, get_all_movie_pagination)


# from movie.utils.response_constants import RESPONSE_ERROR_MESSAGE
ns = api.namespace(
    'movie',
    description='Operations related to movie')

@ns.route('/<int:movie_id>')
class movieResource(Resource):
    """Single object resource
    """

    def get(self, movie_id):
        response = get_movie(movie_id)
        return response_format(response)

    @jwt_required
    @api.expect(movie)
    def put(self, movie_id):
        response = update_movie(movie_id, request.json)
        return response_format(response)

    @jwt_required
    def delete(self, movie_id):
        response = delete_movie(movie_id)
        if response:
            return response_format(response)

@ns.route('/')
class movieList(Resource):
    """Creation and get_all
    """
    @jwt_required
    def get(self):
        response = get_all_movie()
        return response, 200

    @jwt_required
    @api.expect(movie)
    def post(self):
        response = post_movie(request.json)
        return response, 201

@ns.route('/page/<int:page>')
class movieListPage(Resource):
    """get with pagination
    """

    def get(self, page):
        response = get_all_movie_pagination(page)
        return response, 200