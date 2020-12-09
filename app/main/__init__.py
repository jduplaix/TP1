from flask import Flask
from flask_restx import Api


def create_app():
    app = Flask(__name__)
    return app
