from flask import request
from flask_restplus import Resource
from app.main.util.decorator import auth_token_required
from app.main.services.pet_service import PetService
from app.main.util.dto import PetDto

api = PetDto.api
get_pet_dto = PetDto.get_pet
create_pet_dto = PetDto.create_pet
update_pet_dto = PetDto.update_pet

@api.route("/")
class PetList(Resource):
    @auth_token_required
    @api.doc("create pet")
    @api.expect(create_pet_dto, validate=True)
    def post(self):
        authorization_header = request.headers.get("Authorization")
        post_data = request.json

        return PetService.create_pet(authorization_header.split(" ")[1], post_data)

@api.route("/user/<username>/pets/page/<pagination_no>")
@api.param("username", "user identifier")
@api.param("pagination_no", "pagination number")
class UserPetList(Resource):
    @auth_token_required
    @api.doc("get user pets")
    @api.marshal_list_with(get_pet_dto, envelope="data")
    def get(self, username, pagination_no):
        return PetService.get_user_pets(username, int(pagination_no))

@api.route("/pet/<pet_id>")
@api.param("pet_id", "pet identifier")
class Pet(Resource):
    @auth_token_required
    @api.doc("get pet")
    @api.marshal_with(get_pet_dto, skip_none=True)
    def get(self, pet_id):
        return PetService.get_pet(pet_id)

    @auth_token_required
    @api.doc("update pet")
    @api.expect(update_pet_dto, validate=True)
    def put(self, pet_id):
        authorization_header = request.headers.get("Authorization")
        post_data = request.json

        return PetService.update_pet(authorization_header.split(" ")[1], pet_id, post_data)

    @auth_token_required
    @api.doc("delete pet")
    def delete(self, pet_id):
        authorization_header = request.headers.get("Authorization")

        return PetService.delete_pet(authorization_header.split(" ")[1], pet_id)