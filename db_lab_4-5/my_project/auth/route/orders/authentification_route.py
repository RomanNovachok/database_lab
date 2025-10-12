from http import HTTPStatus
from flask import Blueprint, request, make_response, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from my_project.auth.service import user_service
from my_project.auth.domain import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.post('/register')
def register_user():
    """
    Registers a new user.
    """
    content = request.get_json()
    email = content.get("email")
    
    if user_service.find_by_email(email):
        return make_response(jsonify({"message": "User with this email already exists"}), HTTPStatus.CONFLICT)

    user = User.create_from_dto(content)
    user_service.create(user)
    
    return make_response(jsonify(user.put_into_dto()), HTTPStatus.CREATED)


@auth_bp.post('/login')
def login_user():
    """
    Logs in a user and returns an access token.
    """
    content = request.get_json()
    email = content.get("email")
    password = content.get("password")

    user = user_service.find_by_email(email)
    
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.user_id)
        return make_response(jsonify(access_token=access_token), HTTPStatus.OK)
    
    return make_response(jsonify({"message": "Invalid credentials"}), HTTPStatus.UNAUTHORIZED)

@auth_bp.get('/profile')
@jwt_required()
def get_profile():
    """
    An example of a protected route that returns user profile.
    """
    current_user_id = get_jwt_identity()
    user = user_service.find_by_id(current_user_id)
    if user:
        return make_response(jsonify(user.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"message": "User not found"}), HTTPStatus.NOT_FOUND)
