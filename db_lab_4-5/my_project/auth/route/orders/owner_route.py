# route/owner_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import owner_controller
from my_project.auth.domain import Owner
# from my_project.auth.domain import Owner #rewrite a import to propertise

owner_bp = Blueprint('owners', __name__, url_prefix='/owners')

@owner_bp.get('')
def get_all_owners() -> Response:
    """
    Gets all Owner objects using Owner layer.
    :return: Response object
    """
    return make_response(jsonify(owner_controller.find_all()), HTTPStatus.OK)

@owner_bp.post('')
def create_owner() -> Response:
    """
    Creates a new Owner object.
    :return: Response object
    """
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owner_controller.create(owner)
    return make_response(jsonify(owner.put_into_dto()), HTTPStatus.CREATED)

@owner_bp.get('/<int:owner_id>')
def get_owner(owner_id: int) -> Response:
    """
    Gets Owner object by ID.
    :param owner_id: Owner ID
    :return: Response object
    """
    return make_response(jsonify(owner_controller.find_by_id(owner_id)), HTTPStatus.OK)

@owner_bp.put('/<int:owner_id>')
def update_owner(owner_id: int) -> Response:
    """
    Updates Owner object by ID.
    :param owner_id: Owner ID
    :return: Response object
    """
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owner_controller.update(owner_id, owner)
    return make_response("Owner updated", HTTPStatus.OK)

@owner_bp.delete('/<int:owner_id>')
def delete_owner(owner_id: int) -> Response:
    """
    Deletes Owner object by ID.
    :param owner_id: Owner ID
    :return: Response object
    """
    owner_controller.delete(owner_id)
    return make_response("Owner deleted", HTTPStatus.OK)

# New route to get properties for a specific owner
# route/owner_route.py

@owner_bp.get('/<int:owner_id>/properties')
def get_properties_by_owner(owner_id: int) -> Response:
    """
    Gets all properties for a specific owner.
    :param owner_id: Owner ID
    :return: Response object
    """
    properties = owner_controller.get_properties_by_owner(owner_id)
    # Перетворюємо об'єкти Property у словники
    properties_dict = [property.to_dict() for property in properties]
    return make_response(jsonify(properties_dict), HTTPStatus.OK)

@owner_bp.post('/insert_10_owners')
def insert_10_owners() -> Response:
    """
    Endpoint to execute the stored procedure for inserting 10 owners.
    """
    owner_controller.insert_10_owners()
    return make_response("10 owners inserted successfully", HTTPStatus.OK)
