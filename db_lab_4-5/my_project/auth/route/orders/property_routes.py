# route/property_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import property_controller
from my_project.auth.domain import Property

property_bp = Blueprint('properties', __name__, url_prefix='/properties')

@property_bp.get('')
def get_all_properties() -> Response:
    """
    Gets all Property objects using Property layer.
    :return: Response object
    """
    return make_response(jsonify(property_controller.find_all()), HTTPStatus.OK)

@property_bp.post('')
def create_property() -> Response:
    """
    Creates a new Property object.
    :return: Response object
    """
    content = request.get_json()
    property = Property.create_from_dto(content)
    property_controller.create(property)
    return make_response(jsonify(property.put_into_dto()), HTTPStatus.CREATED)

@property_bp.get('/<int:property_id>')
def get_property(property_id: int) -> Response:
    """
    Gets Property object by ID.
    :param property_id: Property ID
    :return: Response object
    """
    return make_response(jsonify(property_controller.find_by_id(property_id)), HTTPStatus.OK)

@property_bp.put('/<int:property_id>')
def update_property(property_id: int) -> Response:
    """
    Updates Property object by ID.
    :param property_id: Property ID
    :return: Response object
    """
    content = request.get_json()
    property = Property.create_from_dto(content)
    property_controller.update(property_id, property)
    return make_response("Property updated", HTTPStatus.OK)

@property_bp.delete('/<int:property_id>')
def delete_property(property_id: int) -> Response:
    """
    Deletes Property object by ID.
    :param property_id: Property ID
    :return: Response object
    """
    property_controller.delete(property_id)
    return make_response("Property deleted", HTTPStatus.OK)

@property_bp.get('/by-owner/<int:owner_id>')
def get_properties_by_owner_id(owner_id: int) -> Response:
    """
    Gets Property objects by owner_id.
    :param owner_id: Owner ID
    :return: Response object
    """
    return make_response(jsonify(property_controller.get_properties_by_owner_id(owner_id)), HTTPStatus.OK)

@property_bp.get('/price-range')
def get_properties_in_price_range() -> Response:
    """
    Gets Property objects within a specified price range.
    :return: Response object
    """
    min_price = float(request.args.get('min_price', 0))
    max_price = float(request.args.get('max_price', 0))
    return make_response(jsonify(property_controller.get_properties_in_price_range(min_price, max_price)), HTTPStatus.OK)

@property_bp.get('/max_price')
def get_max_price() -> Response:
    """
    Endpoint to fetch the maximum price of properties using the stored procedure.
    :return: Response object with maximum price
    """
    max_price = property_controller.get_max_price()
    return jsonify({"max_price": max_price}), HTTPStatus.OK

@property_bp.post('/create-and-insert-properties')
def create_and_insert_properties() -> Response:
    """
    Endpoint to execute the procedure for creating and populating properties tables.
    :return: JSON response with the result of the operation
    """
    result = property_controller.create_and_insert_properties()
    if result["status"] == "success":
        return jsonify(result), HTTPStatus.CREATED
    else:
        return jsonify(result), HTTPStatus.INTERNAL_SERVER_ERROR