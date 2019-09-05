import os

"""Default configuration

Use env var to override
"""
DEBUG = False
SECRET_KEY = "ksr"
DB_HOST = os.environ.get('DB_HOST', '0.0.0.0:3306')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
DB_NAME = os.environ.get('DB_NAME', 'movie_service')
SQLALCHEMY_DATABASE_URI = "mysql://{}:{}@{}/{}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = True
