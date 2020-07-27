from flask import request
from flask_restplus import Resource
from app.main.util.decorator import auth_token_required
from app.main.services.breed_service import BreedService
from app.main.util.dto import BreedDto

api = BreedDto.api
get_breed_dto = BreedDto.get_breed
create_breed_dto = BreedDto.create_breed

@api.route("/")
class BreedList(Resource):
    @auth_token_required
    @api.doc("create breed")
    @api.expect(create_breed_dto, validate=True)
    def post(self):
        post_data = request.json

        return BreedService.create_breed(post_data)

@api.route("/specie/<specie_id>/breeds")
@api.param("specie_id", "specie identifier")
class SpecieBreedList(Resource):
    @auth_token_required
    @api.doc("get specie breeds")
    @api.marshal_list_with(get_breed_dto, envelope="data")
    def get(self, specie_id):
        return BreedService.get_specie_breeds(specie_id)

@api.route("/breed/<breed_id>")
@api.param("breed_id", "breed identifier")
class Breed(Resource):
    @auth_token_required
    @api.doc("get breed")
    @api.marshal_with(get_breed_dto, skip_none=True)
    def get(self, breed_id):
        return BreedService.get_breed(breed_id)

