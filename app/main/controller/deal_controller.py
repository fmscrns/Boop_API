from flask import request
from flask_restplus import Resource
from ..util.dto import DealDto
from ..util.decorator import token_required
from ..services.deal_service import *
from ..services.user_service import get_logged_in_user
from ..models.pet import Pet

api = DealDto.api
_deal = DealDto.deal
parser = DealDto.parser

@api.route("/<public_id>")
class PostDeal(Resource):
    @token_required
    @api.response(201, "Pet listed.")
    @api.doc("create a transaction", parser=parser)
    def post(self, public_id):
        post_data = request.json

        user = get_logged_in_user(request)

        user_username = user[0]["data"]["username"]

        pet = Pet.query.filter_by(public_id=public_id).first()
        
        pet_id = pet.public_id

        return new_deal(data=post_data, username=user_username, public_id=pet_id)


@api.route("/<public_id>")
@api.param("public_id", "transaction identifier")
@api.response(404, "Transaction not found.")
class DealOperations(Resource):
    @token_required
    @api.doc("get a transaction")
    @api.marshal_with(_deal)
    def get(self, public_id):
        deal = get_a_deal(public_id)

        if not deal:
            api.abort(404)

        else:
            return deal
    

    @token_required
    @api.doc("delete a transaction")
    def delete(self, public_id):
        deal = delete_deal(public_id)

        if not deal:
            api.abort(404)
            
        else:
            return deal
    

    @token_required
    @api.doc("update info")
    def put(self, public_id):
        deal_data = request.json

        deal = update_deal(public_id, data=deal_data)

        if not deal:
            api.abort(404)
            
        else:
            return deal


@api.route("/user/<username>")
@api.param("username", "user identifier")
@api.response(404, "posts not found.")
class GetUserDealList(Resource):
    @token_required
    @api.doc("get transactions of a user")
    @api.marshal_with(_deal, envelope='data')
    def get(self, username):
        deals = get_user_deals(username=username)

        return deals

@api.route("/all")
@api.response(404, "deals not found")
class GetAllPosts(Resource):
    @token_required
    @api.doc("get all deals")
    @api.marshal_with(_deal, envelope='data')
    def get(self):
        deals = get_all_deals()

        return deals