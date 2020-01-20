import uuid, datetime

from app.main import db
from app.main.models.user import User, user_comment_rel
from app.main.models.post import Post
from app.main.models.comment import Comment, comment_post_rel
from app.main.services.help import Helper

def new_comment(data, username, public_id):
    new_public_id = str(uuid.uuid4())

    post = Post.query.filter_by(public_id=public_id).first()

    new_comment = Comment(
        public_id = new_public_id,
        posted_on = datetime.datetime.utcnow(),
        comment = data["comment"],
        posted_by = username,
        post_id = post.public_id
    )

    Helper.save_changes(new_comment)

    statement_one = user_comment_rel.insert().values(user_username=username, comm_id=new_public_id)

    statement_two = comment_post_rel.insert().values(post_id=post.public_id, comm_id=new_public_id)

    Helper.execute_changes(statement_one)

    Helper.execute_changes(statement_two)

    return Helper.generate_token("Comment", new_comment)

def get_all_comments():
    return Comment.query.all()

def get_a_comment(public_id):
    comment = Comment.query.filter_by(public_id=public_id).first()

    return comment

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


def get_post_rel_comment(public_id):
    comments = Comment.query.filter_by(post_id=public_id).all()
    
    return comments
