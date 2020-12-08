from flask import Flask
from flask_restx import Api


def create_app():
    #api = Api()
    app = Flask(__name__)
    #api.init_app(app)
    return app
