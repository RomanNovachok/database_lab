# service/amenity_service.py
from typing import List
from my_project.auth.dao import amenity_dao
from my_project.auth.service.general_service import GeneralService

class AmenityService(GeneralService):
    """
    Realisation of Amenity service.
    """
    _dao = amenity_dao

    def get_amenities_by_name(self, name: str) -> List[object]:
        """
        Gets Amenity objects by name.
        :param name: Amenity name
        :return: list of matched objects
        """
        return self._dao.find_by_name(name)
