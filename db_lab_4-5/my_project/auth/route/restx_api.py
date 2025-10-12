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

    # Authentication Namespace (for Swagger UI visibility)
    auth_ns = Namespace("auth", path="/auth", description="Authentication operations")

    @auth_ns.route("/register")
    class UserRegister(Resource):
        def post(self):
            """This endpoint is handled by the auth_bp blueprint. This definition is for Swagger UI documentation."""
            pass

    @auth_ns.route("/login")
    class UserLogin(Resource):
        def post(self):
            """This endpoint is handled by the auth_bp blueprint. This definition is for Swagger UI documentation."""
            pass
            
    @auth_ns.route("/profile")
    class UserProfile(Resource):
        @auth_ns.doc(security='jwt')
        def get(self):
            """This endpoint is handled by the auth_bp blueprint. This definition is for Swagger UI documentation."""
            pass

    api.add_namespace(auth_ns)

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

        def post(self):
            content = request.get_json()
            owner = Owner.create_from_dto(content)
            created = owner_controller.create(owner)
            return created, HTTPStatus.CREATED

    @owners_ns.route("/<int:owner_id>")
    class OwnerById(Resource):
        def get(self, owner_id: int):
            return owner_controller.find_by_id(owner_id), HTTPStatus.OK

        def put(self, owner_id: int):
            content = request.get_json()
            owner = Owner.create_from_dto(content)
            owner_controller.update(owner_id, owner)
            return {"message": "Owner updated"}, HTTPStatus.OK

        def delete(self, owner_id: int):
            owner_controller.delete(owner_id)
            return {"message": "Owner deleted"}, HTTPStatus.OK

    @owners_ns.route("/<int:owner_id>/properties")
    class OwnerProperties(Resource):
        def get(self, owner_id: int):
            properties = owner_controller.get_properties_by_owner(owner_id)
            return [p.to_dict() for p in properties], HTTPStatus.OK

    @owners_ns.route("/insert_10_owners")
    class InsertOwners(Resource):
        def post(self):
            owner_controller.insert_10_owners()
            return {"message": "10 owners inserted successfully"}, HTTPStatus.OK

    api.add_namespace(owners_ns)

    # Properties
    properties_ns = Namespace("properties", path="/properties", description="Properties")

    @properties_ns.route("")
    class Properties(Resource):
        def get(self):
            return property_controller.find_all(), HTTPStatus.OK

        def post(self):
            content = request.get_json()
            prop = Property.create_from_dto(content)
            created = property_controller.create(prop)
            return created, HTTPStatus.CREATED

    @properties_ns.route("/<int:property_id>")
    class PropertyById(Resource):
        def get(self, property_id: int):
            return property_controller.find_by_id(property_id), HTTPStatus.OK

        def put(self, property_id: int):
            content = request.get_json()
            prop = Property.create_from_dto(content)
            property_controller.update(property_id, prop)
            return {"message": "Property updated"}, HTTPStatus.OK

        def delete(self, property_id: int):
            property_controller.delete(property_id)
            return {"message": "Property deleted"}, HTTPStatus.OK

    @properties_ns.route("/by-owner/<int:owner_id>")
    class PropertiesByOwner(Resource):
        def get(self, owner_id: int):
            return property_controller.get_properties_by_owner_id(owner_id), HTTPStatus.OK

    @properties_ns.route("/price-range")
    class PropertiesPriceRange(Resource):
        def get(self):
            min_price = float(request.args.get("min_price", 0))
            max_price = float(request.args.get("max_price", 0))
            return property_controller.get_properties_in_price_range(min_price, max_price), HTTPStatus.OK

    @properties_ns.route("/max_price")
    class PropertiesMaxPrice(Resource):
        def get(self):
            max_price = property_controller.get_max_price()
            return {"max_price": max_price}, HTTPStatus.OK

    @properties_ns.route("/create-and-insert-properties")
    class CreateAndInsertProperties(Resource):
        def post(self):
            result = property_controller.create_and_insert_properties()
            status = HTTPStatus.CREATED if result.get("status") == "success" else HTTPStatus.INTERNAL_SERVER_ERROR
            return result, status

    api.add_namespace(properties_ns)

    # Property Amenities
    prop_amen_ns = Namespace("property-amenities", path="/property-amenities", description="Property amenities")

    @prop_amen_ns.route("")
    class PropertyAmenities(Resource):
        def get(self):
            return property_amenity_controller.find_all(), HTTPStatus.OK

        def post(self):
            content = request.get_json()
            link = PropertyAmenity.create_from_dto(content)
            created = property_amenity_controller.create(link)
            return created, HTTPStatus.CREATED

    @prop_amen_ns.route("/add")
    class PropertyAmenityAdd(Resource):
        def post(self):
            data = request.get_json()
            property_address = data.get("property_address")
            amenity_name = data.get("amenity_name")
            if not property_address or not amenity_name:
                return {"error": "Property address and amenity name are required"}, HTTPStatus.BAD_REQUEST
            property_amenity_controller.add_property_amenity(property_address, amenity_name)
            return {"message": "Property amenity link successfully added."}, HTTPStatus.CREATED

    @prop_amen_ns.route("/property/<int:property_id>")
    class PropertyAmenitiesByProperty(Resource):
        def get(self, property_id: int):
            return property_amenity_controller.get_by_property_id(property_id), HTTPStatus.OK

    @prop_amen_ns.route("/amenity/<int:amenity_id>")
    class PropertyAmenitiesByAmenity(Resource):
        def get(self, amenity_id: int):
            return property_amenity_controller.get_by_amenity_id(amenity_id), HTTPStatus.OK

    @prop_amen_ns.route("/property/<int:property_id>/amenity/<int:amenity_id>")
    class PropertyAmenityDelete(Resource):
        def delete(self, property_id: int, amenity_id: int):
            property_amenity_controller.delete((property_id, amenity_id))
            return {"message": "PropertyAmenity deleted"}, HTTPStatus.OK

    api.add_namespace(prop_amen_ns)

    # Reviews
    reviews_ns = Namespace("reviews", path="/reviews", description="Reviews")

    @reviews_ns.route("")
    class Reviews(Resource):
        def get(self):
            return review_controller.find_all(), HTTPStatus.OK

        def post(self):
            content = request.get_json()
            review = Review.create_from_dto(content)
            created = review_controller.create(review)
            return created, HTTPStatus.CREATED

    @reviews_ns.route("/<int:review_id>")
    class ReviewById(Resource):
        def get(self, review_id: int):
            return review_controller.find_by_id(review_id), HTTPStatus.OK

        def put(self, review_id: int):
            content = request.get_json()
            review = Review.create_from_dto(content)
            review_controller.update(review_id, review)
            return {"message": "Review updated"}, HTTPStatus.OK

        def delete(self, review_id: int):
            review_controller.delete(review_id)
            return {"message": "Review deleted"}, HTTPStatus.OK

    @reviews_ns.route("/get-reviews-by-rating/<int:min_rating>")
    class ReviewsByRating(Resource):
        def get(self, min_rating: int):
            return review_controller.get_reviews_by_rating(min_rating), HTTPStatus.OK

    @reviews_ns.route("/get-reviews-by-date-range")
    class ReviewsByDateRange(Resource):
        def get(self):
            start_date = request.args.get("start_date")
            end_date = request.args.get("end_date")
            return review_controller.get_reviews_by_date_range(start_date, end_date), HTTPStatus.OK

    api.add_namespace(reviews_ns)

    # Owner Details
    owner_details_ns = Namespace("owner-details", path="/owner-details", description="Owner details")

    @owner_details_ns.route("")
    class OwnerDetailsList(Resource):
        def get(self):
            return owner_details_controller.find_all(), HTTPStatus.OK

        def post(self):
            content = request.get_json()
            details = OwnerDetails.create_from_dto(content)
            created = owner_details_controller.create(details)
            return created, HTTPStatus.CREATED

    @owner_details_ns.route("/<int:owner_id>")
    class OwnerDetailsByOwner(Resource):
        def get(self, owner_id: int):
            result = owner_details_controller.get_by_owner_id(owner_id)
            return (result, HTTPStatus.OK) if result else ("Not Found", HTTPStatus.NOT_FOUND)

        def put(self, owner_id: int):
            content = request.get_json()
            details = OwnerDetails.create_from_dto(content)
            owner_details_controller.update(owner_id, details)
            return {"message": "OwnerDetails updated"}, HTTPStatus.OK

        def delete(self, owner_id: int):
            owner_details_controller.delete(owner_id)
            return {"message": "OwnerDetails deleted"}, HTTPStatus.OK

    api.add_namespace(owner_details_ns)

