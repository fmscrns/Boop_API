from flask import request
from flask_restplus import Resource
from ..util.dto import SpecieDto
from ..util.decorator import token_required, admin_token_required
from ..services.specie_service import *

api = SpecieDto.api
_specie = SpecieDto.specie
parser = SpecieDto.parser

@api.route("/")
class NewSpecie(Resource):
    @admin_token_required
    @api.response(201, "Specie added")
    @api.doc("add a new specie", parser=parser)
    def post(self):
        specie_data = request.json

        return new_specie(data=specie_data)

@api.route("/all")
class SpecieList(Resource):
    @token_required
    @api.doc("show list of all registered species")
    @api.marshal_list_with(_specie, envelope="data")
    def get(self):
        return get_all_species()

@api.route("/<public_id>")
@api.param("public_id", "The Specie identifier")
@api.response(404, "Specie not found.")
class SpecieOperations(Resource):
    @admin_token_required
    @api.doc("get a specie")
    @api.marshal_with(_specie)
    def get(self, public_id):
        specie = get_a_specie(public_id)

        if not specie:
            api.abort(404)

        else:
            return specie

    @admin_token_required
    @api.doc("delete specie")
    def delete(self, public_id):
        specie = delete_specie(public_id)

        if not specie:
            api.abort(404)

        else:
            return specie
    
    @admin_token_required
    @api.doc("update specie")
    def put(self, public_id):
        specie_data = request.json

        specie = edit_specie(public_id=public_id, data=specie_data)

        if not specie:
            api.abort(404)

        else:
            return specie