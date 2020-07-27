from app.main import db
from app.main.models.user_model import UserModel

class FriendshipModel(db.Model):
    __tablename__ = "friendship"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    is_accepted = db.Column(db.Integer, default=0)
    sender_user_username = db.Column(db.String, db.ForeignKey("user.username"), nullable=False)
    recipient_user_username = db.Column(db.String, db.ForeignKey("user.username"), nullable=False)

    def __repr__(self):
        return "<Friendship '{}' and '{}'>".format(self.sender_user_username, self.recipient_user_username)