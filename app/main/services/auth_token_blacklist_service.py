from app.main import db
from app.main.models.auth_token_blacklist_model import AuthTokenBlacklistModel

class AuthTokenBlacklistService:
    @staticmethod
    def get_blacklisted_auth_token(auth_token):
        try:
            return AuthTokenBlacklistModel.query.filter_by(auth_token=auth_token).first()

        except Exception:
            return None

    @staticmethod
    def blacklist_auth_token(auth_token):
        try:
            auth_token = AuthTokenBlacklistModel(auth_token=auth_token)

            db.session.add(auth_token)
            db.session.commit()

            return 200

        except Exception:
            return None
            