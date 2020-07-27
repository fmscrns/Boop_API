from app.main import db
from app.main.models.user_model import UserModel
from app.main.models.post_model import PostModel

class CommentModel(db.Model):
    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.String(300), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    commenter_user_username = db.Column(db.String, db.ForeignKey("user.username"), nullable=False)
    parent_post_id = db.Column(db.String, db.ForeignKey("post.public_id"), nullable=False)

    def __repr__(self):
        return "<comment '{}'>".format(self.public_id)