FROM python:3.7.0-alpine3.8

# Current working directory
WORKDIR /app
COPY . /app
# Instal system dependencies
RUN apk add --no-cache build-base && apk add --no-cache mariadb-connector-c-dev && apk add libffi-dev
RUN pip3 install pipenv
# Generate requirements file from Pipenv.lock file
RUN pipenv lock --requirements > requirements.txt
# Install the requirements
RUN pip3 install --user --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "movie/manage.py", "run", "--host=0.0.0.0" ]