import datetime, uuid
from app.main import db
from app.main.models.user_model import UserModel

class UserService:
    @staticmethod
    def create_user(post_data):
        try:
            get_user_row_by_username = UserModel.query.filter_by(username=post_data["username"]).first()
            get_user_row_by_email_address = UserModel.query.filter_by(email_address=post_data["email_address"]).first()

            if not (get_user_row_by_username or get_user_row_by_email_address):
                new_username = post_data["username"]

                new_user = UserModel(
                    is_admin = False,
                    username = new_username,
                    first_name = post_data["first_name"],
                    last_name = post_data["last_name"],
                    email_address = post_data["email_address"],
                    password = post_data["password"],
                    contact_no = post_data["contact_no"],
                    registered_on = datetime.datetime.utcnow()
                )

                db.session.add(new_user)

                db.session.commit()

                return UserModel.encode_auth_token(new_username).decode()

        except Exception as e:
            return None

    @staticmethod
    def get_user(username_or_email_address):
        try:
            return UserModel.query.filter_by(username=username_or_email_address).first() or UserModel.query.filter_by(email_address=username_or_email_address).first()

        except Exception as e:
            return None
            
    @staticmethod
    def get_current_user(auth_token):
        try:
            return UserModel.query.filter_by(username=UserModel.decode_auth_token(auth_token)).first()

        except Exception as e:
            return None

    @staticmethod
    def update_current_user(auth_token, post_data):
        try:
            get_current_user = UserService.get_current_user(auth_token)

            get_current_user.first_name = post_data["first_name"]
            get_current_user.last_name = post_data["last_name"]
            get_current_user.bio = post_data["bio"]
            get_current_user.contact_no = post_data["contact_no"]
            get_current_user.profile_photo_fn = post_data["profile_photo_fn"]
            get_current_user.cover_photo_fn = post_data["cover_photo_fn"]

            db.session.commit()

            return 200

        except Exception as e:
            return None