from .. import db
from app.main.models import pet, user, comment
# from app.main.services.user_service import get_logged_in_user

class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    content = db.Column(db.String(300), nullable=False)
    posted_on = db.Column(db.DateTime, nullable=False)
    post_author = db.Column(db.String, db.ForeignKey('user.username', ondelete="cascade"))
    profPhoto_filename = db.Column(db.String(50))

    def __repr__(self):
        return "<post '{}'>".format(self.public_id)
