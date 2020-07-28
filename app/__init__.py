from flask_restplus import Api
from flask import Blueprint

from .main.controller.auth_controller import api as auth_ns
from .main.controller.user_controller import api as user_ns
from .main.controller.pet_controller import api as pet_ns
from .main.controller.specie_controller import api as specie_ns
from .main.controller.breed_controller import api as breed_ns
from .main.controller.post_controller import api as post_ns
from .main.controller.comment_controller import api as comment_ns
from .main.controller.friendship_controller import api as friendship_ns

blueprint = Blueprint("api", __name__)

api = Api(blueprint,
          title = "BOOP API WITH JWT",
          version = "1.0",
          description = "a flask restplus web service for BOOP"
          )

api.add_namespace(auth_ns, path="/auth_ns")
api.add_namespace(user_ns, path="/user_ns")
api.add_namespace(pet_ns, path="/pet_ns")
api.add_namespace(specie_ns, path="/specie_ns")
api.add_namespace(breed_ns, path="/breed_ns")
api.add_namespace(post_ns, path="/post_ns")
api.add_namespace(comment_ns, path="/comment_ns")
api.add_namespace(friendship_ns, path="/friendship_ns")
