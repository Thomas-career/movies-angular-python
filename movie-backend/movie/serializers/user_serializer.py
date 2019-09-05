from flask_restplus import fields

from movie.middleware.restplus import api

user = api.model('User', {

    'username' : fields.String(),
    'email' : fields.String(required=True),
    'password' : fields.String(required=True),
    'admin' : fields.Boolean(),
   
})
