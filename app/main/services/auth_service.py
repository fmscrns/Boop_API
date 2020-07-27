from app.main.models.user_model import UserModel
from app.main.models.auth_token_blacklist_model import AuthTokenBlacklistModel
from ..services.auth_token_blacklist_service import AuthTokenBlacklistService

class AuthService:
    @staticmethod
    def provide_auth_token(post_data):
        try:
            get_user_row_with_username = UserModel.query.filter_by(username=post_data.get("username_or_email_address")).first()
            get_user_row_with_email_address = UserModel.query.filter_by(email_address=post_data.get("username_or_email_address")).first()

            if get_user_row_with_username and get_user_row_with_username.check_password(post_data.get("password")):
                return UserModel.encode_auth_token(get_user_row_with_username.username).decode()

            elif get_user_row_with_email_address and get_user_row_with_email_address.check_password(post_data.get("password")):
                return UserModel.encode_auth_token(get_user_row_with_email_address.username).decode()

        except Exception:
            return None

    @staticmethod
    def dispose_auth_token(auth_token):
        try:
            if UserModel.decode_auth_token(auth_token):
                return AuthTokenBlacklistService.blacklist_auth_token(auth_token)

        except Exception:
            return None
