# dao/property_amenity_dao.py
from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.property_amenity import PropertyAmenity
from sqlalchemy.sql import text

class PropertyAmenityDAO(GeneralDAO):
    """
    Realisation of PropertyAmenity data access layer.
    """
    _domain_type = PropertyAmenity

    def find_by_property_id(self, property_id: int) -> List[object]:
        """
        Gets PropertyAmenity objects by property_id.
        :param property_id: Property ID
        :return: list of matched objects
        """
        return self._session.query(PropertyAmenity).filter(PropertyAmenity.property_id == property_id).all()

    def find_by_amenity_id(self, amenity_id: int) -> List[object]:
        """
        Gets PropertyAmenity objects by amenity_id.
        :param amenity_id: Amenity ID
        :return: list of matched objects
        """
        return self._session.query(PropertyAmenity).filter(PropertyAmenity.amenity_id == amenity_id).all()

    def add_property_amenity(self, property_address: str, amenity_name: str):
        """
        Calls stored procedure to add a property amenity.
        :param property_address: Property address
        :param amenity_name: Amenity name
        """
        sql = text("CALL AddPropertyAmenity(:property_address, :amenity_name)")
        self._session.execute(sql, {'property_address': property_address, 'amenity_name': amenity_name})
        self._session.commit()