import json
import logging
import traceback

from flask import jsonify
from flask_restplus import Api 


api = Api(version='1.0', title='Movie Service',
          description='Movie Microservices')
