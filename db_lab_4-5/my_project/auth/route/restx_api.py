from http import HTTPStatus

from flask import request
from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required

from my_project.auth.controller import (
    amenity_controller,
    owner_controller,
    property_controller,
    property_amenity_controller,
    review_controller,
    owner_details_controller,
)
from my_project.auth.domain import (
    Amenity,
    Owner,
    Property,
    PropertyAmenity,
    Review,
    OwnerDetails,
)


def register_restx_namespaces(api) -> None:
    """
    Registers RESTX namespaces that mirror existing Blueprint routes
    so they are visible in Swagger UI.
    """

    # Amenities
    amenities_ns = Namespace("amenities", path="/amenities", description="Amenities")

    @amenities_ns.route("")
    class Amenities(Resource):
        def get(self):
            return amenity_controller.find_all(), HTTPStatus.OK

        def post(self):
            content = request.get_json()
            amenity = Amenity.create_from_dto(content)
            created = amenity_controller.create(amenity)
            return created, HTTPStatus.CREATED

    @amenities_ns.route("/search")
    class AmenitiesSearch(Resource):
        def get(self):
            name = request.args.get("name", "")
            return amenity_controller.get_amenities_by_name(name), HTTPStatus.OK

    @amenities_ns.route("/<int:amenity_id>")
    class AmenityById(Resource):
        def get(self, amenity_id: int):
            return amenity_controller.find_by_id(amenity_id), HTTPStatus.OK

        def put(self, amenity_id: int):
            content = request.get_json()
            amenity = Amenity.create_from_dto(content)
            amenity_controller.update(amenity_id, amenity)
            return {"message": "Amenity updated"}, HTTPStatus.OK

        def delete(self, amenity_id: int):
            amenity_controller.delete(amenity_id)
            return {"message": "Amenity deleted"}, HTTPStatus.OK

    api.add_namespace(amenities_ns)

    # Owners
    owners_ns = Namespace("owners", path="/owners", description="Owners")

    @owners_ns.route("")
    class Owners(Resource):
        @owners_ns.doc(security='jwt')
        @jwt_required()
        def get(self):
            return owner_controller.find_all(), HTTPStatus.OK
        
        @owners_ns.doc(security='jwt')
        @jwt_required()
        def post(self):
            content = request.get_json()
            owner = Owner.create_from_dto(content)
            created = owner_controller.create(owner)
            return created, HTTPStatus.CREATED

    @owners_ns.route("/<int:owner_id>")
    class OwnerById(Resource):
        @owners_ns.doc(security='jwt')
        @jwt_required()
        def get(self, owner_id: int):
            return owner_controller.find_by_id(owner_id), HTTPStatus.OK

        @owners_ns.doc(security='jwt')
        @jwt_required()
        def put(self, owner_id: int):
            content = request.get_json()
            owner = Owner.create_from_dto(content)
            owner_controller.update(owner_id, owner)
            return {"message": "Owner updated"}, HTTPStatus.OK

        @owners_ns.doc(security='jwt')
        @jwt_required()
        def delete(self, owner_id: int):
            owner_controller.delete(owner_id)
            return {"message": "Owner deleted"}, HTTPStatus.OK

    @owners_ns.route("/<int:owner_id>/properties")
    class OwnerProperties(Resource):
        @owners_ns.doc(security='jwt')
        @jwt_required()
        def get(self, owner_id: int):
            properties = owner_controller.get_properties_by_owner(owner_id)
            return [p.to_dict() for p in properties], HTTPStatus.OK

    @owners_ns.route("/insert_10_owners")
    class InsertOwners(Resource):
        @owners_ns.doc(security='jwt')
        @jwt_required()
        def post(self):
            owner_controller.insert_10_owners()
            return {"message": "10 owners inserted successfully"}, HTTPStatus.OK

    api.add_namespace(owners_ns)

    # Properties
    properties_ns = Namespace("properties", path="/properties", description="Properties")
    api.add_namespace(properties_ns)

    # Property Amenities
    prop_amen_ns = Namespace("property-amenities", path="/property-amenities", description="Property amenities")
    api.add_namespace(prop_amen_ns)

    # Reviews
    reviews_ns = Namespace("reviews", path="/reviews", description="Reviews")
    api.add_namespace(reviews_ns)

    # Owner Details
    owner_details_ns = Namespace("owner-details", path="/owner-details", description="Owner details")
    api.add_namespace(owner_details_ns)

