# service/owner_service.py
from typing import List
from my_project.auth.dao import owner_dao
from my_project.auth.service.general_service import GeneralService

class OwnerService(GeneralService):
    """
    Realisation of Owner service.
    """
    _dao = owner_dao

    def get_owner_by_name(self, name: str) -> List[object]:
        """
        Gets Owner objects by name.
        :param name: name value
        :return: list of matched objects
        """
        return self._dao.find_by_name(name)

    def get_owner_by_email(self, email: str) -> List[object]:
        """
        Gets Owner objects by email.
        :param email: email value
        :return: list of matched objects
        """
        return self._dao.find_by_email(email)

    def insert_10_owners(self) -> None:
        """
        Calls the DAO method to execute the stored procedure for inserting 10 owners.
        """
        self._dao.insert_10_owners()