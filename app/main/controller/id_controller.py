from flask_restx import Resource
from flask import request
from ..service.id_service import check_id, create_id
from ..util.dto import IdDto

api = IdDto.api
_id = IdDto.id

@api.route('/cle/verification')
@api.doc(params={'id': 'String: 1 alpha + 9 num'}, location='query')
class CheckID(Resource):
    @api.doc('ID integrity check')
    def get(self):
        """ ID integrity check """
        id = request.args.get('id', 1)
        return check_id(id)

@api.route('/cle/creation')
@api.doc(params={'id': 'String: 9 num'}, location='query')
class CheckID(Resource):
    @api.doc('ID creation')
    def get(self):
        """ ID creation """
        value = request.args.get('id', 1)
        id = create_id(value)
        if id == "bad_value":
            api.abort(400)
        else:
            return id
