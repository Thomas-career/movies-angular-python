# Prequal Service

### Requirements

* Python 3.7
* Pipenv

### To run in local:
  
$ `cd to  [project root directory]`

$ `pip install pipenv`

$ `pipenv --python 3.7`

$ `pipenv shell`

$ `pipenv install -e .`

$ `movie run`

#### To see routes

$ `movie routes`

#### To init tables

$ `movie init`

#### Help
$ `movie --help`

#### To deactivate environment
$ `exit`

### Microservice Server with swagger will be flashing in http://0.0.0.0:5000/api/v1/

### Quick Run - Make setup
##### To run server

$ `make init`

$ `make run`

## DB Migration

$ `CREATE DATABASE movieapp`

# IN PIPENV SHELL

$ `flask db init`

$ `flask db migrate`

$ `flask db upgrade`

## API ENDPOINTS

### All movies
- Path : `/movies`
- Method: `GET`
- Response: `200`

### Create movie
- Path : `/movies`
- Method: `POST`
- Fields: `movieDate, customerId, ItemId, movieQty, amount, walletId, movieStatus`
- Response: `201`

### Details a movie
- Path : `/movies/{id}`
- Method: `GET`
- Response: `200`

### Update movie
- Path : `/movies/{id}`
- Method: `PUT`
- Fields: `movieDate, customerId, ItemId, movieQty, amount, walletId, movieStatus`
- Response: `200`

### Delete movie
- Path : `/movies/{id}`
- Method: `DELETE`
- Response: `204`




