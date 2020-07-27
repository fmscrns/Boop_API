from flask import request
from flask_restplus import Resource
from app.main.util.decorator import auth_token_required
from app.main.services.user_service import UserService
from app.main.util.dto import UserDto

api = UserDto.api
get_user_dto = UserDto.get_user
create_user_dto = UserDto.create_user
get_current_user_dto = UserDto.get_current_user
update_current_user_dto = UserDto.update_current_user

@api.route("/")
class UserList(Resource):
    @api.doc("create user")
    @api.expect(create_user_dto, validate=True)
    def post(self):
        post_data = request.json
        
        return UserService.create_user(post_data)

@api.route("/user/<username_or_email>")
@api.param("username_or_email", "user identifier")
class User(Resource):
    @auth_token_required
    @api.doc("get user")
    @api.marshal_with(get_user_dto, skip_none=True)
    def get(self, username_or_email):
        return UserService.get_user(username_or_email)

@api.route("/current_user")
class CurrentUser(Resource):
    @api.doc("get current user")
    @api.marshal_with(get_current_user_dto, skip_none=True)
    def get(self):
        authorization_header = request.headers.get("Authorization")

        return UserService.get_current_user(authorization_header.split(" ")[1])
                    
    @api.doc("update current user")
    @api.expect(update_current_user_dto, validate=True)
    def put(self):
        authorization_header = request.headers.get("Authorization")
        post_data = request.json

        return UserService.update_current_user(authorization_header.split(" ")[1], post_data)

    
