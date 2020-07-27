from app.main import db
from app.main.models.user_model import UserModel
from app.main.models.specie_model import SpecieModel
from app.main.models.breed_model import BreedModel

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
    owner_user_username = db.Column(db.String, db.ForeignKey("user.username"), nullable=False)
    group_specie_id = db.Column(db.String, db.ForeignKey("specie.public_id"), nullable=False)
    subgroup_breed_id = db.Column(db.String, db.ForeignKey("breed.public_id"), nullable=False)
 
    def __repr__(self):
        return "<pet '{}'>".format(self.name)