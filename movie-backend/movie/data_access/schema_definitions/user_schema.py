from marshmallow import fields

from movie.data_access.db_models import User
from movie.extensions import ma


class UserSchema(ma.ModelSchema):

    user = fields.Nested('LenderSchema', only=['id', 'username', 'email','password','admin'])

    class Meta:
        model = User