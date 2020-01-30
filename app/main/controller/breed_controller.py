from flask import request

from flask_restplus import Resource
from ..util.dto import BreedDto
from ..util.decorator import token_required, admin_token_required
from ..services.breed_service import *
from ..services.specie_service import get_a_specie

api = BreedDto.api
_breed = BreedDto.breed
parser = BreedDto.parser

@api.route("/<public_id>")
@api.response(404, "Breed not found")
class NewBreed(Resource):
    @admin_token_required
    @api.response(201, "Breed added")
    @api.doc("add breed", parser=parser)
    def post(self, public_id):
        specie = get_a_specie(public_id)

        breed_data = request.json

        return new_breed(data=breed_data, public_id=specie.public_id)

@api.route("/<public_id>")
@api.param("public_id", "The Breed identifier")
@api.response(404, "Breed not found.")
class BreedOperations(Resource):
    @admin_token_required
    @api.doc("get a breed")
    @api.marshal_with(_breed)
    def get(self, public_id):
        breed = get_a_breed(public_id)

        if not breed:
            api.abort(404)

        else:
            return breed

    @admin_token_required
    @api.doc("delete a breed")
    def delete(self, public_id):
        breed = delete_breed(public_id)

        if not breed:
            api.abort(404)

        else:
            return breed
        
    @admin_token_required
    @api.doc("update a breed")
    def put(self, public_id):
        breed_data = request.json

        breed = edit_breed(public_id, data=breed_data)

        if not breed:
            api.abort(404)

        else:
            return breed

@api.route("/specie/<specie_id>")
@api.param("specie_id", "Breeds with specific specie")
@api.response(404, "Breeds not found.")
class SpecieBreeds(Resource):
    @token_required
    @api.doc("get breeds with specific specie")
    @api.marshal_list_with(_breed, envelope="data")
    def get(self, specie_id):
        breeds = get_specie_breeds(specie_id=specie_id)

        if not breeds:
            api.abort(404)

        else:
            return breeds


@api.route("/all")
@api.response(404, "pets not found")
class GetAllPosts(Resource):
    @admin_token_required
    @api.doc("get all pets")
    @api.marshal_with(_breed)
    def get(self):
        pets = get_all_breeds()

        return pets