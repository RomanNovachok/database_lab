# domain/amenity.py
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Amenity(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "amenities"

    amenity_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amenity_name = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"Amenity({self.amenity_id}, amenity_name='{self.amenity_name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO.
        :return: DTO object as dictionary
        """
        return {
            "amenity_id": self.amenity_id,
            "amenity_name": self.amenity_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> "Amenity":
        """
        Creates domain object from DTO.
        :param dto_dict: DTO object
        :return: Domain object
        """
        return Amenity(**dto_dict)
