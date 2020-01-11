from flask import request
from flask_restplus import Resource
from ..util.dto import PostDto
from ..util.decorator import token_required
from ..services.user_service import get_logged_in_user
from ..services.post_service import *
from ..services.help import Helper

api = PostDto.api
_post = PostDto.post
parser = PostDto.parser

@api.route("/")
class CreatePost(Resource):
    @token_required
    @api.response(201, "Post created.")
    @api.doc("create a post", parser=parser)
    def post(self):
        post_data = request.json

        user = get_logged_in_user(request)

        user_username = user[0]["data"]["username"]

        return new_post(data=post_data, username=user_username)

@api.route("/<post_id>")
@api.param("post_id", "post identifier")
@api.response(404, "Post not found.")
class PostOperations(Resource):
    @token_required
    @api.doc("get a post")
    @api.marshal_with(_post)
    def get(self, post_id):
        post = get_a_post(post_id)

        if not post:
            api.abort(404)
        
        else:
            return post


    @token_required
    @api.doc("delete a post")
    def delete(self, post_id):
        post = delete_post(post_id)

        if not post:
            api.abort(404)
            
        else:
            return post
    
    @token_required
    @api.doc("update post")
    def put(self, post_id):
        post_data = request.json

        post = update_post(post_id=post_id, data=post_data)

        if not post:
            api.abort(404)
        
        else:
            return post

@api.route("/user/<username>")
@api.param("username", "post of a specific user")
@api.response(404, "posts not found.")
class GetUserPostList(Resource):
    @token_required
    @api.doc("get posts of a user")
    @api.marshal_with(_post, envelope='data')
    def get(self, username):
        posts = get_user_posts(username=username)

        return posts