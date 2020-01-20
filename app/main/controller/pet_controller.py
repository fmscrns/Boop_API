from flask import request
from flask_restplus import Resource
from ..util.dto import PetDto
from ..util.decorator import token_required, admin_token_required
from ..models.user import User
from ..services.user_service import get_logged_in_user
from ..services.pet_service import *
from ..services.help import Helper

api = PetDto.api
_pet = PetDto.pet
parser = PetDto.parser

@api.route("/")
class PostPet(Resource):
    @token_required
    @api.response(201, "Pet successfully created.")
    @api.doc("register a pet", parser=parser)
    def post(self):
        post_data = request.json

        user = get_logged_in_user(request)
        
        user_id = user[0]["data"]["public_id"]
        
        return save_new_pet(data=post_data, public_id=user_id)

@api.route("/<public_id>")
@api.param("public_id", "The Pet identifier")
@api.response(404, "Pet not found.")
class PetOperations(Resource):
    @token_required
    @api.doc("get a pet")
    @api.marshal_with(_pet)
    def get(self, public_id):
        pet = get_a_pet(public_id)

        if not pet:
            api.abort(404)

        else:
            return pet

    @token_required
    @api.doc("delete a pet")
    def delete(self, public_id):
        pet = delete_pet(public_id)

        if not pet:
            api.abort(404)
            
        else:
            return pet

    @token_required
    @api.doc("update a pet", parser=parser)
    def put(self, public_id):
        post_data = request.json

        pet = update_pet(public_id=public_id, data=post_data)
        
        if not pet:
            api.abort(404)

        else:
            return pet

@api.route("/user/<username>")
@api.param("username", "Pets of a specific owner")
@api.response(404, "Pets not found.")
class GetUserPetList(Resource):
    @token_required
    @api.doc("get pets with specific owner")
    @api.marshal_list_with(_pet, envelope="data")
    def get(self, username):
        pets = get_user_pets(username=username)

        return pets

@api.route("/specie/<specie_id>")
@api.param("specie_id", "Pets with specific specie")
@api.response(404, "Pets not found.")
class GetSpeciePetList(Resource):
    @token_required
    @api.doc("get pets with specific specie")
    @api.marshal_list_with(_pet, envelope="data")
    def get(self, specie_id):
        pets = get_specie_pets(specie_id=specie_id)

        return pets

@api.route("/breed/<breed_id>")
@api.param("breed_id", "Pets with specific breed")
@api.response(404, "Pets not found.")
class GetBreedPetList(Resource):
    @token_required
    @api.doc("get pets with specific breed")
    @api.marshal_list_with(_pet, envelope="data")
    def get(self, breed_id):
        pets = get_breed_pets(breed_id=breed_id)

        return pets

@api.route("/all")
@api.response(404, "pets not found")
class GetAllPosts(Resource):
    @admin_token_required
    @api.doc("get all pets")
    @api.marshal_with(_pet, envelope='data')
    def get(self):
        pets = get_all_pets()

        return pets


@api.route("/<public_id>/transfer/<user_id>")
@api.response(404, "Update pet owner")
class PetTransfer(Resource):
    @token_required
    def put(self, public_id, user_id):

        user = User.query.filter_by(public_id=user_id).first()

        pet = pet_transfer(public_id=public_id, new_owner_id=user.public_id)

        return pet

