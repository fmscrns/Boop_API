import uuid, datetime

from app.main import db
from app.main.models.user import User, user_post_rel
from app.main.models.post import Post
from app.main.services.help import Helper

def new_post(data, username):
    new_post_id = str(uuid.uuid4())

    author = User.query.filter_by(username=username).first()

    new_post = Post(
        post_id = new_post_id,
        content = data["content"],
        posted_on = datetime.datetime.utcnow(),
        # posted_by = author.id
    )

    Helper.save_changes(new_post)

    statement_one = user_post_rel.insert().values(user_id=author.public_id, post_id=new_post_id)

    Helper.execute_changes(statement_one)

    return Helper.generate_token("Post", new_post)

def get_all_posts():
    return Post.query.all()

def get_a_post(post_id):
    post = db.session.query(Post.content, Post.posted_on).first()
    print(post)
    post_obj = {}

    post_obj["post_id"] = post[0]
    post_obj["content"] = post[1]
    post_obj["posted_on"] = post[2]

    return post_obj

def delete_post(post_id):
    post = Post.query.filter_by(post_id=post_id).first()

    if post:
        db.session.delete(post)

        db.session.commit()

def update_post(post_id, data):
    post = Post.query.filter_by(post_id=post_id).first()

    post.content = data["content"]

    db.session.commit()

    return Helper.return_resp_obj("success", "Post updated successfully.", None, 200)


def get_user_posts(username):
    user_id = User.query.filter_by(username=username).first().public_id

    posts = db.session.query(Post.post_id, Post.content, Post.posted_on, User.first_name, User.last_name).filter(User.public_id==user_id).filter(user_post_rel.c.user_id==User.public_id).filter(user_post_rel.c.post_id==Post.post_id).all()

    post_list = []

    for x, post in enumerate(posts):
        post_obj = {}
        
        post_obj["post_id"] = post[0]
        post_obj["content"] = post[1]
        post_obj["posted_on"] = post[2]
        
        post_list.append(post_obj)

    return post_list