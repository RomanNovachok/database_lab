from typing import List

from my_project.auth.dao import review_dao
from my_project.auth.service.general_service import GeneralService

class ReviewService(GeneralService):
    """
    Realisation of Review service.
    """
    _dao = review_dao

    def get_reviews_by_rating(self, min_rating: int) -> List[object]:
        """
        Gets Review objects from database table with rating >= min_rating.
        :param min_rating: rating value
        :return: list of all objects
        """
        return self._dao.get_reviews_by_rating(min_rating)

    def get_reviews_by_date_range(self, start_date: str, end_date: str) -> List[object]:
        """
        Gets Review objects from database table within the specified date range.
        :param start_date: start date
        :param end_date: end date
        :return: list of all objects
        """
        return self._dao.get_reviews_by_date_range(start_date, end_date)

    def add_review(self, property_id: int, review_text: str, rating: int, review_date: str) -> None:
        """
        Adds a new review using the DAO layer.
        :param property_id: ID of the property
        :param review_text: Text of the review
        :param rating: Rating of the review
        :param review_date: Date of the review
        """
        self._dao.insert_review(property_id, review_text, rating, review_date)
