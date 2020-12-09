from flask_restx import Namespace, fields

class IdDto:
    api = Namespace('client', description='id related operations')
    id = api.model('id',{
        'value': fields.String(required=True, description='Identifier\'s value to check or create')
    })
