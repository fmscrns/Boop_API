import uuid, datetime

from app.main import db
from app.main.models.user import User, user_service_rel
from app.main.models.service import Service
from app.main.services.help import Helper

def create_service(data, username):
    new_public_id = str(uuid.uuid4())
    
    print(username)
    user = User.query.filter_by(username=username).first()
    print(user)
    

    new_service = Service(
        public_id = new_public_id,
        service_name = data["serviceName"],
    )

    Helper.save_changes(new_service)

    statement_one = user_service_rel.insert().values(user_username=username, service_id=new_public_id)

    Helper.execute_changes(statement_one)

    return Helper.generate_token("Service", new_service)


def get_all_services():
    return Service.query.all()

def get_a_service(public_id):
    service = Service.query.filter_by(public_id=public_id).first()

    return service

def delete_service(public_id):
    service = Service.query.filter_by(public_id=public_id).first()

    if service:
        db.session.delete(service)

        db.session.commit()

        return Helper.return_resp_obj("success", "Services rendered useless", None, 200)

    else:
        return Helper.return_resp_obj("failed", "No service found.", None, 409)
    
def update_service(data, public_id):
    service = Service.query.filter_by(public_id=public_id).first()

    if service:
        service_name = data["serviceName"],

        db.session.commit()

        return Helper.return_resp_obj("success", "Services rendered useless", None, 200)

    else:
        return Helper.return_resp_obj("failed", "No service found.", None, 409)

def get_user_service(username):
    user = User.query.filter_by(username=username).first()

    services = db.session.query(Service.public_id,
                                Service.service_name,
                                User.first_name,
                                User.last_name).filter(user_service_rel.c.user_username==username).filter(User.username==user_service_rel.c.user_username).filter(Service.public_id==user_service_rel.c.service_id).all()
    
    service_list = []
    for x in services:
        print("HELLO2 {}".format(x))
    for x, service in enumerate(services):
        service_obj = {}

        service_obj["public_id"] = service[0]
        service_obj["service_name"] = service[1]
        service_obj["first_name"] = service[2]
        service_obj["last_name"] = service[3]

        service_list.append(service_obj)
    for s in service_list:
        print("HI {}".format(s))
    return service_list
