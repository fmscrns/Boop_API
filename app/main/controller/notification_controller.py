from flask import request
from flask_restplus import Resource
from app.main.util.decorator import auth_token_required
from app.main.services.notification_service import NotificationService
from app.main.util.dto import NotificationDto

api = NotificationDto.api
create_notification_dto = NotificationDto.create_notification
get_notification_dto = NotificationDto.get_notification

@api.route("/current_user/notifications/page/<pagination_no>")
@api.param("pagination_no", "pagination number")
class CurrentUserNotificationList(Resource):
    @auth_token_required
    @api.doc("get current user notifications")
    @api.marshal_list_with(get_notification_dto, envelope="data")
    def get(self, pagination_no):
      authorization_header = request.headers.get("Authorization")

      return NotificationService.get_current_user_notifications(authorization_header.split(" ")[1], int(pagination_no))

@api.route("/notification/<notification_id>")
@api.param("notification_id", "notification identifier")
class Notification(Resource):
    @auth_token_required
    @api.doc("get notification")
    @api.marshal_with(get_notification_dto, skip_none=True)
    def get(self, notification_id):
      authorization_header = request.headers.get("Authorization")

      return NotificationService.get_notification(authorization_header.split(" ")[1], notification_id)

    @auth_token_required
    @api.doc("delete notification")
    def delete(self, notification_id):
      authorization_header = request.headers.get("Authorization")

      return NotificationService.delete_notification(authorization_header.split(" ")[1], notification_id)