from .. import db
from app.main.models import pet

pet_price_rel = db.Table("pet_price_rel",
    db.Column("pet_id", db.String, db.ForeignKey("pet.public_id", ondelete="cascade")),
    db.Column("deal_id", db.String, db.ForeignKey("deal.public_id", ondelete="cascade"))
)

class Deal(db.Model):
    __tablename__ = "deal"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    posted_on = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Numeric(100,2), nullable=False, default="0.00")
    status = db.Column(db.String(15), nullable=False, default="adopt")
    deal_owner = db.Column(db.String, db.ForeignKey('user.username', ondelete="cascade"))

    pet_rel = db.relationship("Pet", secondary=pet_price_rel, backref=db.backref("pet", lazy=True), cascade="all, delete", passive_deletes=True)
    
    def __repr__(self):
        return "<Deal '{}'>".format(self.id)