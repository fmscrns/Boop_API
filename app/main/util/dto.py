from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'first_name': fields.String(required=True, description='user first name'),
        'last_name': fields.String(required=True, description='user last name'),
        'email': fields.String(required=True, description='user email address'),
        'contact': fields.String(required=True, description='user contact'),
        'address': fields.String(required=True, description='user address'),
        'img': fields.String(required=True, description='user image'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        # 'public_id': fields.String(description='user Identifier')
    })

    parser = api.parser()
    parser.add_argument('first_name', type=str, help='user first name', location='form')
    parser.add_argument('last_name', type=str, help='user last name', location='form')
    parser.add_argument('email', type=str, help='user email', location='form')
    parser.add_argument('contact', type=str, help='user contact', location='form')
    parser.add_argument('address', type=str, help='user address', location='form')
    parser.add_argument('img', type=str, help='user image', location='form')
    parser.add_argument('username', type=str, help='user identifier', location='form')
    parser.add_argument('password', type=str, help='user password', location='form')


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
