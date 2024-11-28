from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class Review(db.Model, IDto):
    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    property_id = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review_date = db.Column(db.Date, nullable=False)
    renter_id = db.Column(db.Integer, nullable=True)  # Додано nullable=True

    def __repr__(self) -> str:
        return f"Review({self.review_id}, {self.property_id}, '{self.review_text}', {self.rating}, '{self.review_date}', {self.renter_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "review_id": self.review_id,
            "property_id": self.property_id,
            "review_text": self.review_text,
            "rating": self.rating,
            "review_date": self.review_date,
            "renter_id": self.renter_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> "Review":
        return Review(**dto_dict)
