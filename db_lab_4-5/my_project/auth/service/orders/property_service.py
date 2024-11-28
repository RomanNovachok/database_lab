# service/property_service.py
from typing import List
from my_project.auth.dao import property_dao
from my_project.auth.service.general_service import GeneralService

class PropertyService(GeneralService):
    """
    Realisation of Property service.
    """
    _dao = property_dao

    def get_properties_by_owner_id(self, owner_id: int) -> List[object]:
        """
        Gets Property objects by owner_id.
        :param owner_id: Owner ID
        :return: list of matched objects
        """
        return self._dao.find_by_owner_id(owner_id)

    def get_properties_in_price_range(self, min_price: float, max_price: float) -> List[object]:
        """
        Gets Property objects within a price range.
        :param min_price: Minimum price per night
        :param max_price: Maximum price per night
        :return: list of matched objects
        """
        return self._dao.find_by_price_range(min_price, max_price)

    def get_max_price(self) -> float:
        """
        Calls the DAO method to fetch the maximum price of properties using the stored procedure.
        :return: Maximum price as a float
        """
        return self._dao.get_max_price_using_procedure()

    def create_and_insert_properties(self) -> dict:
        """
        Executes the stored procedure to create and populate two properties tables.
        :return: A dictionary with status and message
        """
        return self._dao.create_and_insert_into_two_properties_tables()