from movie.data_access.db_models.base import Base
from movie.extensions import db


class Movie(db.Model, Base):
    """Basic Movie model """
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100), nullable=False)
    Year  = db.Column(db.String(30))
    Rated = db.Column(db.String(50))
    Released = db.Column(db.String(50))
    Runtime = db.Column(db.String(10))
    Genre = db.Column(db.String(500))
    Director = db.Column(db.String(500))
    Writer = db.Column(db.String(500))
    Actors = db.Column(db.String(500))
    Plot = db.Column(db.String(1000))
    Language = db.Column(db.String(500))
    Country = db.Column(db.String(500))
    Awards = db.Column(db.String(500))
    Poster = db.Column(db.String(500))
    Ratings = db.relationship('Ratings', backref='movie', cascade='all, delete-orphan', lazy='dynamic')
    Metascore = db.Column(db.String(50))
    imdbRating = db.Column(db.String(50))
    imdbVotes = db.Column(db.String(50))
    imdbID = db.Column(db.String(100))
    Type = db.Column(db.String(100))
    DVD = db.Column(db.String(500))
    BoxOffice = db.Column(db.String(100))
    Production = db.Column(db.String(100))
    Website = db.Column(db.String(100))
    Response =  db.Column(db.String(500))
    createdAt = db.Column(db.String(30))
    updatedAt = db.Column(db.String(30)) 

    def __init__(self, **kwargs):
        super(Movie, self).__init__(**kwargs)

    def __repr__(self):
        return "<Movie %s>" % self.id

class Ratings(db.Model, Base):

    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key=True)
    Source = db.Column(db.String(120), nullable=False)
    Value = db.Column(db.String(120), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    createdAt = db.Column(db.String(30))
    updatedAt = db.Column(db.String(30)) 
    
    def __init__(self, **kwargs):
        super(Ratings, self).__init__(**kwargs)

    def __repr__(self):
        return '<Ratings %r>' % self.id    
