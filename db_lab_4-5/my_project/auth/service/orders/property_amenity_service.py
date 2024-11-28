# service/property_amenity_service.py
from typing import List
from my_project.auth.dao import property_amenity_dao
from my_project.auth.service.general_service import GeneralService

class PropertyAmenityService(GeneralService):
    """
    Realisation of PropertyAmenity service.
    """
    _dao = property_amenity_dao

    def get_by_property_id(self, property_id: int) -> List[object]:
        """
        Gets PropertyAmenity objects by property_id.
        :param property_id: Property ID
        :return: list of matched objects
        """
        return self._dao.find_by_property_id(property_id)

    def get_by_amenity_id(self, amenity_id: int) -> List[object]:
        """
        Gets PropertyAmenity objects by amenity_id.
        :param amenity_id: Amenity ID
        :return: list of matched objects
        """
        return self._dao.find_by_amenity_id(amenity_id)

    def add_property_amenity(self, property_address: str, amenity_name: str):
        self._dao.add_property_amenity(property_address, amenity_name)