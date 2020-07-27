from flask import request
from flask_restplus import Resource
from app.main.util.decorator import auth_token_required
from app.main.services.auth_service import AuthService
from app.main.util.dto import AuthDto

api = AuthDto.api
provide_auth_token_dto = AuthDto.provide_auth_token

@api.route("/login")
class Login(Resource):
    @api.doc("log in a user")
    @api.expect(provide_auth_token_dto, validate=True)
    def post(self):
        post_data = request.json

        if post_data:
            return AuthService.provide_auth_token(post_data)

@api.route("/logout")
class Logout(Resource):
    @auth_token_required
    @api.doc("log out a user")
    def post(self):
        authorization_header = request.headers.get("Authorization")

        return AuthService.dispose_auth_token(authorization_header.split(" ")[1])

