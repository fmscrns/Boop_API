import uuid

from app.main import db
from app.main.models.specie_model import SpecieModel
from app.main.models.breed_model import BreedModel

class BreedService:
    @staticmethod
    def create_breed(post_data):
        try:
            get_specie_row = SpecieModel.query.filter_by(public_id=post_data["specie_id"]).first()

            new_breed = BreedModel(
                public_id = str(uuid.uuid4()),
                name = post_data["name"],
                specie_has_breeds_rel = get_specie_row.public_id
            )

            db.session.add(new_breed)

            db.session.commit()

            return 200

        except Exception:
            return None

    @staticmethod
    def get_specie_breeds(specie_id):
        try:
            return BreedModel.query.filter_by(specie_has_breeds_rel=specie_id).all()

        except Exception:
            return None


    @staticmethod
    def get_breed(breed_id):
        try:
            return BreedModel.query.filter_by(public_id=breed_id).first()

        except Exception:
            return None
