from .. import db
from app.main.models import pet_model
from app.main.models import post_model
from app.main.models import comment_model
from app.main.services.auth_token_blacklist_service import AuthTokenBlacklistService

class FriendshipModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    connected_on = db.Column(db.DateTime, nullable=False)
    sender_user_username = db.Column(db.String, db.ForeignKey("user.username"), nullable=False)
    recipient_user_username = db.Column(db.String, db.ForeignKey("user.username"), nullable=False)

    def __repr__(self):
        return "<Friendship '{}' and '{}'>".format(self.sender_user_username, self.recipient_user_username)