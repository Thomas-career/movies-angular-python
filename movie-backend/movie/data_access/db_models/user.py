from movie.data_access.db_models.base import Base
from movie.extensions import db

class User(db.Model, Base):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(20))
    admin = db.Column(db.Boolean, default=False)
    createdAt = db.Column(db.String(30))
    updatedAt = db.Column(db.String(30)) 

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return "<User %s>" % self.id