import collections
from datetime import datetime

from flask import jsonify, request
from flask_restplus import Resource
from marshmallow import fields

from movie.data_access.db_models import Movie, Ratings
from movie.data_access.schema_definitions.movie_schema import MovieSchema
from movie.extensions import db, ma
from movie.middleware.restplus import api
from movie.serializers.movie_serializer import movie


def get_movie(movie_id):
    schema = MovieSchema()
    movie = Movie.query.filter_by(id=movie_id).first()
    if movie != None:
        response = schema.dump(movie)
    else: 
        response = {'message':"movie not found"}
    return response

def update_movie(movie_id, movie_data):
    schema = MovieSchema(partial=True)
    movie= get_movie(movie_id)
    if not movie.get('message'):
        data = db.session.query(Movie).get(movie_id)

        data.Title = movie_data.get('Title') or data.Title
        data.Year  = movie_data.get('Year') or data.Year
        data.Rated = movie_data.get('Rated') or data.Rated
        data.Released = movie_data.get('Released') or data.Released
        data.Runtime = movie_data.get('Runtime') or data.Runtime
        data.Genre = movie_data.get('Genre') or data.Genre
        data.Director = movie_data.get('Director') or data.Director
        data.Writer = movie_data.get('Writer') or data.Writer
        data.Actors = movie_data.get('Actors') or data.Actors
        data.Plot = movie_data.get('Plot') or data.Plot
        data.Language = movie_data.get('Language') or data.Language
        data.Country = movie_data.get('Country') or data.Country
        data.Awards = movie_data.get('Awards') or data.Awards
        data.Poster = movie_data.get('Poster') or data.Poster
        data.Metascore = movie_data.get('Metascore') or data.Metascore
        data.imdbRating = movie_data.get('imdbRating') or data.imdbRating
        data.imdbVotes = movie_data.get('imdbVotes') or data.imdbVotes
        data.imdbID = movie_data.get('imdbID') or data.imdbID
        data.Type = movie_data.get('Type') or data.Type
        data.DVD = movie_data.get('DVD') or data.DVD
        data.BoxOffice = movie_data.get('BoxOffice') or data.BoxOffice
        data.Production = movie_data.get('Production') or data.Production
        data.Website = movie_data.get('Website') or data.Website
        data.Response =  movie_data.get('Response') or data.Response
        data.updatedAt = datetime.now()
        
        # data.Ratings =  movie_data.get('Ratings') or data.Ratings

        for x in movie_data.get('Ratings'):
            #print(x)
            if type(x) is not int:    
                if 'id' in x:
                    ratingdata = db.session.query(Ratings).get(x['id'])
                    ratingdata.Source = x['Source'] or ratingdata.Source
                    ratingdata.Value = x['Value'] or ratingdata.Value
                    data.Ratings.append(ratingdata)
                else:
                    rating = Ratings(Source=x['Source'], Value=x['Value'], createdAt=datetime.now(), updatedAt=datetime.now())
                    data.Ratings.append(rating)

        db.session.commit()
        movie_data['id'] = movie['id']
    else:
        movie_data = movie
    return movie_data

def delete_movie(movie_id):
    response= get_movie(movie_id)
    if not response.get('message'):
        movie = Movie.query.get_or_404(movie_id)
        movie.delete()
        response = {'removed':"movie deleted"}
    return response

def get_all_movie():
    schema = MovieSchema(many=True)
    query = Movie.query
    response = schema.dump(query)
    return response

def get_all_movie_pagination(page=1):
    schema = MovieSchema(many=True)
    per_page = 10
    query = Movie.query.order_by(Movie.id.asc()).paginate(page,per_page,error_out=False)
    response = schema.dump(query.items)
    return response

def post_movie(data):

    movie = Movie(Title=data.get('Title'), Year=data.get('Year'), Rated=data.get('Rated'), Released=data.get('Released'), Runtime=data.get('Runtime'), 
    Genre=data.get('Genre'), Director=data.get('Director'), Writer=data.get('Writer'), Actors=data.get('Actors'), Plot=data.get('Plot'),
    Language=data.get('Language'), Country=data.get('Country'), Awards=data.get('Awards'), Poster=data.get('Poster'), Metascore=data.get('Metascore'),
    imdbRating=data.get('imdbRating'), imdbVotes=data.get('imdbVotes'), imdbID=data.get('imdbID'),Type=data.get('Type'), DVD=data.get('DVD'),
    BoxOffice=data.get('BoxOffice'), Production=data.get('Production'), Website=data.get('Website'),Response=data.get('Response'),
    createdAt=datetime.now(), updatedAt=datetime.now())

    for x in data.get('Ratings'):
        #print(x)
        rating = Ratings(Source=x['Source'], Value=x['Value'], createdAt=datetime.now(), updatedAt=datetime.now())
        movie.Ratings.append(rating)

    response=movie.save()
    data['id']=response.id
    return data