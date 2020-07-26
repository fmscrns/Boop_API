<<<<<<< HEAD
import datetime, jwt, json
from app.main.models.user import User
from ..services.blacklist_service import save_token_to_blacklist
from ..services.user_service import get_a_user
from app.main.services.help import Helper

def login_user(data):
    try:
        user = User.query.filter_by(email=data.get("usernameOrEmail")).first()

        if user and user.check_password(data.get("password")):
            auth_token = Helper.encode_auth_token(user.public_id)

            if auth_token:
                return Helper.return_resp_obj("success", "Successfully logged in.", auth_token, 200)

        elif user is None:
            user = User.query.filter_by(username=data.get("usernameOrEmail")).first()
            
            if user and user.check_password(data.get("password")):
                auth_token = Helper.encode_auth_token(user.public_id)

                if auth_token:
                    return Helper.return_resp_obj("success", "Successfully logged in.", auth_token, 200)
            else:
                return Helper.return_resp_obj("fail", "Log in unsuccessful. Try again.", None, 401)

        else:
            return Helper.return_resp_obj("fail", "Log in unsuccessful. Try again.", None, 401)

    except Exception as e:
        return Helper.return_resp_obj("fail", "Try again.", None, 500)

def logout_user(data):
    if data:
        print(data)
        auth_token = data.split(" ")[0]

    else:
        auth_token = ""

    if auth_token:
        resp = Helper.decode_auth_token(auth_token)

        if not isinstance(resp, str):
            return save_token_to_blacklist(token=auth_token)

        else:
            response_object = {
                "status" : "fail",
                "message" : resp
            }

            return response_object, 401
    else:
        response_object = {
            "status" : "fail",
            "message" : "Provide a valid authorized token."
        }

        return response_object, 403
=======
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
>>>>>>> master
