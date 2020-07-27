from app.main import db
import datetime

class AuthTokenBlacklistModel(db.Model):
    __tablename__ = "auth_token_blacklist"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    auth_token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.blacklisted_on = datetime.datetime.now()

    def __repr__(self):
        return "auth token: {}".format(self.auth_token)
