import uuid, datetime
from app.main import db
from app.main.models.user_model import UserModel
from app.main.models.friendship_model import FriendshipModel

class FriendshipService:
    @staticmethod
    def create_friendship(auth_token, post_data):
        try:
            get_current_user = UserService.get_current_user(auth_token)
            get_friendship_row_as_sender = FriendshipModel.query.filter_by(sender_user_username=get_current_user.username).filter_by(recipient_user_username=post_data["recipient_user_username"]).first()
            get_friendship_row_as_recipient = FriendshipModel.query.filter_by(sender_user_username=post_data["recipient_user_username"]).filter_by(recipient_user_username=get_current_user.username).first()

            if not (get_friendship_row_as_sender or get_friendship_row_as_recipient):
                new_public_id = str(uuid.uuid4())

                new_friendship = FriendshipModel(
                    public_id = new_public_id,
                    connected_on = datetime.datetime.utcnow(),
                    sender_user_username = get_current_user.username,
                    recipient_user_username = post_data["recipient_user_username"]
                )
                
                db.session.add(new_friendship)

                db.session.commit()

                return new_public_id

        except Exception:
            return None

    @staticmethod
    def get_user_friendships(username, pagination_no):
        try:
            return FriendshipModel.query.filter_by(sender_user_username=username).filter_by(is_accepted=1).paginate(page=pagination_no, per_page=6).items

        except Exception:
            return None

    @staticmethod
    def get_friendship(friendship_id):
        try:
            return FriendshipModel.query.filter_by(public_id=friendship_id).first()

        except Exception:
            return None

    @staticmethod
    def update_friendship(auth_token, friendship_id):
        try:
            get_current_user = UserService.get_current_user(auth_token)
            get_friendship_row = FriendshipModel.query.filter_by(public_id=friendship_id).first()

            if get_friendship_row.recipient_user_username == get_current_user.username:
                get_friendship_row.is_accepted = 1
                
                db.session.commit()

                return 200

        except Exception:
            return None

    @staticmethod
    def delete_friendship(auth_token, friendship_id):
        try:
            get_current_user = UserService.get_current_user(auth_token)
            get_friendship_row = FriendshipModel.query.filter_by(public_id=friendship_id).first()

            if (get_friendship_row.sender_user_username == get_current_user.username) or (get_friendship_row.recipient_user_username == get_current_user.username):
                db.session.delete(get_friendship_row)
                
                db.session.commit()

            return 200

        except Exception:
            return None
