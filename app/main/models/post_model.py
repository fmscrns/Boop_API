from .. import db
from app.main.models import user_model
from app.main.models import comment_model

class PostModel(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.String(300), nullable=False)
    photo_fn = db.Column(db.String(50))
    created_on = db.Column(db.DateTime, nullable=False)
    user_creates_posts_rel = db.Column(db.String, db.ForeignKey("user.username"), nullable=False)
    post_has_comments_rel = db.relationship("CommentModel", backref="post", lazy=True)
    
    def __repr__(self):
        return "<post '{}'>".format(self.public_id)

    def __dto__(self):
        return {
            "id": self.id,
            "public_id": self.public_id,
            "content": self.content,
            "photo_fn": self.photo_fn,
            "created_on": self.created_on,
            "user_creator": self.user_creates_posts_rel
        }