from .. import db

class ServiceType(db.Model):
    __tablename__ = "service_type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    service_type = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return "<service_type '{}'>".format(self.service_type)