from .. import db
from app.main.models import pet

pet_price_rel = db.Table("pet_price_rel",
    db.Column("pet_id", db.String, db.ForeignKey("pet.public_id")),
    db.Column("deal_id", db.String, db.ForeignKey("deal.public_id"))
)

class Deal(db.Model):
    __tablename__ = "deal"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    posted_on = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Numeric(100,2), nullable=False, default="0.00")
    for_sale = db.Column(db.Boolean, nullable=False, default=False)
    for_adoption = db.Column(db.Boolean, nullable=False, default=False)
    deal_owner = db.Column(db.String, db.ForeignKey('user.username'))

    pet_rel = db.relationship("Pet", secondary=pet_price_rel, backref=db.backref("pet", lazy=True))
    
    def __repr__(self):
        return "<Deal '{}'>".format(self.id)