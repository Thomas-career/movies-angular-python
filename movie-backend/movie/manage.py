import os

import click
from flask.cli import FlaskGroup

from movie.app import create_app


def create_prequal(info):
    environment = 'production' if os.environ['FLASK_ENV'] == 'production' else 'development'
    return create_app(cli=True, environment=environment)


@click.group(cls=FlaskGroup, create_app=create_prequal)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Init application, create database tables
    and create a new user named admin with password admin
    """
    from movie.extensions import db
    click.echo("create database")
    db.create_all()
    click.echo("done")


if __name__ == "__main__":
    cli()
