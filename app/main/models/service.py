from .. import db
from app.main.models import user

class Service(db.Model):
    __tablename__ = "service"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    service_name = db.Column(db.String(50))

    def __repr__(self):
        return "<service '{}'>".format(self.public_id)
