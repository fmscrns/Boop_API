from .. import db
from app.main.models import pet_model
from app.main.models import specie_model

class BreedModel(db.Model):
    __tablename__ = "breed"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    pet_has_breed_rel = db.relationship("PetModel", backref="breed", lazy=True)
    specie_has_breeds_rel = db.Column(db.String, db.ForeignKey("specie.public_id"), nullable=False)

    def __repr__(self):
        return "<breed '{}'>".format(self.public_id)