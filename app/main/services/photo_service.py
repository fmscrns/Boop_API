import uuid, datetime

from app.main import db
from app.main.models.user import User, user_post_rel
from app.main.models.photo import Photo
from app.main.services.help import Helper

def save_new_photo(data, username):
    new_public_id = str(uuid.uuid4())

    uploader = User.query.filter_by(username=username).first()

    new_photo = Photo(
        public_id = new_public_id,
        filename = data["filename"],
        posted_on = datetime.datetime.utcnow(),
        uploader = uploader.username
    )

    Helper.save_changes(new_photo)

    statement_one = post_photo_rel.insert().values(post_id=data["post_id"], photo_id=new_public_id)

    Helper.execute_changes(statement_one)
    
    return Helper.generate_token("Photo", new_photo)

def insert_post_photo(data):
    statement_one = post_photo_rel.insert().values(post_id=data.get("post_id"), photo_id=data.get("filename"))

    Helper.execute_changes(statement_one)

def get_all_photo():
    return Photo.query.order_by(Photo.posted_on.desc()).all()

def get_a_photo(public_id):
    photo = db.session.query(Photo.public_id, Photo.filename, Photo.posted_on, Photo.uploader).filter(Photo.public_id==public_id).first()
    
    photo_obj = {}

    photo_obj["public_id"] = photo[0]
    photo_obj["filename"] = photo[1]
    photo_obj["posted_on"] = photo[2]
    photo_obj["uploader"] = photo[3]

    return photo_obj

def delete_photo(public_id):
    photo = Photo.query.filter_by(public_id=public_id).first()

    if photo:
        db.session.delete(photo)

        db.session.commit()
        
        return Helper.return_resp_obj("success", "Photo deleted successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No photo found.", None, 409)

def update_photo(public_id, data):
    photo = Photo.query.filter_by(public_id=public_id).first()

    photo.filename = data["filename"]

    db.session.commit()

    return Helper.return_resp_obj("success", "Photo updated successfully.", None, 200)


def get_user_photos(username):
    photos = Photo.query.filter_by(uploader==username).order_by(Photo.posted_on.desc()).all()

    return photos