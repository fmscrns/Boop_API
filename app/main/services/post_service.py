import uuid, datetime

from app.main import db
from app.main.models.user_model import UserModel
from app.main.models.post_model import PostModel
from app.main.services.user_service import UserService

class PostService:
    @staticmethod
    def create_post(auth_token, post_data):
        try:
            get_current_user = UserService.get_current_user(auth_token)

            new_public_id = str(uuid.uuid4())

            new_post = PostModel(
                public_id = new_public_id,
                content = post_data["content"],
                photo_fn = post_data["photo_fn"],
                created_on = datetime.datetime.utcnow(),
                creator_user_id = get_current_user.username
            )

            db.session.add(new_post)

            db.session.commit()

            return new_public_id

        except Exception:
            return None

    @staticmethod
    def get_user_posts(username, pagination_no):
        try:
            return PostModel.query.filter_by(creator_user_id=username).paginate(page=pagination_no, per_page=6).items

        except Exception:
            return None

    @staticmethod
    def get_post(post_id):
        try:
            return PostModel.query.filter_by(public_id=post_id).first()

        except Exception:
            return None

    @staticmethod    
    def delete_post(auth_token, post_id):
        try:
            get_current_user = UserService.get_current_user(auth_token)
            get_post_row = PostModel.query.filter_by(public_id=post_id).first()

            if get_post_row.poster_user_username == get_current_user.username:
                db.session.delete(get_post_row)

                db.session.commit()

                return 200

        except Exception:
            return None
