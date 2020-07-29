from app.main import db

#   status types:
#   0 is closed
#   1 is open for adoption
#   2 is missing
#   3 is dead

class PetModel(db.Model):
    __tablename__ = "pet"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.String(100))
    birthday = db.Column(db.DateTime, nullable=True)
    sex = db.Column(db.String(20), nullable=False)
    profile_photo_fn = db.Column(db.String(50), default="pet-default-profile-photo.jpg", nullable=False)
    cover_photo_fn = db.Column(db.String(50), default="pet-default-cover-photo.jpg", nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    owner_user_username = db.Column(db.String, db.ForeignKey("owner.username"), nullable=False)
    group_specie_id = db.Column(db.String, db.ForeignKey("group.public_id"), nullable=False)
    subgroup_breed_id = db.Column(db.String, db.ForeignKey("subgroup.public_id"), nullable=False)
    
    follow_followed_rel = db.relationship("FollowModel", backref="followed", lazy=True)
 
    def __repr__(self):
        return "<pet '{}'>".format(self.name)