from .. import db
from app.main.models import specie, user

pet_kind_rel = db.Table("pet_kind_rel",
    db.Column("pet_id", db.String, db.ForeignKey("pet.public_id", ondelete="cascade")),
    db.Column("specie_id", db.String, db.ForeignKey("specie.public_id", ondelete="cascade")),
    db.Column("breed_id", db.String, db.ForeignKey("breed.public_id", ondelete="cascade"))
)

class Pet(db.Model):
    __tablename__ = "pet"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    pet_name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.String(200), nullable=True)
    birthday = db.Column(db.DateTime, nullable=True)
    sex = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(100,2), nullable=False)
    profPhoto_filename = db.Column(db.String(50), nullable=False, default="pet-default-profPhoto.jpg")
    coverPhoto_filename = db.Column(db.String(50), nullable=False, default="pet-default-coverPhoto.jpg")
    registered_on = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(15), nullable=False, default="owned")
    price = db.Column(db.Numeric(100,2), nullable=False, default="0.00")
    pet_owner = db.Column(db.String, db.ForeignKey('user.username', ondelete="cascade"))

    specie_rel = db.relationship("Specie", secondary=pet_kind_rel, backref=db.backref("pet", lazy=True), cascade="all, delete", passive_deletes=True)
    
    def __repr__(self):
        return "<pet '{}'>".format(self.pet_name)
