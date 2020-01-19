from .. import db
from app.main.models import user, deal

transaction_rel = db.Table("transaction_rel",
    db.Column("tans_id", db.String, db.ForeignKey("transaction.public_id", ondelete="cascade")),
    db.Column("req_id", db.String, db.ForeignKey("user.public_id", ondelete="cascade")),
    db.Column("deal_id", db.String, db.ForeignKey("deal.public_id", ondelete="cascade")),
    db.Column("owner_id", db.String, db.ForeignKey("user.public_id", ondelete="cascade")),
)

class Listing(db.Model):
    __tablename__ = "transaction"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    posted_on = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String, nullable=False, default="Pending")
    req_id = db.Column(db.String, db.ForeignKey('user.public_id', ondelete="cascade"))
    deal_id = db.Column(db.String, db.ForeignKey('deal.public_id', ondelete="cascade"))
    owner_id = db.Column(db.String, db.ForeignKey('user.public_id', ondelete="cascade"))

    transaction_rel = db.relationship("Deal", secondary=transaction_rel, backref=db.backref("deal", lazy=True), cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return "<Deal '{}'>".format(self.id)