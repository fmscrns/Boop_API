import uuid, datetime

from app.main import db
from app.main.models.user import User, user_service_rel
from app.main.models.service import Service
from app.main.services.help import Helper

def create_service(data, public_id):
    new_public_id = str(uuid.uuid4())

    owner = User.query.filter_by(oublic_id=public_id).first()

    new_service = Service(
        public_id = new_public_id,
        service_name = data["serviceName"],
        days = data["days"],
        open_time = data["openTime"],
        close_time = data["endTime"],
        description = data["description"],
        service_owner = owner.public_id
    )

    Helper.save_changes(new_service)

    statement_one = user_service_rel.insert().values(user_id=owner.public_id, service_id=new_public_id)

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
        days = data["days"],
        open_time = data["openTime"],
        close_time = data["endTime"],
        description = data["description"]

        db.session.commit()

        return Helper.return_resp_obj("success", "Services rendered useless", None, 200)

    else:
        return Helper.return_resp_obj("failed", "No service found.", None, 409)

def get_user_service(username):
    user_id = User.query.filter_by(username=username).first.public_id

    services = db.session.query(Service.public_id,
                                Service.days,
                                Service.open_time,
                                Service.close_time,
                                Service.description,
                                User.first_name,
                                User.last_name).filter(
                                    User.public_id==user_id).filter(
                                        user_service_rel.c.user_id==User.public_id).all()
    
    service_list = []

    for service in enumerate(services):
        service_obj = {}

        service_obj["public_id"] = service[0]
        service_obj["days"] = service[1]
        service_obj["open_time"] = service[2]
        service_obj["close_time"] = service[3]
        service_obj["description"] = service[4]
        service_obj["first_name"] = service[5]
        service_obj["last_name"] = service[6]

        service_list.append(service_obj)

    return service_list
