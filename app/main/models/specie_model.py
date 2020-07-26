from .. import db
from app.main.models import pet_model
from app.main.models import breed_model

class SpecieModel(db.Model):
    __tablename__ = "specie"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    pet_has_specie_rel = db.relationship("PetModel", backref="specie", lazy=True)
    specie_has_breeds_rel = db.relationship("BreedModel", backref="specie", lazy=True)

    def __repr__(self):
        return "<specie '{}'>".format(self.public_id)