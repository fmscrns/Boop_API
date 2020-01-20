from flask import request
from flask_restplus import Resource
from ..util.dto import ServiceDto
from ..util.decorator import token_required, admin_token_required
from ..services.user_service import get_logged_in_user
from ..services.service_service import *

api = ServiceDto.api
_service = ServiceDto.service
parser = ServiceDto.parser

@api.route("/")
class OfferService(Resource):
    @token_required
    @api.response(201, "Offered")
    @api.doc("create a service", parser=parser)
    def post(self):
        serv_data = request.json

        user = get_logged_in_user(request)

        user_id = user[0]["data"]["[public_id]"]

        return create_service(data=serv_data, public_id=user_id)

@api.route("/<public_id>")
@api.param("public_id", "The service identifier")
@api.response(404, "Service not found.")
class ServiceOperations(Resource):
    @token_required
    @api.doc("get a service")
    @api.marshal_with(_service)
    def get(self, public_id):
        service = get_a_service(public_id)

        if not service:
            api.abort(404)

        else:
            return service

    @token_required
    @api.doc("delete a service")
    def delete(self, public_id):
        service = delete_service(public_id)

        if not service:
            api.abort(404)
            
        else:
            return service

    @token_required
    @api.doc("update a service", parser=parser)
    def put(self, public_id):
        service_data = request.json

        service = update_service(data=service_data, public_id=public_id)
        
        if not service:
            api.abort(404)

        else:
            return service

@api.route("/user/<username>")
@api.param("username", "Services of a specific owner")
@api.response(404, "services not found.")
class GetUserServiceList(Resource):
    @token_required
    @api.doc("get services with specific owner")
    @api.marshal_list_with(_service, envelope="data")
    def get(self, username):
        service = get_user_service(username=username)

        return service

@api.route("/all")
@api.response(404, "services not found")
class GetAllPosts(Resource):
    @admin_token_required
    @api.doc("get all services")
    @api.marshal_with(_service, envelope='data')
    def get(self):
        services = get_all_services()

        return services
