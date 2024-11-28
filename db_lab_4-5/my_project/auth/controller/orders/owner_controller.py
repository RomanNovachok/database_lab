# controller/owner_controller.py
from typing import List
from my_project.auth.service import owner_service, property_service
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.dao import owner_dao, property_dao

class OwnerController(GeneralController):
    """
    Realisation of Owner controller.
    """
    _service = owner_service

    @staticmethod
    def get_properties_by_owner(owner_id: int) -> List[dict[str, any]]:
        properties = property_service.find_by_owner_id(owner_id)
        return [property_.to_dict() for property_ in properties]

    def get_owner_by_name(self, name: str) -> List[object]:
        """
        Gets Owner objects by name using Service layer as DTO objects.
        :param name: name value
        :return: list of matched objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_owner_by_name(name)))

    def get_owner_by_email(self, email: str) -> List[object]:
        """
        Gets Owner objects by email using Service layer as DTO objects.
        :param email: email value
        :return: list of matched objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_owner_by_email(email)))

    def insert_10_owners(self) -> None:
        """
        Calls the Service method to execute the stored procedure.
        """
        self._service.insert_10_owners()