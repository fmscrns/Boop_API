import uuid, datetime

from app.main import db
from app.main.models.user import User, user_sale_rel
from app.main.models.pet import Pet
from app.main.models.deal import Deal, pet_price_rel
from app.main.services.help import Helper

def new_deal(data, username, public_id):
    new_public_id = str(uuid.uuid4())

    seller = User.query.filter_by(username=username).first()
    pet = Pet.query.filter_by(public_id=public_id).first()

    new_deal = Deal(
        public_id = new_public_id,
        posted_on = datetime.datetime.utcnow(),
        price = data["price"],
        status = data["status"],
        deal_owner = seller.username
    )

    Helper.save_changes(new_deal)

    statement_one = user_sale_rel.insert().values(user_id=seller.public_id, deal_id=new_public_id)

    statement_two = pet_price_rel.insert().values(pet_id=pet.public_id, deal_id=new_public_id)

    Helper.execute_changes(statement_one)

    Helper.execute_changes(statement_two)

    return Helper.generate_token("Deal", new_deal)

def get_all_deals():
    return Deal.query.all()

def get_a_deal(public_id):
    deal = db.session.query(Deal.public_id, Deal.price, Deal.posted_on, Deal.status, Deal.deal_owner).first()
    print(deal)
    deal_obj = {}

    deal_obj["public_id"] = deal[0]
    deal_obj["price"] = deal[1]
    deal_obj["posted_on"] = deal[2]
    deal_obj["status"] = deal[3]
    deal_obj["deal_owner"] = deal[4]

    return deal_obj

def delete_deal(public_id):
    deal = Deal.query.filter_by(public_id=public_id).first()

    if deal:
        db.session.delete(deal)

        db.session.commit()
        
        return Helper.return_resp_obj("success", "Transaction deleted successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No transaction found.", None, 409)

def update_deal(public_id, data):
    deal = Deal.query.filter_by(public_id=public_id).first()

    if deal:
        deal.price = data["price"]
        deal.status = data["status"]
        deal.posted_on = datetime.datetime.utcnow()

        db.session.commit()

        return Helper.return_resp_obj("success", "Information updated successfully.", None, 200)
    
    else:
        return Helper.return_resp_obj("fail", "No transaction found.", None, 409)


def get_user_deals(username):
    user_id = User.query.filter_by(username=username).first().public_id

    deals = db.session.query(Deal.public_id, Deal.price, Deal.posted_on, Deal.status, Deal.deal_owner, User.username).filter(User.public_id==user_id).filter(user_sale_rel.c.user_id==User.public_id).filter(user_sale_rel.c.public_id==Deal.public_id).all()

    deal_list = []

    for x, deal in enumerate(deals):
        deal_obj = {}
        
        deal_obj["public_id"] = deal[0]
        deal_obj["price"] = deal[1]
        deal_obj["posted_on"] = deal[2]
        deal_obj["status"] = deal[3]
        deal_obj["deal_owner"] = deal[4]
        deal_obj["usernaeme"] = deal[5]
        
        deal_list.append(deal_obj)

    return deal_list



