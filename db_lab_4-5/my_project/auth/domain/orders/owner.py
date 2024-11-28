# domain/owner.py
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Owner(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "owner"

    owner_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"Owner({self.owner_id}, '{self.name}', '{self.email}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship.
        :return: DTO object as dictionary
        """
        return {
            "owner_id": self.owner_id,
            "name": self.name,
            "email": self.email,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> "Owner":
        """
        Creates domain object from DTO.
        :param dto_dict: DTO object
        :return: Domain object
        """
        return Owner(**dto_dict)
