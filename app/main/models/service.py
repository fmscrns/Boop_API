from .. import db
from app.main.models import user, service_type

class Service(db.Model):
    __tablename__ = "service"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    service_name = db.Column(db.String(50))
    days = db.Column(db.String(100))
    open_time = db.Column(db.Time)
    close_time = db.Column(db.Time)
    description = db.Column(db.String(100))
    service_owner = db.Column(db.String, db.ForeignKey('user.username', ondelete="cascade"))
    
    has_types = db.relationship("ServiceType", backref="type", lazy=True)

    def __repr__(self):
        return "<service '{}'>".format(self.public_id)
