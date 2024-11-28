from typing import List
from my_project.auth.service import owner_details_service
from my_project.auth.controller.general_controller import GeneralController


class OwnerDetailsController(GeneralController):
    """
    Realisation of OwnerDetails controller.
    """
    _service = owner_details_service

    def get_by_owner_id(self, owner_id: int):
        """
        Gets OwnerDetails by owner_id.
        :param owner_id: owner_id value
        :return: DTO object
        """
        result = self._service.get_by_owner_id(owner_id)
        return result.put_into_dto() if result else None
