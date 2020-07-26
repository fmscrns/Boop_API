import uuid

from app.main import db
from app.main.models.specie_model import SpecieModel

class SpecieService:
    @staticmethod
    def get_all_species():
        try:
            return SpecieModel.query.all()

        except Exception:
            return None

    @staticmethod
    def create_specie(post_data):
        try:
            new_public_id = str(uuid.uuid4())

            new_specie = SpecieModel(
                public_id = new_public_id,
                name = post_data["name"]
            )

            db.session.add(new_specie)

            db.session.commit()

            return new_public_id

        except Exception:
            return None

    @staticmethod
    def get_specie(specie_id):
        try:
            return SpecieModel.query.filter_by(public_id=specie_id).first()

        except Exception:
            return None