# domain/property_amenity.py
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class PropertyAmenity(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "property_amenities"

    property_id = db.Column(db.Integer, db.ForeignKey('properties.property_id', ondelete='CASCADE'), primary_key=True)
    amenity_id = db.Column(db.Integer, db.ForeignKey('amenities.amenity_id', ondelete='CASCADE'), primary_key=True)

    # Relationships (optional if you want to navigate to related entities)
    property = db.relationship("Property", backref="property_amenities")
    amenity = db.relationship("Amenity", backref="property_amenities")

    def __repr__(self) -> str:
        return f"PropertyAmenity(property_id={self.property_id}, amenity_id={self.amenity_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO.
        :return: DTO object as dictionary
        """
        return {
            "property_id": self.property_id,
            "amenity_id": self.amenity_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> "PropertyAmenity":
        """
        Creates domain object from DTO.
        :param dto_dict: DTO object
        :return: Domain object
        """
        return PropertyAmenity(**dto_dict)
