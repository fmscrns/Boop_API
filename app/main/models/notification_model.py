import jwt, datetime
from app.main import db, flask_bcrypt
from app.main.config import key
from app.main.services.auth_token_blacklist_service import AuthTokenBlacklistService

#   classification types:
#   0 is follow under current user's pets
#   1 is like under current user's posts
#   2 is comment under current user's posts

class NotificationModel(db.Model):
    __tablename__ = "notification"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    represented_model_id = db.Column(db.String(100), nullable=False)
    classification = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(300), nullable=False)
    photo_fn = db.Column(db.String(50))
    is_read = db.Column(db.Boolean, default=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    recipient_user_username = db.Column(db.String, db.ForeignKey("recipient.username"), nullable=False)
    
    def __repr__(self):
        return "<Notification '{}'>".format(self.public_id)