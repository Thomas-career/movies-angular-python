from marshmallow import fields

from movie.data_access.db_models import Movie
from movie.extensions import ma


class MovieSchema(ma.ModelSchema):

    movie = fields.Nested('LenderSchema', only=['id', 'Title', 'Year', 'Rated', 'Released', 'Runtime', 'Director', 
    'Writer', 'Actors', 'Plot', 'Language','Country', 'Awards', 'Poster', 'Ratings', 'Metascore', 'imdbRating'
    'imdbVotes','imdbID','Type','DVD','BoxOffice','Production', 'Website','Response'])

    class Meta:
        model = Movie