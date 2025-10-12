from typing import Dict, Any
from werkzeug.security import generate_password_hash, check_password_hash
from my_project import db
from my_project.auth.domain.i_dto import IDto
import datetime

class User(db.Model, IDto):
    """
    Model declaration for Users.
    """
    __tablename__ = "Users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    user_type = db.Column(db.Enum('renter', 'owner'), nullable=False, default='renter')
    account_balance = db.Column(db.Numeric(10, 2), default=0.00)
    registration_date = db.Column(db.Date, nullable=False, default=datetime.date.today)

    def set_password(self, password_to_hash: str):
        """Hashes and sets the user's password."""
        self.password = generate_password_hash(password_to_hash)

    def check_password(self, password_to_check: str) -> bool:
        """Checks if the provided password matches the hashed one."""
        return check_password_hash(self.password, password_to_check)

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO, excluding password.
        """
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "user_type": self.user_type,
            "account_balance": str(self.account_balance),
            "registration_date": self.registration_date.isoformat()
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> "User":
        """
        Creates a User domain object from a DTO.
        """
        user = User(
            name=dto_dict.get("name"),
            email=dto_dict.get("email"),
            user_type=dto_dict.get("user_type", "renter")
        )
        if dto_dict.get("password"):
            user.set_password(dto_dict["password"])
        return user
