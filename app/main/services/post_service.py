import uuid, datetime

from app.main import db
<<<<<<< HEAD
from app.main.models.user import User, user_post_rel
from app.main.models.post import Post
from app.main.services.help import Helper

def new_post(data, username):
    new_public_id = str(uuid.uuid4())
    new_post = Post(
        public_id = new_public_id,
        content = data["content"],
        posted_on = datetime.datetime.utcnow(),
        photo = data["photo"],
        post_author = username
    )

    Helper.save_changes(new_post)

    statement_one = user_post_rel.insert().values(user_username=username, public_id=new_public_id)

    Helper.execute_changes(statement_one)
    
    return Helper.generate_token("Post", new_post)

def get_all_posts():
    return Post.query.order_by(Post.posted_on.desc()).all()

def get_a_post(public_id):
    post = db.session.query(Post.public_id, Post.content, Post.photo, Post.posted_on, Post.post_author).filter(Post.public_id==public_id).first()
    
    post_obj = {}

    post_obj["public_id"] = post[0]
    post_obj["content"] = post[1]
    post_obj["photo"] = post[2]
    post_obj["posted_on"] = post[3]
    post_obj["post_author"] = post[4]

    return post_obj

def delete_post(public_id):
    post = Post.query.filter_by(public_id=public_id).first()

    if post:
        db.session.delete(post)

        db.session.commit()
        
        return Helper.return_resp_obj("success", "Post deleted successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No post found.", None, 409)

def get_user_posts(username):
    user_id = User.query.filter_by(username=username).first().public_id

    posts = db.session.query(Post.public_id, Post.content, Post.photo, Post.posted_on, Post.post_author, User.first_name, User.last_name).filter(User.public_id==user_id).filter(user_post_rel.c.user_username==username).filter(user_post_rel.c.public_id==Post.public_id).order_by(Post.posted_on.desc()).all()

    post_list = []

    for x, post in enumerate(posts):
        post_obj = {}
        
        post_obj["public_id"] = post[0]
        post_obj["content"] = post[1]
        post_obj["photo"] = post[2]
        post_obj["posted_on"] = post[3]
        post_obj["post_author"] = post[4]
        
        post_list.append(post_obj)

    return post_list
=======
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
>>>>>>> master
