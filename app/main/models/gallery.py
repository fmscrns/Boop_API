from .. import db
from app.main.models import user, pet, post

gal_user_rel = db.Table("gal_user_rel",
    db.Column("gall_id", db.String, db.ForeignKey("gallery.public_id")),
    db.Column("user_id", db.String, db.ForeignKey("user.public_id"))
)

gal_post_rel = db.Table("gal_user_rel",
    db.Column("gall_id", db.String, db.ForeignKey("gallery.public_id")),
    db.Column("post_id", db.String, db.ForeignKey("post.post_id"))
)

gal_pet_rel = db.Table("gal_user_rel",
    db.Column("gall_id", db.String, db.ForeignKey("gallery.public_id")),
    db.Column("pet_id", db.String, db.ForeignKey("pet.public_id"))
)

class Pet(db.Model):
    __tablename__ = "pet"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    gallery_name = db.Column(db.String(100), nullable=True)
    images_filename = db.Column(db.String(50), nullable=True)
    uploaded_on = db.Column(db.DateTime, nullable=False)
    owner_id = db.Column(db.String, db.ForeignKey('user.username'))
    pet_id = db.Column(db.String, db.ForeignKey('pet.username'))
    post_id = db.Column(db.String, db.ForeignKey('user.username'))

    gal_user_rel = db.relationship("User", secondary=gal_user_rel, backref=db.backref("user", lazy=True))
    gal_post_rel = db.relationship("User", secondary=gal_post_rel, backref=db.backref("user", lazy=True))
    gal_pet_rel = db.relationship("User", secondary=gal_pet_rel, backref=db.backref("user", lazy=True))

    def __repr__(self):
        return "<User '{}'>".format(self.username)