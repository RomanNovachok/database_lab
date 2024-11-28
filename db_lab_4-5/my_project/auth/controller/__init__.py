"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.owner_controller import OwnerController
owner_controller = OwnerController()
from .orders.property_controller import PropertyController
property_controller = PropertyController()
from .orders.amenity_controller import AmenityController
amenity_controller = AmenityController()
from .orders.property_amenity_controller import PropertyAmenityController
property_amenity_controller = PropertyAmenityController()
from .orders.review_controller import ReviewController
review_controller = ReviewController()
from .orders.owner_details_controller import OwnerDetailsController
owner_details_controller = OwnerDetailsController()




# from .orders.user_controller import UsersController
# from .orders.booking_controller import BookingController
# from .orders.author_controller import AuthorController
# from .orders.book_controller import BookController
# from .orders.client_controller import ClientController
# from .orders.client_type_controller import ClientTypeController
#
# user_controller = UsersController()
# booking_controller = BookingController()
# author_controller = AuthorController()
# client_controller = ClientController()
# client_type_controller = ClientTypeController()
# book_controller = BookController()
