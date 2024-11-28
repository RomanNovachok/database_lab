# route/amenity_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import amenity_controller
from my_project.auth.domain import Amenity

amenity_bp = Blueprint('amenities', __name__, url_prefix='/amenities')

@amenity_bp.get('')
def get_all_amenities() -> Response:
    """
    Gets all Amenity objects using Amenity layer.
    :return: Response object
    """
    return make_response(jsonify(amenity_controller.find_all()), HTTPStatus.OK)

@amenity_bp.post('')
def create_amenity() -> Response:
    """
    Creates a new Amenity object.
    :return: Response object
    """
    content = request.get_json()
    amenity = Amenity.create_from_dto(content)
    amenity_controller.create(amenity)
    return make_response(jsonify(amenity.put_into_dto()), HTTPStatus.CREATED)

@amenity_bp.get('/<int:amenity_id>')
def get_amenity(amenity_id: int) -> Response:
    """
    Gets Amenity object by ID.
    :param amenity_id: Amenity ID
    :return: Response object
    """
    return make_response(jsonify(amenity_controller.find_by_id(amenity_id)), HTTPStatus.OK)

@amenity_bp.put('/<int:amenity_id>')
def update_amenity(amenity_id: int) -> Response:
    """
    Updates Amenity object by ID.
    :param amenity_id: Amenity ID
    :return: Response object
    """
    content = request.get_json()
    amenity = Amenity.create_from_dto(content)
    amenity_controller.update(amenity_id, amenity)
    return make_response("Amenity updated", HTTPStatus.OK)

@amenity_bp.delete('/<int:amenity_id>')
def delete_amenity(amenity_id: int) -> Response:
    """
    Deletes Amenity object by ID.
    :param amenity_id: Amenity ID
    :return: Response object
    """
    amenity_controller.delete(amenity_id)
    return make_response("Amenity deleted", HTTPStatus.OK)

@amenity_bp.get('/search')
def get_amenities_by_name() -> Response:
    """
    Gets Amenity objects by name using query parameter.
    :return: Response object
    """
    name = request.args.get('name', '')
    return make_response(jsonify(amenity_controller.get_amenities_by_name(name)), HTTPStatus.OK)
