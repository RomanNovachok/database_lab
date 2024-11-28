from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class OwnerDetails(db.Model, IDto):
    """
    Model declaration for OwnerDetails.
    """
    __tablename__ = "ownerdetails"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(db.Integer, nullable=False, unique=True)
    details = db.Column(db.Text)

    def repr(self) -> str:
        return f"OwnerDetails({self.id}, {self.owner_id}, '{self.details}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO.
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "details": self.details,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> "OwnerDetails":
        """
        Creates domain object from DTO.
        :param dto_dict: DTO object
        :return: Domain object
        """
        return OwnerDetails(**dto_dict)
