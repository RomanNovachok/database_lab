from my_project.auth.service import user_service
from my_project.auth.controller.general_controller import GeneralController

class UserController(GeneralController):
    """
    Realisation of User controller.
    """
    _service = user_service
