import uuid 
import datetime
from flask import request

from app.main.models.user import User, user_sale_rel
from app.main.models.deal import Deal
from app.main.models.transactions import Listing, transaction_rel
from app.main.services.user_service import get_logged_in_user
from app.main.services.help import Helper

def new_transaction(public_id):
    new_public_id = str(uuid.uuid4())

    requester = get_logged_in_user(request)

    req_id = requester[0]["data"]["public_id"]

    deal = Deal.query.filter_by(public_id=public_id).first()

    user = User.query.filter_by(public_id=username).first()

    new_trans(
        public_id = new_public_id,
        posted_on = datetime.datetime.utcnow()
        req_id = req_id
        deal_id = deal.public_id
        owner_id = user.public_id
    )

    statement_one = transaction_rel.insert().values(trans_id=new_public_id, req_id=req_id, deal_id=deal.public_id, owner_id=user.public_id)

    Helper.execute_changes(statement_one)

    return Helper.generate_token("List", new_trans)
