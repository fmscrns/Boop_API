import uuid, datetime

from app.main import db
from app.main.models.user import User, user_request_rel
from app.main.models.deal import Deal
from app.main.models.request import Request
from app.main.services.help import Helper

def new_request(deal_id, user_id):
    new_public_id = str(uuid.uuid4())

    requester = User.query.filter_by(public_id=user_id).first()

    deal = Deal.query.filter_by(public_id=deal_id).first()

    new_req = Request(
        public_id = new_public_id,
        req_date = datetime.datetime.utcnow(),
        status = "pending",
        deal_id = deal.public_id,
        requester_id = requester.public_id
    )

    Helper.save_changes(new_req)

    statement_one = user_request_rel.insert().values(user_id=requester.public_id, req_id=new_public_id)

    # statement_two = req_deal_rel.insert().values(deal_id=deal.public_id, req_id=new_public_id, requester=requester.username, deal_owner=deal.deal_owner)

    Helper.execute_changes(statement_one)

    # Helper.execute_changes(statement_two)

    Helper.generate_token("Request", new_req)

def get_all_requests():
    return Request.query.all()

def get_a_request(public_id):
    request = db.session.query(Request.public_id,
                               Request.req_date,
                               Request.status,
                               Request.deal_id,
                               Request.requester_id).first()
    req_obj = {}

    req_obj["public_id"] = request[0]
    req_obj["req_date"] = request[1]
    req_obj["status"] = request[2]
    req_obj["deal_id"] = request[3]
    req_obj["requester_id"] = request[4]

    return req_obj

def delete_request(public_id):
    req = Request.query.filter_by(public_id=public_id).first()

    if req:
        db.session.delete(req)

        db.session.commit()

        return Helper.return_resp_obj("success", "Request deleted successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No request found.", None, 409)