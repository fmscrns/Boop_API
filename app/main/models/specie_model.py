from app.main import db

class SpecieModel(db.Model):
    __tablename__ = "specie"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)

    pet_group_rel = db.relationship("PetModel", backref="group", lazy=True)
    breed_parent_rel = db.relationship("BreedModel", backref="parent", lazy=True)

    def __repr__(self):
        return "<specie '{}'>".format(self.public_id)