from flask import request
from flask_restplus import Resource
from app.main.util.decorator import auth_token_required
from app.main.services.post_service import PostService
from app.main.util.dto import PostDto

api = PostDto.api
get_post_dto = PostDto.get_post
create_post_dto = PostDto.create_post

@api.route("/")
class PostList(Resource):
    @auth_token_required
    @api.doc("create post")
    @api.expect(create_post_dto, validate=True)
    def post(self):
        authorization_header = request.headers.get("Authorization")
        post_data = request.json

        return PostService.create_post(authorization_header.split(" ")[1], post_data)

@api.route("/user/<username>/posts/page/<pagination_no>")
@api.param("username", "user identifier")
@api.param("pagination_no", "pagination number")
class UserPostList(Resource):
    @auth_token_required
    @api.doc("get user posts")
    @api.marshal_with(get_post_dto, envelope="data")
    def get(self, username, pagination_no):
        return PostService.get_user_posts(username, int(pagination_no))

@api.route("/post/<post_id>")
@api.param("post_id", "post identifier")
class Post(Resource):
    @auth_token_required
    @api.doc("get post")
    @api.marshal_with(get_post_dto)
    def get(self, post_id):
        return PostService.get_post(post_id)

    @auth_token_required
    @api.doc("delete post")
    def delete(self, post_id):
        authorization_header = request.headers.get("Authorization")

        return PostService.delete_post(authorization_header.split(" ")[1], post_id)