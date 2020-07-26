import datetime
from flask_restplus import Namespace, fields

class AuthDto:
    api = Namespace("Authentication", description="auth operations")
    
    provide_auth_token = api.model("provide auth token", {
        "username_or_email_address" : fields.String(required=True, description="user username or email address"),
        "password" : fields.String(required=True, description="user password")
    })

class UserDto:
    api = Namespace("User", description="user operations")

    get_user = api.model("get user", {
        "username" : fields.String(required=True, description="username"),
        "first_name" : fields.String(required=True, description="first name"),
        "last_name" : fields.String(required=True, description="last name"),
        "bio" : fields.String(required=True, description="biography"),
        "profile_photo_fn" : fields.String(required=False, description="profile photo"),
        "cover_photo_fn" : fields.String(required=False, description="cover photo"),
        "contact_no" : fields.String(required=False, description="contact number")
    })

    create_user = api.model("create user", {
        "username" : fields.String(required=True, description="username"),
        "first_name" : fields.String(required=True, description="first name"),
        "last_name" : fields.String(required=True, description="last name"),
        "bio" : fields.String(required=False, description="biography"),
        "email_address" : fields.String(required=True, description="email address"),
        "profile_photo_fn" : fields.String(required=False, description="profile photo"),
        "cover_photo_fn" : fields.String(required=False, description="cover photo"),
        "contact_no" : fields.String(required=False, description="contact number")
    })

    get_current_user = api.model("get current user", {
        "username" : fields.String(required=True, description="username"),
        "first_name" : fields.String(required=True, description="first name"),
        "last_name" : fields.String(required=True, description="last name"),
        "bio" : fields.String(required=True, description="biography"),
        "email_address" : fields.String(required=True, description="email address"),
        "profile_photo_fn" : fields.String(required=False, description="profile photo"),
        "cover_photo_fn" : fields.String(required=False, description="cover photo"),
        "contact_no" : fields.String(required=False, description="contact number")
    })

    update_current_user = api.model("update current user", {
        "first_name" : fields.String(required=False, description="first name"),
        "last_name" : fields.String(required=False, description="last name"),
        "bio" : fields.String(required=False, description="biography"),
        "profile_photo_fn" : fields.String(required=False, description="profile photo"),
        "cover_photo_fn" : fields.String(required=False, description="cover photo"),
        "contact_no" : fields.String(required=False, description="contact number")
    })

class PetDto:
    api = Namespace("Pet", description="pet operations")

    get_pet = api.model("get pet", {
        "public_id" : fields.String(required=True, description="public identifier"),
        "name" : fields.String(required=True, description="name"),
        "bio" : fields.String(required=True, description="biography"),
        "birthday" : fields.DateTime(dt_format="rfc822", required=False, description="birthday"),
        "sex" : fields.String(required=True, description="sex"),
        "status" : fields.String(required=True, description="status"),
        "profile_photo_fn" : fields.String(required=True, description="profile photo"),
        "cover_photo_fn" : fields.String(required=True, description="cover photo"),
        "registered_on" : fields.DateTime(required=False, description="registration date"),
        "user_owner" : fields.String(required=True, decription="user username"),
        "specie_kind" : fields.String(required=True, description="specie name"),
        "breed_kind" : fields.String(required=True, description="breed name")
    })

<<<<<<< HEAD
    breed = api.model("breed", {
        "breed_name": fields.String(required=True, description="breed name"),
        "public_id" : fields.String(require=True, description="breed public id"),
        "specie_id" : fields.String(require=True, description="breed specie id")
=======
    create_pet = api.model("create pet", {
        "name" : fields.String(required=True, description="name"),
        "bio" : fields.String(required=True, description="biography"),
        "birthday" : fields.DateTime(dt_format="rfc822", required=True, description="birthday"),
        "sex" : fields.String(required=True, description="sex"),
        "status" : fields.String(required=True, description="status"),
        "profile_photo_fn" : fields.String(required=True, description="profile photo"),
        "cover_photo_fn" : fields.String(required=True, description="cover photo"),
        "specie_id" : fields.String(required=True, description="specie public identifier"),
        "breed_id" : fields.String(required=True, description="breed public identifier")
>>>>>>> master
    })

    update_pet = api.model("update pet", {
        "name" : fields.String(required=True, description="name"),
        "bio" : fields.String(required=True, description="biography"),
        "birthday" : fields.DateTime(dt_format="rfc822", required=False, description="birthday"),
        "sex" : fields.String(required=True, description="sex"),
        "status" : fields.String(required=True, description="status"),
        "profile_photo_fn" : fields.String(required=True, description="profile photo"),
        "cover_photo_fn" : fields.String(required=True, description="cover photo")
    })

class SpecieDto:
    api = Namespace("specie", description="specie operations")

    get_specie = api.model("get specie", {
        "public_id" : fields.String(required=True, description="public identifier"),
        "name" : fields.String(required=True, description="name")
    })

    create_specie = api.model("create specie", {
        "name" : fields.String(required=True, description="name")
    })

class BreedDto:
    api = Namespace("breed", description="breed operations")

    get_breed = api.model("get breed", {
        "public_id" : fields.String(require=True, description="public identifier"),
        "name": fields.String(required=True, description="name"),
        "specie_id" : fields.String(required=True, description="specie public identifier")
    })

    create_breed = api.model("create breed", {
        "name" : fields.String(required=True, description="name"),
        "specie_id" : fields.String(required=True, description="specie public identifier")
    })

class PostDto:
    api = Namespace("post", description="post operations")

    get_post = api.model("get post", {
        "public_id" : fields.String(require=True, description="public identifier"),
        "content" : fields.String(required=True, description="content"),
        "photo_fn" : fields.String(description="photo"),
        "created_on" : fields.DateTime(dt_format="rfc822", required=True, description="creation date"),
        "user_creator" : fields.String(required=True, decription="user username")
    })

    create_post = api.model("create post", {
        "content" : fields.String(required=True, description="content"),
        "photo_fn" : fields.String(description="photo")
    })

class CommentDto:
    api = Namespace("comment", description="comment operations")

    get_comment = api.model("get comment", {
        "public_id" : fields.String(required=True, description="public identifier"),
        "content" : fields.String(required=True, description="content"),
        "created_on" : fields.DateTime(required=True, description="creation date"),
        "user_id" : fields.String(required=True, decription="user public identifier"),
        "post_id" : fields.String(required=True, decription="post public identifier")
    })

<<<<<<< HEAD
    parser = api.parser

class ServiceDto:
    api = Namespace("services", description="service operations")

    service = api.model("service", {
        "public_id" : fields.String(required=True, decription="service id"),
        "service_name" : fields.String(required=True, description="service type")
    })

    parser = api.parser

class ServiceTypeDto:
    api = Namespace("service types", description="service types operations")

    service_type = api.model("service_type",{
        "public_id" : fields.String(required=True, decription="service id"),
        "service_type" : fields.String(required=True, description="service type description")
    })

    parser = api.parser
=======
    create_comment = api.model("create comment", {
        "content" : fields.String(required=True, description="content"),
        "post_id" : fields.String(required=True, decription="post public identifier")
    })
>>>>>>> master
