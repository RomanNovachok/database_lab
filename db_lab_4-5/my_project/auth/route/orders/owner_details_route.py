from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import owner_details_controller
from my_project.auth.domain import OwnerDetails

owner_details_bp = Blueprint('owner_details', __name__, url_prefix='/owner-details')


@owner_details_bp.get('')
def get_all_owner_details() -> Response:
    """
    Gets all OwnerDetails objects.
    :return: Response object
    """
    return make_response(jsonify(owner_details_controller.find_all()), HTTPStatus.OK)


@owner_details_bp.post('')
def create_owner_details() -> Response:
    """
    Creates new OwnerDetails object.
    :return: Response object
    """
    content = request.get_json()
    owner_details = OwnerDetails.create_from_dto(content)
    owner_details_controller.create(owner_details)
    return make_response(jsonify(owner_details.put_into_dto()), HTTPStatus.CREATED)


@owner_details_bp.get('/<int:owner_id>')
def get_owner_details_by_owner_id(owner_id: int) -> Response:
    """
    Gets OwnerDetails by owner_id.
    :param owner_id: owner_id value
    :return: Response object
    """
    result = owner_details_controller.get_by_owner_id(owner_id)
    return make_response(jsonify(result) if result else "Not Found", HTTPStatus.OK if result else HTTPStatus.NOT_FOUND)


@owner_details_bp.put('/<int:owner_id>')
def update_owner_details(owner_id: int) -> Response:
    """
    Updates OwnerDetails by owner_id.
    :param owner_id: owner_id value
    :return: Response object
    """
    content = request.get_json()
    owner_details = OwnerDetails.create_from_dto(content)
    owner_details_controller.update(owner_id, owner_details)
    return make_response("OwnerDetails updated", HTTPStatus.OK)


@owner_details_bp.delete('/<int:owner_id>')
def delete_owner_details(owner_id: int) -> Response:
    """
    Deletes OwnerDetails by owner_id.
    :param owner_id: owner_id value
    :return: Response object
    """
    owner_details_controller.delete(owner_id)
    return make_response("OwnerDetails deleted", HTTPStatus.OK)
