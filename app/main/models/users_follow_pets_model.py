from app.main import db

class UsersFollowPetsModel(db.Model):
    __tablename__ = "follow"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    following_user_username = db.Column(db.String, db.ForeignKey("follower.username"), nullable=False)
    followed_pet_id = db.Column(db.String, db.ForeignKey("followed.public_id"), nullable=False)

    def __repr__(self):
        return "<Follow '{}' and '{}'>".format(self.following_user_username, self.followed_pet_id)