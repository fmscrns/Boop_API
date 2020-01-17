from .. import db
from app.main.models import pet, user
# from app.main.services.user_service import get_logged_in_user


class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.String(100), unique=True)
    content = db.Column(db.String(300), nullable=False)
    # post_gallery = db.Column(db.String(50), nullable=True)
    posted_on = db.Column(db.DateTime, nullable=False)
    post_author = db.Column(db.String, db.ForeignKey('user.username'))

    # pet_rel =  db.relationship("Pet", secondary=pet_post_rel, backref=db.backref("pet", lazy=True))


    def __repr__(self):
        return "<post '{}'>".format(self.post_id)
