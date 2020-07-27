import uuid, datetime

from app.main import db
from app.main.models.post_model import PostModel
from app.main.models.comment_model import CommentModel
from app.main.services.user_service import UserService

class CommentService:
    @staticmethod
    def create_comment(auth_token, post_data):
        try:
            get_current_user = UserService.get_current_user(auth_token)
            get_post_row = PostModel.query.filter_by(public_id=post_data["post_id"]).first()

            new_comment = CommentModel(
                public_id = str(uuid.uuid4()),
                content = post_data["content"],
                created_on = datetime.datetime.utcnow(),
                creator_user_username = get_current_user.username,
                parent_post_id = get_post_row.public_id
            )

            db.session.add(new_comment)

            db.session.commit()

            return 200

        except Exception:
            return None

    @staticmethod
    def get_post_comments(post_id, pagination_no):
        try:
            get_comment_list = CommentModel.query.filter_by(parent_post_id=post_id).paginate(page=pagination_no, per_page=6).items

            return [row.__dto__() for row in get_comment_list]

        except Exception:
            return None

    @staticmethod
    def get_comment(comment_id):
        try:
            return CommentModel.query.filter_by(public_id=comment_id).first().__dto__()

        except Exception:
            return None

    