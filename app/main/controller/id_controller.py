from flask_restx import Resource
from ..service.id_service import check_id
from ..util.dto import IdDto

api = IdDto.api
_id = IdDto.id

@api.route('/<id>')
#@api.expect(_id, validate=True)
class CheckID(Resource):
    @api.doc('ID integrity check')
    #@api.marshal_with(_id)
    def get(self, id):
        """ ID integrity check """
        return check_id(id)

