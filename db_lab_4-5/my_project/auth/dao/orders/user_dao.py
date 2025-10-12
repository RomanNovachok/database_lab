from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.user import User

class UserDAO(GeneralDAO):
    """
    Realisation of User data access layer.
    """
    _domain_type = User

    def find_by_email(self, email: str) -> User or None:
        """
        Gets a User object from the database table by email.
        :param email: user's email
        :return: User object or None if not found
        """
        return self._session.query(User).filter(User.email == email).first()

