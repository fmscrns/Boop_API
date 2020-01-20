from .. import db, flask_bcrypt
from app.main.models import business, circle, post, deal, request

user_pet_rel = db.Table("user_pet_rel",
    db.Column("user_username", db.String, db.ForeignKey("user.username", ondelete="cascade")),
    db.Column("pet_id", db.String, db.ForeignKey("pet.public_id", ondelete="cascade"))
)

user_business_rel = db.Table("user_business_rel",
    db.Column("user_username", db.String, db.ForeignKey("user.username", ondelete="cascade")),
    db.Column("business_id", db.String, db.ForeignKey("business.public_id", ondelete="cascade"))
)

user_circle_rel = db.Table("user_circle_rel",
    db.Column("user_username", db.String, db.ForeignKey("user.username", ondelete="cascade")),
    db.Column("circle_id", db.String, db.ForeignKey("circle.public_id", ondelete="cascade"))
)

user_post_rel = db.Table("user_post_rel",
    db.Column("user_username", db.String, db.ForeignKey("user.username", ondelete="cascade")),
    db.Column("public_id", db.String, db.ForeignKey("post.public_id", ondelete="cascade"))
)

user_sale_rel = db.Table("pet_sale_rel",
    db.Column("user_username", db.String, db.ForeignKey("user.username", ondelete="cascade")),
    db.Column("deal_id", db.String, db.ForeignKey("deal.public_id", ondelete="cascade")),
)

user_comment_rel = db.Table("user_comment_rel",
    db.Column("user_username", db.String, db.ForeignKey("user.username", ondelete="cascade")),
    db.Column("comm_id", db.String, db.ForeignKey("comment.public_id", ondelete="cascade"))
)

user_request_rel = db.Table("user_request_rel",
    db.Column("user_id", db.String, db.ForeignKey("user.public_id", ondelete="cascade")),
    db.Column("req_id", db.String, db.ForeignKey("request.public_id", ondelete="cascade"))
)

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    public_id = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True)
    profPhoto_filename = db.Column(db.String(50), nullable=False, default="user-default-profPhoto.jpg")
    coverPhoto_filename = db.Column(db.String(50), nullable=False, default="user-default-coverPhoto.jpg")
    password_hash = db.Column(db.String(100))
    contact_no = db.Column(db.String(20), nullable=True)
    registered_on = db.Column(db.DateTime, nullable=False)

    user_pet_rel = db.relationship("Pet", secondary=user_pet_rel, backref=db.backref("user", lazy=True), cascade="all, delete", passive_deletes=True)
    business_rel = db.relationship("Business", secondary=user_business_rel, backref=db.backref("user", lazy=True))
    circle_rel = db.relationship("Circle", secondary=user_circle_rel, backref=db.backref("user", lazy=True))
    post_rel = db.relationship("Post", secondary=user_post_rel, backref=db.backref("author", lazy=True), cascade="all, delete", passive_deletes=True)
    sale_rel = db.relationship("Deal", secondary=user_sale_rel, backref=db.backref("seller", lazy=True), cascade="all, delete", passive_deletes=True)
    comm_rel = db.relationship("Comment", secondary=user_comment_rel, backref=db.backref("commenter", lazy=True), cascade="all, delete", passive_deletes=True)
    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)
