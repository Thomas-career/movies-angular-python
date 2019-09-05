from flask_restplus import fields

from movie.middleware.restplus import api

login = api.model('User', {

    'email' : fields.String(required=True),
    'password' : fields.String(required=True)
   
})
