from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.review import Review
import sqlalchemy


class ReviewDAO(GeneralDAO):
    """
    Realisation of Review data access layer.
    """
    _domain_type = Review

    def find_by_property_id(self, property_id: int) -> List[object]:
        """
        Gets Review objects from database table by field property_id.
        :param property_id: property_id value
        :return: search objects
        """
        return self._session.query(Review).filter(Review.property_id == property_id).order_by(Review.review_date).all()

    # STORED PROCEDURES
    def get_reviews_by_rating(self, min_rating: int) -> List[object]:
        """
        Gets Review objects from database table with rating >= min_rating.
        :param min_rating: rating value
        :return: search objects
        """
        return self._session.execute(sqlalchemy.text("CALL get_reviews_by_rating(:p1)"),
                                     {"p1": min_rating}).mappings().all()

    def get_reviews_by_date_range(self, start_date: str, end_date: str) -> List[object]:
        """
        Gets Review objects from database table within the specified date range.
        :param start_date: start date
        :param end_date: end date
        :return: search objects
        """
        return self._session.execute(sqlalchemy.text("CALL get_reviews_by_date_range(:p1, :p2)"),
                                     {"p1": start_date, "p2": end_date}).mappings().all()

    def insert_review(self, property_id: int, review_text: str, rating: int, review_date: str) -> None:
        """
        Inserts a new review into the database using a stored procedure.
        :param property_id: ID of the property
        :param review_text: The text of the review
        :param rating: The rating of the review
        :param review_date: The date of the review
        """
        self._session.execute(
            sqlalchemy.text("CALL insert_review(:property_id, :review_text, :rating, :review_date)"),
            {"property_id": property_id, "review_text": review_text, "rating": rating, "review_date": review_date}
        )
        self._session.commit()
