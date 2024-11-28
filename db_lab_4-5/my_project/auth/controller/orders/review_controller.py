from typing import List

from my_project.auth.service import review_service
from my_project.auth.controller.general_controller import GeneralController

class ReviewController(GeneralController):
    """
    Realisation of Review controller.
    """
    _service = review_service

    def get_reviews_by_rating(self, min_rating: int) -> List[object]:
        """
        Gets Review objects from database table with rating >= min_rating using Service layer as DTO objects.
        :param min_rating: rating value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_reviews_by_rating(min_rating)))

    def get_reviews_by_date_range(self, start_date: str, end_date: str) -> List[object]:
        """
        Gets Review objects from database table within the specified date range using Service layer as DTO objects.
        :param start_date: start date
        :param end_date: end date
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_reviews_by_date_range(start_date, end_date)))

    def insert_review(self, property_id: int, rating: int, review_text: str, review_date: str) -> dict:
        """
        Adds a new review.
        :param property_id: ID of the property
        :param rating: Rating value
        :param review_text: Review text
        :param review_date: Date of the review
        :return: confirmation message
        """
        self._service.add_review(property_id, review_text, rating, review_date)
        return {"message": "Review successfully added."}
