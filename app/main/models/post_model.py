from app.main import db
from app.main.models.user_model import UserModel
from app.main.models.comment_model import CommentModel

class PostModel(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.String(300), nullable=False)
    photo_fn = db.Column(db.String(50))
    registered_on = db.Column(db.DateTime, nullable=False)
    poster_user_username = db.Column(db.String, db.ForeignKey("user.username"), nullable=False)

    comment_parent_rel = db.relationship("CommentModel", backref="parent", lazy=True)
    
    def __repr__(self):
        return "<post '{}'>".format(self.public_id)