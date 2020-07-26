import uuid, datetime
from sqlalchemy.orm import aliased
from app.main import db
<<<<<<< HEAD
from app.main.models.user import User, user_pet_rel
from app.main.models.pet import Pet, pet_kind_rel
from app.main.models.specie import Specie
from app.main.models.breed import Breed
from app.main.services.help import Helper

def save_new_pet(data, username):
    new_public_id = str(uuid.uuid4())
    new_pet = Pet(
        public_id = new_public_id,
        pet_name = data["petName"],
        bio = data["bio"],
        birthday = data["birthday"],
        sex = data["sex"],
        status = data["status"],
        price = data["price"],
        profPhoto_filename = data["profPhotoFilename"],
        coverPhoto_filename = data["coverPhotoFilename"],
        registered_on = datetime.datetime.utcnow(),
        pet_owner = username
    )

    Helper.save_changes(new_pet)

    statement_one = user_pet_rel.insert().values(user_username=username, pet_id=new_public_id)

    statement_two = pet_kind_rel.insert().values(pet_id=new_public_id, specie_id=data["specieId"], breed_id=data["breedId"])

    Helper.execute_changes(statement_one)

    Helper.execute_changes(statement_two)

    return Helper.generate_token("Pet", new_pet)

def get_all_pets():
    return Pet.query.all()

def get_a_pet(public_id):
    pet = db.session.query(Pet.public_id, 
                           Pet.pet_name, 
                           Pet.bio, 
                           Pet.birthday, 
                           Pet.sex, 
                           Pet.status, 
                           Pet.price, 
                           Pet.profPhoto_filename, 
                           Pet.coverPhoto_filename, 
                           Specie.specie_name, 
                           Breed.breed_name, 
                           Pet.pet_owner).filter(Pet.public_id==public_id).filter(pet_kind_rel.c.pet_id==Pet.public_id).filter(Specie.public_id==pet_kind_rel.c.specie_id).filter(Breed.public_id==pet_kind_rel.c.breed_id).first()

    pet_obj = {}

    pet_obj["public_id"] = pet[0]
    pet_obj["pet_name"] = pet[1]
    pet_obj["bio"] = pet[2]
    pet_obj["birthday"] = pet[3]
    pet_obj["sex"] = pet[4]
    pet_obj["status"] = pet[5]
    pet_obj["price"] = pet[6]
    pet_obj["profPhoto_filename"] = pet[7]
    pet_obj["coverPhoto_filename"] = pet[8]
    pet_obj["specie_name"] = pet[9]
    pet_obj["breed_name"] = pet[10]
    pet_obj["pet_owner"] = pet[11]

    return pet_obj

def delete_pet(public_id):
    pet = Pet.query.filter_by(public_id=public_id).first()

    if pet:
        db.session.delete(pet)

        db.session.commit()

        return Helper.return_resp_obj("success", "Pet deleted successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No pet found.", None, 409)

def update_pet(public_id, data):
    pet = Pet.query.filter_by(public_id=public_id).first()
    
    if pet:
        pet.pet_name = data["petName"]
        pet.bio = data["bio"]
        pet.profPic_filename = data["profPhotoFilename"]
        pet.coverPic_filename = data["coverPhotoFilename"]
        pet.sex = data["sex"]
        pet.birthday = data["birthday"]
        pet.status = data["status"]
        pet.price = data["price"]
        pet.pet_owner = data["petOwner"]
        
        db.session.commit()
        
        return Helper.return_resp_obj("success", "Pet updated successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No pet found.", None, 409)

def get_user_pets(username):
    user = User.query.filter_by(username=username).first()

    pets = db.session.query(Pet.public_id, 
                            Pet.pet_name, 
                            Pet.bio, 
                            Pet.birthday, 
                            Pet.sex, 
                            Pet.status,
                            Pet.price,
                            Pet.profPhoto_filename, 
                            Pet.coverPhoto_filename, 
                            Pet.pet_owner, 
                            Specie.specie_name, 
                            Breed.breed_name).filter(
                                User.public_id==user.public_id).filter(
                                    user_pet_rel.c.user_username==username).filter(
                                        user_pet_rel.c.pet_id==Pet.public_id).filter(
                                            pet_kind_rel.c.pet_id==user_pet_rel.c.pet_id).filter(
                                                pet_kind_rel.c.specie_id==Specie.public_id).filter(
                                                    pet_kind_rel.c.breed_id==Breed.public_id).filter(
                                                        Breed.specie_id==Specie.public_id).all()

    pet_list = []

    for x, pet in enumerate(pets):
        pet_obj = {}
        
        pet_obj["public_id"] = pet[0]
        pet_obj["pet_name"] = pet[1]
        pet_obj["bio"] = pet[2]
        pet_obj["birthday"] = pet[3]
        pet_obj["sex"] = pet[4]
        pet_obj["status"] = pet[5]
        pet_obj["price"] = pet[6]
        pet_obj["profPhoto_filename"] = pet[7]
        pet_obj["coverPhoto_filename"] = pet[8]
        pet_obj["pet_owner"] = pet[9]
        pet_obj["specie_name"] = pet[10]
        pet_obj["breed_name"] = pet[11]

        pet_list.append(pet_obj)

    return pet_list

def get_specie_pets(specie_id):
    pets = db.session.query(Pet.pet_name, 
                            Pet.public_id, 
                            Pet.sex, 
                            Pet.pet_owner, 
                            Specie.specie_name, 
                            Breed.breed_name, 
                            Pet.profPhoto_filename,
                            Pet.coverPhoto_filename).filter(Pet.public_id==pet_kind_rel.c.pet_id).filter(pet_kind_rel.c.specie_id==Specie.public_id).filter(pet_kind_rel.c.breed_id==Breed.public_id).filter(pet_kind_rel.c.specie_id==specie_id).all()
    
    pet_list = []
    
    for x, pet in enumerate(pets):
        pet_obj = {}
        
        pet_obj["pet_name"] = pet[0]
        pet_obj["public_id"] = pet[1]
        pet_obj["sex"] = pet[2]
        pet_obj["pet_owner"] = pet[3]
        pet_obj["specie_name"] = pet[4]
        pet_obj["breed_name"] = pet[5]
        pet_obj["profPhoto_filename"] = pet[6]
        pet_obj["coverPhoto_filename"] = pet[7]
        
        pet_list.append(pet_obj)

    return pet_list

def get_breed_pets(breed_id):
    pets = db.session.query(Pet.pet_name, 
                            Pet.public_id, 
                            Pet.sex, 
                            Pet.pet_owner, 
                            Specie.specie_name, 
                            Breed.breed_name, 
                            Pet.profPic_filename).filter(
                                Pet.public_id==pet_kind_rel.c.pet_id).filter(
                                    pet_kind_rel.c.specie_id==Specie.public_id).filter(
                                        pet_kind_rel.c.breed_id==Breed.public_id).filter(
                                            pet_kind_rel.c.breed_id==breed_id).all()
    
    pet_list = []
    
    for x, pet in enumerate(pets):
        pet_obj = {}
        
        pet_obj["pet_name"] = pet[0]
        pet_obj["public_id"] = pet[1]
        pet_obj["sex"] = pet[2]
        pet_obj["pet_owner"] = pet[3]
        pet_obj["specie_name"] = pet[4]
        pet_obj["breed_name"] = pet[5]
        pet_obj["profPhoto_filename"] = pet[6]
        pet_obj["coverPhoto_filename"] = pet[7]

        pet_list.append(pet_obj)

    return pet_list

def pet_transfer(public_id, new_owner_id):
    pet = Pet.query.filter_by(public_id=public_id).first()

    new_owner = User.query.filter_by(public_id=new_owner_id).first()

    if pet:
        pet.pet_owner = new_owner.public_id

        db.session.commit()

        statement_one = user_pet_rel.update().values(user_id=new_owner.public_id, pet_id=pet.public_id)

        Helper.execute_changes(statement_one)

        return Helper.return_resp_obj("success", "Pet succesfully transferred.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No pet found.", None, 404)
=======
from app.main.models.user_model import UserModel
from app.main.models.pet_model import PetModel
from app.main.models.specie_model import SpecieModel
from app.main.models.breed_model import BreedModel

class PetService:
    @staticmethod
    def create_pet(auth_token, post_data):
        try:
            get_current_user = UserService.get_current_user(auth_token)
            get_specie_row = SpecieModel.query.filter_by(public_id=post_data["specie_id"]).first()
            get_breed_row = BreedModel.query.filter_by(public_id=post_data["breed_id"]).first()

            if get_specie_row.public_id == get_breed_row.specie_has_breeds_rel:
                new_pet = PetModel(
                    public_id = str(uuid.uuid4()),
                    name = post_data["name"],
                    bio = post_data["bio"],
                    birthday = post_data["birthday"],
                    sex = post_data["sex"],
                    status = post_data["status"],
                    profile_photo_fn = post_data["profile_photo_fn"],
                    cover_photo_fn = post_data["cover_photo_fn"],
                    registered_on = datetime.datetime.utcnow(),
                    user_creates_pet_rel = get_current_user.username,
                    pet_has_specie_rel = post_data["specie_id"],
                    pet_has_breed_rel = post_data["breed_id"]
                )
                
                db.session.add(new_pet)

                db.session.commit()

                return 200

        except Exception:
            return None

    @staticmethod
    def get_user_pets(username, pagination_no):
        try:
            get_pet_list = PetModel.query.filter_by(user_creates_pet_rel=username).paginate(page=pagination_no, per_page=6).items

            return [row.__dto__() for row in get_pet_list]

        except Exception:
            return None

    @staticmethod
    def get_pet(pet_id):
        try:
            return PetModel.query.filter_by(public_id=pet_id).first()

        except Exception:
            return None

    @staticmethod
    def update_pet(auth_token, pet_id, post_data):
        try:
            get_current_user = UserService.get_current_user(auth_token)
            get_pet_row = PetModel.query.filter_by(public_id=pet_id).first()

            if get_pet_row.user_creates_pet_rel == get_current_user.username:
                get_pet_row.name = post_data["name"]
                get_pet_row.bio = post_data["bio"]
                get_pet_row.birthday = post_data["birthday"]
                get_pet_row.sex = post_data["sex"]
                get_pet_row.status = post_data["status"]
                get_pet_row.profile_photo_fn = post_data["profile_photo_fn"]
                get_pet_row.cover_photo_fn = post_data["cover_photo_fn"]
                
                db.session.commit()

                return 200

        except Exception:
            return None

    @staticmethod
    def delete_pet(auth_token, pet_id):
        try:
            get_current_user = UserService.get_current_user(auth_token)
            get_pet_row = PetModel.query.filter_by(public_id=pet_id).first()

            if get_pet_row.user_creates_pet_rel == get_current_user.username:
                db.session.delete(get_pet_row)
                
                db.session.commit()

            return 200

        except Exception:
            return None
>>>>>>> master
