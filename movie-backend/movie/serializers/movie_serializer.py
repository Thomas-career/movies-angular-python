from flask_restplus import fields

from movie.middleware.restplus import api

movie = api.model('Movie', {

    'Title' : fields.String(required=True),
    'Year'  : fields.String(),
    'Rated' : fields.String(),
    'Released' : fields.String(),
    'Runtime' : fields.String(),
    'Genre' : fields.String(),
    'Director' : fields.String(),
    'Writer' : fields.String(),
    'Actors' : fields.String(),
    'Plot' : fields.String(),
    'Language' : fields.String(),
    'Country' : fields.String(),
    'Awards' : fields.String(),
    'Poster' : fields.String(),
    # 'Ratings' : fields.String(),
    'Metascore' : fields.String(),
    'imdbRating' : fields.String(),
    'imdbVotes' : fields.String(),
    'imdbID' : fields.String(),
    'Type' : fields.String(),
    'DVD' : fields.String(),
    'BoxOffice' : fields.String(),
    'Production' : fields.String(),
    'Website' : fields.String(),
    'Response' :  fields.String()
})
