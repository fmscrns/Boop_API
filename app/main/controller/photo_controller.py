from flask import request
from flask_restplus import Resource
from ..util.dto import PhotoDto
from ..util.decorator import token_required
from ..services.user_service import get_logged_in_user
from ..services.photo_service import *
from ..services.help import Helper

api = PhotoDto.api
_photo = PostDto.post
parser = PostDto.parser

@api.route("/")
class CreatePhoto(Resource):
    @token_required
    @api.response(201, "Photo created.")
    @api.doc("create a photo", parser=parser)
    def post(self):
        post_data = request.json
        
        user = get_logged_in_user(request)
        
        user_username = user[0]["data"]["username"]

        t = save_new_photo(data=post_data, username=user_username)

@api.route("/insert")
class InsertPhoto(Resource):
    @token_required
    @api.response(201, "Photo inserted."
    @api.doc("insert a photo", parser=parser)
    def post(self):
        return insert_post_photo(request):
 
@api.route("/<public_id>")
@api.param("public_id", "photo identifier")
@api.response(404, "Photo not found.")
class PhotoOperations(Resource):
    @token_required
    @api.doc("get a photo")
    @api.marshal_with(_photo)
    def get(self, public_id):
        photo = get_a_photo(public_id)

        if not photo:
            api.abort(404)
        
        else:
            return photo


    @token_required
    @api.doc("delete a photo")
    def delete(self, public_id):
        photo = delete_photo(public_id)

        if not photo:
            api.abort(404)
            
        else:
            return photo
    
    @token_required
    @api.doc("update photo")
    def put(self, public_id):
        photo_data = request.json

        photo = update_photo(public_id=public_id, data=photo_data)

        if not photo:
            api.abort(404)
        
        else:
            return photo

@api.route("/user/<username>")
@api.param("username", "photos of a specific user")
@api.response(404, "photos not found.")
class GetUserPhotoList(Resource):
    @token_required
    @api.doc("get photos of a user")
    @api.marshal_with(_photos, envelope='data')
    def get(self, username):
        photos = get_user_photos(username=username)

        return photos

@api.route("/all")
@api.response(404, "photos not found")
class GetAllPhotos(Resource):
    @token_required
    @api.doc("get all photos")
    @api.marshal_with(_photos, envelope='data')
    def get(self):
        photos = get_all_photos()

        return photos
