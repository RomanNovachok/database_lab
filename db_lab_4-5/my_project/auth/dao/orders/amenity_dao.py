# dao/amenity_dao.py
from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.amenity import Amenity

class AmenityDAO(GeneralDAO):
    """
    Realisation of Amenity data access layer.
    """
    _domain_type = Amenity

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets Amenity objects by amenity_name.
        :param name: Amenity name
        :return: list of matched objects
        """
        return self._session.query(Amenity).filter(Amenity.amenity_name.ilike(f"%{name}%")).all()
