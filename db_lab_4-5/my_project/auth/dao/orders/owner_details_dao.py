from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.owner_details import OwnerDetails


class OwnerDetailsDAO(GeneralDAO):
    """
    Realisation of OwnerDetails data access layer.
    """
    _domain_type = OwnerDetails

    def find_by_owner_id(self, owner_id: int) -> OwnerDetails:
        """
        Gets OwnerDetails by owner_id.
        :param owner_id: owner_id value
        :return: OwnerDetails object
        """
        return self._session.query(OwnerDetails).filter(OwnerDetails.owner_id == owner_id).first()

    def find_all(self) -> List[OwnerDetails]:
        """
        Gets all OwnerDetails entries.
        :return: List of OwnerDetails objects
        """
        return self._session.query(OwnerDetails).order_by(OwnerDetails.id).all()
