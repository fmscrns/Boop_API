import uuid, datetime
from app.main import db
from app.main.models.user_model import UserModel
from app.main.models.follow_model import FollowModel

class FollowService:
    @staticmethod
    def create_follow(auth_token, post_data):
        try:
            get_current_user = UserService.get_current_user(auth_token)

            new_public_id = str(uuid.uuid4())

            new_follow = FollowModel(
                public_id = new_public_id,
                registered_on = datetime.datetime.utcnow(),
                following_user_username = get_current_user.username,
                followed_pet_id = post_data["followed_pet_id"]
            )
            
            db.session.add(new_follow)

            db.session.commit()

            return new_public_id

        except Exception:
            return None

    @staticmethod
    def get_user_follows(username, pagination_no):
        try:
            return FollowModel.query.filter_by(following_user_username=username).paginate(page=pagination_no, per_page=6).items
        
        except Exception:
            return None

    @staticmethod
    def get_pet_follows(pet_id, pagination_no):
        try:
            return FollowModel.query.filter_by(followed_pet_id=pet_id).paginate(page=pagination_no, per_page=6).items
        
        except Exception:
            return None

    @staticmethod
    def get_follow(follow_id):
        try:
            return FollowModel.query.filter_by(public_id=follow_id).first()

        except Exception:
            return None

    @staticmethod
    def delete_follow(auth_token, follow_id):
        try:
            get_current_user = UserService.get_current_user(auth_token)
            get_follow_row = FollowModel.query.filter_by(public_id=follow_id).first()

            if (get_follow_row.sender_user_username == get_current_user.username) or (get_follow_row.recipient_user_username == get_current_user.username):
                db.session.delete(get_follow_row)
                
                db.session.commit()

            return 200

        except Exception:
            return None
