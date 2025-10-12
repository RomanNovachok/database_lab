from my_project.auth.service import user_service
from my_project.auth.controller.general_controller import GeneralController


class UserController(GeneralController):
    """
    Realisation of UserController.
    """
    _service = user_service

    def find_by_email(self, email: str):
        """
        Gets User by email.
        :param email: email value
        :return: User object
        """
        return self._service.find_by_email(email)

