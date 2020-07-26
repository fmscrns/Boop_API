from flask import request
from flask_restplus import Resource
from ..util.decorator import auth_token_required
from ..services.user_service import UserService
from ..services.post_service import PostService
from ..services.comment_service import CommentService
from ..util.dto import CommentDto

api = CommentDto.api
get_comment_dto = CommentDto.get_comment
create_comment_dto = CommentDto.create_comment

@api.route("/")
class CommentList(Resource):
    @api.doc("create comment")
    @api.expect(create_comment_dto, validate=True)
    def post(self):
        authorization_header = request.headers.get("Authorization")
        post_data = request.json

        return CommentService.create_comment(authorization_header.split(" ")[1], post_data)

@api.route("/post/<post_id>/comments/page/<pagination_no>")
@api.param("post_id", "post identifier")
@api.param("pagination_no", "pagination number")
class PostCommentList(Resource):
    @auth_token_required
    @api.doc("get comments of a post")
    @api.marshal_list_with(get_comment_dto, envelope="data")
    def get(self, post_id, pagination_no):
        return CommentService.get_post_comments(post_id, int(pagination_no))

@api.route("/comment/<comment_id>")
@api.param("comment_id", "comment identifier")
class Comment(Resource):
    @auth_token_required
    @api.doc("get comment")
    @api.marshal_with(get_comment_dto, skip_none=True)
    def get(self, comment_id):
        return CommentService.get_comment(comment_id)