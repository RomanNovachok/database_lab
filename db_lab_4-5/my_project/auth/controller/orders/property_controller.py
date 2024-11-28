from typing import List
from my_project.auth.service import property_service
from my_project.auth.controller.general_controller import GeneralController

class PropertyController(GeneralController):
    """
    Realisation of Property controller.
    """
    _service = property_service

    def get_properties_by_owner_id(self, owner_id: int) -> List[object]:
        """
        Gets Property objects by owner_id using Service layer as DTO objects.
        :param owner_id: Owner ID
        :return: list of matched objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_properties_by_owner_id(owner_id)))

    def get_properties_in_price_range(self, min_price: float, max_price: float) -> List[object]:
        """
        Gets Property objects within a price range using Service layer as DTO objects.
        :param min_price: Minimum price per night
        :param max_price: Maximum price per night
        :return: list of matched objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_properties_in_price_range(min_price, max_price)))

    def get_max_price(self) -> float:
        """
        Calls the Service method to get the maximum price of properties using the stored procedure.
        :return: Maximum price as a float
        """
        return self._service.get_max_price()

    def create_and_insert_properties(self) -> dict:
        """
        Calls the Service method to execute the procedure for creating and populating two properties tables.
        :return: A dictionary indicating success or failure of the operation
        """
        return self._service.create_and_insert_properties()
