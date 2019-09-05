from setuptools import find_packages, setup

__version__ = '0.1'


setup(
    name='movie',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-restful',
        'flask-restplus',
        'flask-migrate',
        'flask-marshmallow',
        'marshmallow-sqlalchemy',
        'python-dotenv',
        'passlib'
    ],
    entry_points={
        'console_scripts': [
            'movie = movie.manage:cli'
        ]
    }
)
