from typing import List
from my_project.auth.dao import owner_details_dao
from my_project.auth.service.general_service import GeneralService


class OwnerDetailsService(GeneralService):
    """
    Realisation of OwnerDetails service.
    """
    _dao = owner_details_dao

    def get_by_owner_id(self, owner_id: int):
        """
        Gets OwnerDetails by owner_id.
        :param owner_id: owner_id value
        :return: OwnerDetails object
        """
        return self._dao.find_by_owner_id(owner_id)
