from flask import request
from flask_restplus import Resource
from ..util.dto import TransactionDto
from ..util.decorator import token_required
from ..services.transaction_service import *
from ..services.user_service import get_logged_in_user
from ..models.pet import Pet

api = TransactionDto.api
_deal = TransactionDto.trans
parser = TransactionDto.parser

@api.route("/<public_id>")
class PostReq(Resource):
    @token_required
    @api.response(201, "Pet listed.")
    @api.doc("create a request", parser=parser)
    def post(self, public_id):
        post_data = request.json

        deal = User.query.filter_by(public_id=public_id).first

        return new_deal(data=post_data, username=user_username, public_id=pet_id)
