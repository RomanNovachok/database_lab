# dao/owner_dao.py
from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.owner import Owner
from sqlalchemy import text


class OwnerDAO(GeneralDAO):
    """
    Realisation of Owner data access layer.
    """
    _domain_type = Owner

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets Owner objects from database table by field name.
        :param name: name value
        :return: list of matched objects
        """
        return self._session.query(Owner).filter(Owner.name == name).order_by(Owner.name).all()

    def find_by_email(self, email: str) -> List[object]:
        """
        Gets Owner objects from database table by field email.
        :param email: email value
        :return: list of matched objects
        """
        return self._session.query(Owner).filter(Owner.email == email).all()

    def insert_10_owners(self) -> None:
        """
        Calls the MySQL procedure to insert 10 owners.
        """
        self._session.execute(text("CALL insert_10_owners()"))
        self._session.commit()