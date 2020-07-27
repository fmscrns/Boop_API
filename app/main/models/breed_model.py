from .. import db
from app.main.models import pet_model
from app.main.models import specie_model

class BreedModel(db.Model):
    __tablename__ = "breed"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    parent_specie_id = db.Column(db.String, db.ForeignKey("specie.public_id"), nullable=False)

    pet_breed_rel = db.relationship("PetModel", backref="breed", lazy=True)

    def __repr__(self):
        return "<breed '{}'>".format(self.public_id)