from app.main import db

class BreedModel(db.Model):
    __tablename__ = "breed"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    parent_specie_id = db.Column(db.String, db.ForeignKey("parent.public_id"), nullable=False)

    pet_subgroup_rel = db.relationship("PetModel", backref="subgroup", lazy=True)

    def __repr__(self):
        return "<breed '{}'>".format(self.public_id)