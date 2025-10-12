from http import HTTPStatus
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from my_project.auth.controller import user_controller
from my_project.auth.domain.orders.user import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Registers a new user.
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), HTTPStatus.BAD_REQUEST

    if user_controller.find_by_email(email):
        return jsonify({"message": "User with this email already exists"}), HTTPStatus.CONFLICT

    user = User.create_from_dto(data)
    user_controller.create(user)

    return jsonify(user.put_into_dto()), HTTPStatus.CREATED


@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Logs in a user and returns an access token.
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = user_controller.find_by_email(email)

    if user and user.check_password(password):
        # Змінено user.id на user.email для створення токена
        access_token = create_access_token(identity=user.email)
        return jsonify(access_token=access_token), HTTPStatus.OK

    return jsonify({"message": "Invalid credentials"}), HTTPStatus.UNAUTHORIZED

