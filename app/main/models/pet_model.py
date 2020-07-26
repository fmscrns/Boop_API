from .. import db
from app.main.models import user_model
from app.main.models import specie_model
from app.main.models import breed_model

class PetModel(db.Model):
    __tablename__ = "pet"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.String(100))
    birthday = db.Column(db.DateTime, nullable=True)
    sex = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    profile_photo_fn = db.Column(db.String(50), default="pet-default-profile-photo.jpg", nullable=False)
    cover_photo_fn = db.Column(db.String(50), default="pet-default-cover-photo.jpg", nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    user_creates_pet_rel = db.Column(db.String, db.ForeignKey("user.username"), nullable=False)
    pet_has_specie_rel = db.Column(db.String, db.ForeignKey("specie.public_id"), nullable=False)
    pet_has_breed_rel = db.Column(db.String, db.ForeignKey("breed.public_id"), nullable=False)
 
    def __repr__(self):
        return "<pet '{}'>".format(self.name)

    def __dto__(self):
        get_specie_row = specie_model.SpecieModel.query.filter_by(public_id=self.pet_has_specie_rel).first()
        get_breed_row = breed_model.BreedModel.query.filter_by(public_id=self.pet_has_breed_rel).first()

        return {
            "id": self.id,
            "public_id": self.public_id,
            "name": self.name,
            "bio": self.bio,
            "birthday": self.birthday,
            "sex": self.sex,
            "status": self.status,
            "profile_photo_fn": self.profile_photo_fn,
            "cover_photo_fn": self.cover_photo_fn,
            "registered_on": self.registered_on,
            "user_owner": self.user_creates_pet_rel,
            "specie_kind": get_specie_row.name,
            "breed_kind": get_breed_row.name
        }