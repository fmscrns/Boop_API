import uuid, datetime
from sqlalchemy.orm import aliased
from app.main import db
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

            if get_specie_row.public_id == get_breed_row.parent_specie_id:
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
                    owner_user_username = get_current_user.username,
                    specie_id = post_data["specie_id"],
                    breed_id = post_data["breed_id"]
                )
                
                db.session.add(new_pet)

                db.session.commit()

                return 200

        except Exception:
            return None

    @staticmethod
    def get_user_pets(username, pagination_no):
        try:
            get_pet_list = PetModel.query.filter_by(owner_user_username=username).paginate(page=pagination_no, per_page=6).items

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

            if get_pet_row.owner_user_username == get_current_user.username:
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

            if get_pet_row.owner_user_username == get_current_user.username:
                db.session.delete(get_pet_row)
                
                db.session.commit()

            return 200

        except Exception:
            return None
