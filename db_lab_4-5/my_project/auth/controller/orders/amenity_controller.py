# controller/amenity_controller.py
from typing import List
from my_project.auth.service import amenity_service
from my_project.auth.controller.general_controller import GeneralController

class AmenityController(GeneralController):
    """
    Realisation of Amenity controller.
    """
    _service = amenity_service

    def get_amenities_by_name(self, name: str) -> List[object]:
        """
        Gets Amenity objects by name using Service layer as DTO objects.
        :param name: Amenity name
        :return: list of matched objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_amenities_by_name(name)))
