import collections
from datetime import datetime

from flask import jsonify, request
from flask_restplus import Resource
from marshmallow import fields
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

from movie.data_access.db_models import User
from movie.data_access.schema_definitions.user_schema import UserSchema
from movie.extensions import db, ma
from movie.middleware.restplus import api
from movie.serializers.user_serializer import user


def create_user(data):
    email_exist = User.query.filter_by(email=data.get('email')).first()

    if email_exist != None:
        data = {'failed':"Email Already Exists"}
    else:
        user = User(username=data.get('username'), email=data.get('email'), password=data.get('password'), admin=data.get('admin'), 
        createdAt=datetime.now(), updatedAt=datetime.now())    
        response=user.save()
        data = {'success':"User Registration Successfull"}        
    return data


def login_user(data):
    user = User.query.filter_by(email=data.get('email'), password=data.get('password')).first()

    if user != None:
        access_token = create_access_token(identity=data.get('email'))
        user_data={}
        user_data['username']=user.username
        user_data['email']=user.email
        user_data['admin']=user.admin
        user_data['access_token']=access_token
        response = user_data
    else: 
        response = {'unauthorized':"Email or Password is invalid"}
    return response    