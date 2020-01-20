from .. import db
from app.main.models import pet, user, comment, photo
# from app.main.services.user_service import get_logged_in_user

post_photo_rel = db.Table("post_photo_rel",
    db.Column("public_id", db.Integer, primary_key=True, autoincrement=True),
    db.Column("post_id", db.String, db.ForeignKey("post.public_id", ondelete="cascade")),
    db.Column("photo_id", db.String, db.ForeignKey("photo.public_id", ondelete="cascade"))
)

class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    content = db.Column(db.String(300), nullable=False)
    posted_on = db.Column(db.DateTime, nullable=False)
    post_author = db.Column(db.String, db.ForeignKey('user.username', ondelete="cascade"))

    photo_rel = db.relationship("Photo", secondary=post_photo_rel, backref=db.backref("post_photo_setter", lazy=True), cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return "<post '{}'>".format(self.public_id)
