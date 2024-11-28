# controller/property_amenity_controller.py
from typing import List
from my_project.auth.service import property_amenity_service
from my_project.auth.controller.general_controller import GeneralController

class PropertyAmenityController(GeneralController):
    """
    Realisation of PropertyAmenity controller.
    """
    _service = property_amenity_service

    def get_by_property_id(self, property_id: int) -> List[object]:
        """
        Gets PropertyAmenity objects by property_id using Service layer as DTO objects.
        :param property_id: Property ID
        :return: list of matched objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_by_property_id(property_id)))

    def get_by_amenity_id(self, amenity_id: int) -> List[object]:
        """
        Gets PropertyAmenity objects by amenity_id using Service layer as DTO objects.
        :param amenity_id: Amenity ID
        :return: list of matched objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_by_amenity_id(amenity_id)))

    def add_property_amenity(self, property_address: str, amenity_name: str):
        self._service.add_property_amenity(property_address, amenity_name)