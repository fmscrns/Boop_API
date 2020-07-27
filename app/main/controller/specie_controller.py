from flask import request
from flask_restplus import Resource
from app.main.util.decorator import auth_token_required
from app.main.services.specie_service import SpecieService
from app.main.util.dto import SpecieDto

api = SpecieDto.api
get_specie_dto = SpecieDto.get_specie
create_specie_dto = SpecieDto.create_specie

@api.route("/")
class SpecieList(Resource):
    @auth_token_required
    @api.doc("get all species")
    @api.marshal_list_with(get_specie_dto, envelope="data")
    def get(self):
        return SpecieService.get_all_species()

    @auth_token_required
    @api.doc("create specie")
    @api.expect(create_specie_dto, validate=True)
    def post(self):
        post_data = request.json

        return SpecieService.create_specie(post_data)

@api.route("/specie/<specie_id>")
@api.param("specie_id", "specie identifier")
class Specie(Resource):
    @auth_token_required
    @api.doc("get specie")
    @api.marshal_with(get_specie_dto, skip_none=True)
    def get(self, specie_id):
        return SpecieService.get_specie(specie_id)