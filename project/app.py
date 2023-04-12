from flask import Flask
from flask_restx import Api

from project.config import Config
from setup_db import db
from project.views.auth.auth import auth_ns
from project.views.main.directors_view import director_ns
from project.views.main.genres import genre_ns
from project.views.main.movie_view import movie_ns
from project.views.auth.user import user_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


app = create_app(Config())
app.debug = True

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)