# domain/property.py
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Property(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "properties"

    property_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.owner_id', ondelete='CASCADE'), nullable=False)
    neighborhood_id = db.Column(db.Integer, nullable=True)  # Foreign Key to Neighborhood table, optional
    type_id = db.Column(db.Integer, nullable=True)  # Foreign Key to Property_Type table, optional
    address = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price_per_night = db.Column(db.Numeric(10, 2), nullable=False)

    # Relationship with Owner
    owner = db.relationship("Owner", backref="properties")

    def __repr__(self) -> str:
        return f"Property({self.property_id}, owner_id={self.owner_id}, address='{self.address}', price_per_night={self.price_per_night})"

    def to_dict(self):
        return {
            "property_id": self.property_id,
            "owner_id": self.owner_id,
            "neighborhood_id": self.neighborhood_id,
            "type_id": self.type_id,
            "address": self.address,
            "description": self.description,
            "price_per_night": str(self.price_per_night)
        }

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationships.
        :return: DTO object as dictionary
        """
        return {
            "property_id": self.property_id,
            "owner_id": self.owner_id,
            "neighborhood_id": self.neighborhood_id,
            "type_id": self.type_id,
            "address": self.address,
            "description": self.description,
            "price_per_night": str(self.price_per_night),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> "Property":
        """
        Creates domain object from DTO.
        :param dto_dict: DTO object
        :return: Domain object
        """
        return Property(**dto_dict)
