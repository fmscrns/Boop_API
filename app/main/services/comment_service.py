import uuid, datetime

from app.main import db
from app.main.models.post_model import PostModel
from app.main.models.comment_model import CommentModel

class CommentService:
    @staticmethod
    def create_comment(auth_token, post_data):
        try:
            get_current_user = UserService.get_current_user(auth_token)
            get_post_row = PostModel.query_filter_by(public_id=post_data["post_id"]).first()

            new_comment = CommentModel(
                public_id = str(uuid.uuid4()),
                content = data["content"],
                created_on = datetime.datetime.utcnow(),
                user_creates_comments_rel = get_current_user.username,
                post_has_comments_rel = get_post_row.public_id
            )

            db.session.add(new_comment)

            db.session.commit()

            return 200

        except Exception:
            return None

    @staticmethod
    def get_post_comments(post_id, pagination_no):
        try:
            return CommentModel.query.filter_by(post_id=post_id).paginate(page=pagination_no, per_page=6)

        except Exception:
            return None

    @staticmethod
    def get_comment(comment_id):
        try:
            return CommentModel.query.filter_by(public_id=comment_id).first()

        except Exception:
            return None

    