from functools import wraps
from flask import request
from app.main.services.user_service import UserService

def auth_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        authorization_header = request.headers.get("Authorization")

        if authorization_header.split(" ")[0] == "Bearer":
            get_current_user = UserService.get_current_user(authorization_header.split(" ")[1])

            if get_current_user:
                return f(*args, **kwargs)

    return decorated