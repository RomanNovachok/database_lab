# dao/property_dao.py
from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.properties import Property
from sqlalchemy import text

class PropertyDAO(GeneralDAO):
    """
    Realisation of Property data access layer.
    """
    _domain_type = Property

    def find_by_owner_id(self, owner_id: int) -> List[object]:
        """
        Gets Property objects from database table by field owner_id.
        :param owner_id: Owner ID value
        :return: list of matched objects
        """
        return self._session.query(Property).filter(Property.owner_id == owner_id).all()

    def find_by_price_range(self, min_price: float, max_price: float) -> List[object]:
        """
        Gets Property objects within a price range.
        :param min_price: Minimum price per night
        :param max_price: Maximum price per night
        :return: list of matched objects
        """
        return self._session.query(Property).filter(Property.price_per_night.between(min_price, max_price)).all()

    def get_max_price_using_procedure(self) -> float:
        """
        Calls the MySQL stored procedure to get the maximum price of properties.
        :return: Maximum price as a float
        """
        result = self._session.execute(text("CALL get_max_price_procedure()")).fetchone()

        print(result)

        if result:
            # result is a tuple like (Decimal('400.00'),)
            return float(result[0]) if result[0] is not None else 0.0
        return 0.0

    def create_and_insert_into_two_properties_tables(self) -> dict:
        """
        Executes the stored procedure create_and_insert_into_two_properties_tables.
        :return: A dictionary with status and message
        """
        try:
            self._session.execute(text("CALL create_and_insert_into_two_properties_tables()"))
            self._session.commit()
            return {"status": "success", "message": "Data inserted into tables successfully."}
        except Exception as e:
            self._session.rollback()
            return {"status": "error", "message": str(e)}