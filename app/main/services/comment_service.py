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

            new_public_id = str(uuid.uuid4())

            new_comment = CommentModel(
                public_id = new_public_id,
                content = post_data["content"],
                created_on = datetime.datetime.utcnow(),
                commenter_user_username = get_current_user.username,
                parent_post_id = get_post_row.public_id
            )

            db.session.add(new_comment)

            db.session.commit()

            return new_public_id

        except Exception:
            return None

    @staticmethod
    def get_post_comments(post_id, pagination_no):
        try:
            return CommentModel.query.filter_by(parent_post_id=post_id).paginate(page=pagination_no, per_page=6).items
        
        except Exception:
            return None

    @staticmethod
    def get_comment(comment_id):
        try:
            return CommentModel.query.filter_by(public_id=comment_id).first()

        except Exception:
            return None

    