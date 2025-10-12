from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.user import User


class UserDAO(GeneralDAO):
    """
    Realisation of User data access layer.
    """
    _domain_type = User

    def find_by_email(self, email: str) -> User:
        """
        Gets User object from database table by email.
        :param email: email value
        :return: User object
        """
        return self._session.query(User).filter_by(email=email).first()

