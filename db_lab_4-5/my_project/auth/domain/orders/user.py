from werkzeug.security import generate_password_hash, check_password_hash
from my_project import db
from my_project.auth.domain.i_dto import IDto


class User(db.Model, IDto):
    """
    Model declaration for User.
    """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def put_into_dto(self):
        return {
            "id": self.id,
            "email": self.email,
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = User(
            email=dto_dict.get("email")
        )
        obj.set_password(dto_dict.get("password"))
        return obj

