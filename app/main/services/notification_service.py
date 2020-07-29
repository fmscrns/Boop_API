import uuid, datetime
from app.main import db
from app.main.models.comment_model import NotificationModel
from app.main.services.user_service import UserService

class CommentService:
    @staticmethod
    def create_notification(auth_token, payload):
        try:
            get_current_user = UserService.get_current_user(auth_token)

            new_public_id = str(uuid.uuid4())

            new_notification = NotificationModel(
                public_id = new_public_id,
                represented_model_id = payload["model_id"],
                classification = payload["classification"],
                photo_fn = payload["photo_fn"],
                registered_on = datetime.datetime.utcnow(),
                recipient_user_username = get_current_user.username
            )

            db.session.add(new_notification)

            db.session.commit()

            return new_public_id

        except Exception:
            return None

    @staticmethod
    def get_current_user_notifications(auth_token, pagination_no):
        try:
          get_current_user = UserService.get_current_user(auth_token)

          return NotificationModel.query.filter_by(recipient_user_username=get_current_user.username).paginate(page=pagination_no, per_page=6).items
        
        except Exception:
            return None

    @staticmethod
    def get_notification(auth_token, notification_id):
        try:
            get_current_user = UserService.get_current_user(auth_token)
            get_notification_row = NotificationModel.query.filter_by(public_id=notification_id).first()

            if get_notification_row.recipient_user_username = get_current_user.username:
              return get_notification_row

        except Exception:
            return None

    