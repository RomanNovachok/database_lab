# route/property_amenity_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import property_amenity_controller
from my_project.auth.domain import PropertyAmenity

property_amenity_bp = Blueprint('property_amenities', __name__, url_prefix='/property-amenities')

@property_amenity_bp.get('')
def get_all_property_amenities() -> Response:
    """
    Gets all PropertyAmenity objects.
    :return: Response object
    """
    return make_response(jsonify(property_amenity_controller.find_all()), HTTPStatus.OK)

@property_amenity_bp.post('')
def create_property_amenity() -> Response:
    """
    Creates a new PropertyAmenity object.
    :return: Response object
    """
    content = request.get_json()
    property_amenity = PropertyAmenity.create_from_dto(content)
    property_amenity_controller.create(property_amenity)
    return make_response(jsonify(property_amenity.put_into_dto()), HTTPStatus.CREATED)

@property_amenity_bp.post('/add')
def add_property_amenity() -> Response:
    """
    Adds a new property-amenity link by calling stored procedure.
    :return: Response object
    """
    data = request.get_json()
    property_address = data.get('property_address')
    amenity_name = data.get('amenity_name')

    if not property_address or not amenity_name:
        return make_response(jsonify({"error": "Property address and amenity name are required"}), HTTPStatus.BAD_REQUEST)

    try:
        property_amenity_controller.add_property_amenity(property_address, amenity_name)
        return make_response(jsonify({"message": "Property amenity link successfully added."}), HTTPStatus.CREATED)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)

@property_amenity_bp.get('/property/<int:property_id>')
def get_by_property_id(property_id: int) -> Response:
    """
    Gets PropertyAmenity objects by property_id.
    :param property_id: Property ID
    :return: Response object
    """
    return make_response(jsonify(property_amenity_controller.get_by_property_id(property_id)), HTTPStatus.OK)

@property_amenity_bp.get('/amenity/<int:amenity_id>')
def get_by_amenity_id(amenity_id: int) -> Response:
    """
    Gets PropertyAmenity objects by amenity_id.
    :param amenity_id: Amenity ID
    :return: Response object
    """
    return make_response(jsonify(property_amenity_controller.get_by_amenity_id(amenity_id)), HTTPStatus.OK)

@property_amenity_bp.delete('/property/<int:property_id>/amenity/<int:amenity_id>')
def delete_property_amenity(property_id: int, amenity_id: int) -> Response:
    """
    Deletes a PropertyAmenity object.
    :param property_id: Property ID
    :param amenity_id: Amenity ID
    :return: Response object
    """
    property_amenity_controller.delete((property_id, amenity_id))
    return make_response("PropertyAmenity deleted", HTTPStatus.OK)
