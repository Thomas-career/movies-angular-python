from flask import jsonify, request
from flask_restplus import Resource
from marshmallow import fields

from movie.data_access.db_models import user
from movie.data_access.schema_definitions.user_schema import UserSchema
from movie.extensions import db, ma
from movie.middleware.restplus import api
from movie.serializers.user_serializer import user
from movie.serializers.login_serializer import login
from movie.utils.response_code import response_format
from movie.services.user.service import (create_user, login_user)

# from movie.utils.response_constants import RESPONSE_ERROR_MESSAGE
ns = api.namespace(
    'auth',
    description='Operations related to auth')

@ns.route('/register')
class userRegister(Resource):
    """User Registration
    """

    @api.expect(user)
    def post(self):
        response = create_user(request.json)
        return response_format(response)

@ns.route('/login')
class userLogin(Resource):
    """User Login
    """

    @api.expect(login)
    def post(self):
        response = login_user(request.json)
        return response_format(response)
