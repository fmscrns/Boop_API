import datetime
from flask_restplus import Namespace, fields

class AuthDto:
    api = Namespace("auth", description="auth operations")
    
    provide_auth_token = api.model("provide auth token", {
        "username_or_email" : fields.String(required=True, description="username or email address"),
        "password" : fields.String(required=True, description="password")
    })

class UserDto:
    api = Namespace("user", description="user operations")

    get_user = api.model("get user", {
        "username" : fields.String(required=True, description="username"),
        "first_name" : fields.String(required=True, description="first name"),
        "last_name" : fields.String(required=True, description="last name"),
        "bio" : fields.String(required=True, description="biography"),
        "profile_photo_fn" : fields.String(required=True, description="profile photo filename"),
        "cover_photo_fn" : fields.String(required=True, description="cover photo filename"),
        "registered_on" : fields.DateTime(required=True, description="registration date")
    })

    create_user = api.model("create user", {
        "username" : fields.String(required=True, description="username"),
        "first_name" : fields.String(required=True, description="first name"),
        "last_name" : fields.String(required=True, description="last name"),
        "email" : fields.String(required=True, description="email address"),
        "profile_photo_fn" : fields.String(required=True, description="profile photo filename"),
        "cover_photo_fn" : fields.String(required=True, description="cover photo filename"),
        "contact_no" : fields.String(required=True, description="contact number")
    })

    get_current_user = api.model("get current user", {
        "username" : fields.String(required=True, description="username"),
        "first_name" : fields.String(required=True, description="first name"),
        "last_name" : fields.String(required=True, description="last name"),
        "bio" : fields.String(required=True, description="biography"),
        "email" : fields.String(required=True, description="email address"),
        "profile_photo_fn" : fields.String(required=True, description="profile photo filename"),
        "cover_photo_fn" : fields.String(required=True, description="cover photo filename"),
        "contact_no" : fields.String(required=True, description="contact number"),
        "registered_on" : fields.DateTime(required=True, description="registration date")
    })

    update_current_user = api.model("update current user", {
        "first_name" : fields.String(required=True, description="first name"),
        "last_name" : fields.String(required=True, description="last name"),
        "bio" : fields.String(required=True, description="biography"),
        "profile_photo_fn" : fields.String(required=True, description="profile photo filename"),
        "cover_photo_fn" : fields.String(required=True, description="cover photo filename"),
        "contact_no" : fields.String(required=True, description="contact number")
    })

class PetDto:
    api = Namespace("pet", description="pet operations")

    get_pet = api.model("get pet", {
        "public_id" : fields.String(required=True, description="public identifier"),
        "name" : fields.String(required=True, description="name"),
        "bio" : fields.String(required=True, description="biography"),
        "birthday" : fields.DateTime(dt_format="rfc822", required=True, description="birthday"),
        "sex" : fields.String(required=True, description="sex"),
        "status" : fields.String(required=True, description="status"),
        "profile_photo_fn" : fields.String(required=True, description="profile photo filename"),
        "cover_photo_fn" : fields.String(required=True, description="cover photo filename"),
        "registered_on" : fields.DateTime(required=True, description="registration date"),
        "owner_user_username" : fields.String(required=True, decription="owner user username"),
        "group_specie_id" : fields.String(required=True, description="group specie identifier"),
        "subgroup_breed_id" : fields.String(required=True, description="subgroup breed identifier")
    })

    create_pet = api.model("create pet", {
        "name" : fields.String(required=True, description="name"),
        "bio" : fields.String(required=True, description="biography"),
        "birthday" : fields.DateTime(dt_format="rfc822", required=True, description="birthday"),
        "sex" : fields.String(required=True, description="sex"),
        "status" : fields.String(required=True, description="status"),
        "profile_photo_fn" : fields.String(required=True, description="profile photo filename"),
        "cover_photo_fn" : fields.String(required=True, description="cover photo filename"),
        "group_specie_id" : fields.String(required=True, description="group specie identifier"),
        "subgroup_breed_id" : fields.String(required=True, description="subgroup breed identifier")
    })

    update_pet = api.model("update pet", {
        "name" : fields.String(required=True, description="name"),
        "bio" : fields.String(required=True, description="biography"),
        "birthday" : fields.DateTime(dt_format="rfc822", required=False, description="birthday"),
        "sex" : fields.String(required=True, description="sex"),
        "status" : fields.String(required=True, description="status"),
        "profile_photo_fn" : fields.String(required=True, description="profile photo filename"),
        "cover_photo_fn" : fields.String(required=True, description="cover photo filename")
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
        "parent_specie_id" : fields.String(required=True, description="parent specie identifier")
    })

    create_breed = api.model("create breed", {
        "name" : fields.String(required=True, description="name"),
        "parent_specie_id" : fields.String(required=True, description="parent specie identifier")
    })

class PostDto:
    api = Namespace("post", description="post operations")

    get_post = api.model("get post", {
        "public_id" : fields.String(require=True, description="public identifier"),
        "content" : fields.String(required=True, description="content"),
        "photo_fn" : fields.String(required=True, description="photo filename"),
        "registered_on" : fields.DateTime(dt_format="rfc822", required=True, description="registration date"),
        "poster_user_username" : fields.String(required=True, decription="poster user username")
    })

    create_post = api.model("create post", {
        "content" : fields.String(required=True, description="content"),
        "photo_fn" : fields.String(required=True, description="photo filename")
    })

class CommentDto:
    api = Namespace("comment", description="comment operations")

    get_comment = api.model("get comment", {
        "public_id" : fields.String(required=True, description="public identifier"),
        "content" : fields.String(required=True, description="content"),
        "registered_on" : fields.DateTime(required=True, description="registration date"),
        "commenter_user_username" : fields.String(required=True, decription="commenter user username"),
        "parent_post_id" : fields.String(required=True, decription="parent post identifier")
    })

    create_comment = api.model("create comment", {
        "content" : fields.String(required=True, description="content"),
        "parent_post_id" : fields.String(required=True, decription="parent post identifier")
    })

class FriendshipDto:
    api = Namespace("Friendship", description="friendship operations")

    get_friendship = api.model("get friendship", {
        "public_id" : fields.String(required=True, description="public identifier"),
        "registered_on" : fields.DateTime(required=False, description="registration date"),
        "is_accepted" : fields.String(required=True, decription="boolean acceptance"),
        "sender_user_username" : fields.String(required=True, description="sender user username"),
        "recipient_user_username" : fields.String(required=True, description="recipient user username")
    })

    create_friendship = api.model("create friendship", {
        "sender_user_username" : fields.String(required=True, description="sender user username"),
        "recipient_user_username" : fields.String(required=True, description="recipient user username")
    })