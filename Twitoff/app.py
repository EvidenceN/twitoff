"""Code for our app"""

from flask import Flask

# make our app factory

def create_app():
    app = Flask(__name__)

    # make route
    @app.rout('/')
    def root():
        return 'Welcome to Twitoff!!'

    return app