import uuid, datetime

from app.main import db
from app.main.models.user_model import UserModel
from app.main.models.post_model import PostModel

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
                user_creates_posts_rel = get_current_user.username
            )

            db.session.add(new_post)

            db.session.commit()

            return new_public_id

        except Exception:
            return None

    @staticmethod
    def get_user_posts(username, pagination_no):
        try:
            get_post_list = PostModel.query.filter_by(user_creates_posts_rel=username).paginate(page=pagination_no, per_page=6).items

            return [row.__dto__() for row in get_post_list]

        except Exception:
            return None

    @staticmethod
    def get_post(post_id):
        try:
            return PostModel.query.filter_by(public_id=post_id).first().__dto__()

        except Exception:
            return None

    @staticmethod    
    def delete_post(auth_token, post_id):
        try:
            get_current_user = UserService.get_current_user(auth_token)
            get_post_row = PostModel.query.filter_by(public_id=post_id).first()

            if get_post_row.user_creates_posts_rel == get_current_user.username:
                db.session.delete(get_post_row)

                db.session.commit()

                return 200

        except Exception:
            return None