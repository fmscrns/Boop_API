import uuid

from app.main import db
from app.main.models.breed import Breed
from app.main.models.specie import Specie
from app.main.services.help import Helper

def new_breed(data, public_id):
    new_public_id = str(uuid.uuid4())

    specie = Specie.query.filter_by(public_id=public_id).first()

    new_breed = Breed(
        public_id = new_public_id,
        breed_name = data["breedName"],
        specie_id = specie.public_id
    )

    Helper.save_changes(new_breed)

    return Helper.generate_token("Breed", new_breed)

def get_specie_breeds(specie_id):
    return Breed.query.filter_by(specie_id=specie_id).all()

def get_a_breed(public_id):
    return Breed.query.filter_by(public_id=public_id).first()

def get_all_breeds():
    return Breed.query.all()

def delete_breed(public_id):
    breed = Breed.query.filter_by(public_id=public_id).first()

    if breed:
        db.session.delete(breed)
        db.session.commit()

        return Helper.return_resp_obj("success", "Breed deleted successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No breed found.", None, 409)

def edit_breed(public_id, data):
    breed = Breed.query.filter_by(public_id=public_id).first()

    if breed:
        breed.breed_name = data["breedName"]
        breed.specie_id = data["specieId"]

        db.session.commit()

        return Helper.return_resp_obj("success", "Breed updated successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No breed found.", None, 409)
