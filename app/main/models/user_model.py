import jwt, datetime
from app.main import db, flask_bcrypt
from app.main.config import key
from app.main.models.pet_model import PetModel
from app.main.models.post_model import PostModel
from app.main.models.comment_model import CommentModel
from app.main.services.auth_token_blacklist_service import AuthTokenBlacklistService

class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.String(100))
    email = db.Column(db.String(50), unique=True, nullable=False)
    profile_photo_fn = db.Column(db.String(50), default="user-default-profile-photo.jpg", nullable=False)
    cover_photo_fn = db.Column(db.String(50), default="user-default-cover-photo.jpg", nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    contact_no = db.Column(db.String(20), nullable=True)
    registered_on = db.Column(db.DateTime, nullable=False)

    post_poster_rel = db.relationship("PostModel", backref="poster", lazy=True)
    comment_commenter_rel = db.relationship("CommentModel", backref="commenter", lazy=True)
    friendship_sender_rel = db.relationship("UserFriendListModel", backref="sender", lazy=True)
    friendship_recipient_rel = db.relationship("UserFriendListModel", backref="recipient", lazy=True)
    
    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)

    @staticmethod
    def encode_auth_token(username):
        try:
            user = UserModel.query.filter_by(username=username).first()

            if user:
                payload = {
                    "exp" : datetime.datetime.utcnow() + datetime.timedelta(days=3650),
                    "iat" : datetime.datetime.utcnow(),
                    "sub" : username
                }

                return jwt.encode(payload, key, algorithm = "HS256")

        except Exception:
            return None

    @staticmethod  
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, key)
            
            if UserModel.query.filter_by(username=payload["sub"]).first():
                if not AuthTokenBlacklistService.get_blacklisted_auth_token(auth_token):
                    return payload["sub"]

        except Exception:
            return None