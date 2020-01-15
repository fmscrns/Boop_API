import uuid, datetime

from app.main import db
from app.main.models.user import User, user_comment_rel
from app.main.models.post import Post
from app.main.models.comment import Comment, comment_post_rel
from app.main.services.help import Helper

def new_comment(data, username, post_id):
    new_public_id = str(uuid.uuid4())

    commenter = User.query.filter_by(username=username).first()
    post = Post.query.filter_by(post_id=post_id).first()

    new_comment = Comment(
        public_id = new_public_id,
        posted_on = datetime.datetime.utcnow(),
        comment = data["comment"],
        posted_by = commenter.username,
        post_id = post.post_id
    )

    Helper.save_changes(new_comment)

    statement_one = user_comment_rel.insert().values(user_id=commenter.public_id, comm_id=new_public_id)

    statement_two = comment_post_rel.insert().values(post_id=post.post_id, comm_id=new_public_id)

    Helper.execute_changes(statement_one)

    Helper.execute_changes(statement_two)

    return Helper.generate_token("Comment", new_comment)

def get_all_comments():
    return Comment.query.all()

def get_a_comment(public_id):
    comment = db.session.query(Comment.public_id, Comment.posted_on, Comment.comment, Comment.posted_by, Comment.post_id).first()
    print(comment)
    comm_obj = {}

    comm_obj["public_id"] = comment[0]
    comm_obj["posted_on"] = comment[1]
    comm_obj["comment"] = comment[2]
    comm_obj["posted_by"] = comment[3]
    comm_obj["post_id"] = comment[4]

    return comm_obj

def delete_comment(public_id):
    comm = Comment.query.filter_by(public_id=public_id).first()

    if comm:
        db.session.delete(comm)

        db.session.commit()
        
        return Helper.return_resp_obj("success", "Comment deleted successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No comment found.", None, 409)

def edit_comment(public_id, data):
    comm = Comment.query.filter_by(public_id=public_id).first()

    if comm:
        comm.comment = data["comment"]
        comm.posted_on = datetime.datetime.utcnow()

        db.session.commit()

        return Helper.return_resp_obj("success", "Comment updated successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No comment found.", None, 409)


def get_post_rel_comment(post_id):
    post = Post.query.filter_by(post_id=post_id).first()

    comments = comment_post_rel.query.filter_by(post_id=post.post_id)

    return comments
