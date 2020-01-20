from .. import db
from app.main.models import user, deal, request

class Request(db.Model):
    __tablename__ = "request"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    req_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(15), nullable=False, default="pending")
    deal_id = db.Column(db.String, db.ForeignKey('deal.public_id', ondelete="cascade"))
    requester_id = db.Column(db.String, db.ForeignKey('user.public_id', ondelete="cascade"))

    def __repr__(self):
        return "<Request '{}'>".format(self.id)
