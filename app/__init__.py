from flask_restx import Api
from flask import Blueprint

from .main.controller.id_controller import api as id_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='TP1 API',
          version='1.0',
          description='Some random shitty but clean Flask API ...',
          )

api.add_namespace(id_ns, path='/')