from flask import request
from flask_restplus import Resource
from app.main.util.decorator import auth_token_required
from app.main.services.friendship_service import FriendshipService
from app.main.util.dto import FriendshipDto

api = FriendshipDto.api
get_friendship_dto = FriendshipDto.get_friendship
create_friendship_dto = FriendshipDto.create_friendship

@api.route("/")
class FriendshipList(Resource):
    @auth_token_required
    @api.doc("create friendship")
    @api.expect(create_friendship_dto, validate=True)
    def post(self):
        authorization_header = request.headers.get("Authorization")
        post_data = request.json

        return FriendshipService.create_friendship(authorization_header.split(" ")[1])

@api.route("/user/<username>/friendships/page/<pagination_no>")
@api.param("username", "user identifier")
@api.param("pagination_no", "pagination number")
class UserFriendshipList(Resource):
    @auth_token_required
    @api.doc("get user friendships")
    @api.marshal_list_with(get_friendship_dto, envelope="data")
    def get(self, username, pagination_no):
        return FriendshipService.get_user_friendships(username, int(pagination_no))

@api.route("/friendship/<friendship_id>")
@api.param("friendship_id", "friendship identifier")
class Friendship(Resource):
    @auth_token_required
    @api.doc("get friendship")
    @api.marshal_with(get_friendship_dto, skip_none=True)
    def get(self, friendship_id):
        return FriendshipService.get_friendship(friendship_id)

    @auth_token_required
    @api.doc("update friendship")
    def put(self, friendship_id):
        authorization_header = request.headers.get("Authorization")

        return FriendshipService.update_friendship(authorization_header.split(" ")[1], friendship_id)

    @auth_token_required
    @api.doc("delete friendship")
    def delete(self, friendship_id):
        authorization_header = request.headers.get("Authorization")

        return FriendshipService.delete_friendship(authorization_header.split(" ")[1], friendship_id)