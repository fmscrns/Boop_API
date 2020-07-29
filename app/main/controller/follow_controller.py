from flask import request
from flask_restplus import Resource
from app.main.util.decorator import auth_token_required
from app.main.services.follow_service import FollowService
from app.main.util.dto import UserDto
from app.main.util.dto import PetDto
from app.main.util.dto import FollowDto

api = FollowDto.api
create_follow_dto = FollowDto.create_follow
get_follow_dto = FollowDto.get_follow

@api.route("/")
class FollowList(Resource):
    @auth_token_required
    @api.doc("create follow")
    @api.expect(create_follow_dto, validate=True)
    def post(self):
        authorization_header = request.headers.get("Authorization")
        post_data = request.json

        return FollowService.create_follow(authorization_header.split(" ")[1], post_data)

@api.route("/user/<username>/follows/page/<pagination_no>")
@api.param("username", "user identifier")
@api.param("pagination_no", "pagination number")
class UserFollowList(Resource):
    @auth_token_required
    @api.doc("get user follows")
    @api.marshal_list_with(get_follow_dto, envelope="data")
    def get(self, username, pagination_no):
        return FollowService.get_user_follows(username, int(pagination_no))

@api.route("/pet/<pet_id>/follows/page/<pagination_no>")
@api.param("pet_id", "user identifier")
@api.param("pagination_no", "pagination number")
class PetFollowList(Resource):
    @auth_token_required
    @api.doc("get pet followers")
    @api.marshal_list_with(get_follow_dto, envelope="data")
    def get(self, pet_id, pagination_no):
        return FollowService.get_pet_follows(pet_id, int(pagination_no))

@api.route("/follow/<follow_id>")
@api.param("follow_id", "follow identifier")
class Follow(Resource):
    @auth_token_required
    @api.doc("get follow")
    @api.marshal_with(get_follow_dto, skip_none=True)
    def get(self, follow_id):
        return FollowService.get_follow(follow_id)

    @auth_token_required
    @api.doc("delete follow")
    def delete(self, follow_id):
        authorization_header = request.headers.get("Authorization")

        return FollowService.delete_follow(authorization_header.split(" ")[1], follow_id)