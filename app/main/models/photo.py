from .. import db
from app.main.models import pet, user, comment

class Photo(db.Model):
    __tablename__ = "photo"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    posted_on = db.Column(db.DateTime, nullable=False)
    uploader = db.Column(db.String, db.ForeignKey('user.public_id', ondelete="cascade"))
    filename = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<photo '{}'>".format(self.public_id)