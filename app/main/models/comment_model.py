from .. import db
from app.main.models import user_model
from app.main.models import post_model

class CommentModel(db.Model):
    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.String(300), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    user_creates_comments_rel = db.Column(db.String, db.ForeignKey("user.username"), nullable=False)
    post_has_comments_rel = db.Column(db.String, db.ForeignKey("post.public_id"), nullable=False)

    def __repr__(self):
        return "<comment '{}'>".format(self.public_id)
