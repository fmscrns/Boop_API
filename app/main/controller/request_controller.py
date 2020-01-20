from flask import request
from flask_restplus import Resource
from ..util.dto import RequestDto
from ..util.decorator import token_required
from ..services.request_service import *

api = RequestDto.api
_request = RequestDto.request
parser = RequestDto.parser

@api.route("/<deal_id>/request/<user_id>")
class PostRequest(Resource):
    @token_required
    @api.response(201, "Request sent.")
    @api.doc("request for a trade", parser=parser)
    def post(self, deal_id, user_id):

        return new_request(deal_id=deal_id, user_id=user_id)

@api.route("/<public_id>")
@api.param("public_id", "request identifier")
@api.response(404, "Request not found.")
class RequestOperations(Resource):
    @token_required
    @api.doc("get a request")
    @api.marshal_with(_request)
    def get(self, public_id):
        req = get_a_request(public_id)

        if not req:
            api.abort(404)
        
        else:
            return req
    
    @token_required
    @api.doc("delete a request")
    def delete(self, public_id):
        req = delete_request(public_id)

        if not req:
            api.abort(404)
            
        else:
            return req

    # @token_required
    # @api.dov("approve request")
    # def put(self, public_id):
    #     req = get_a_request(public_id)

    #     if

