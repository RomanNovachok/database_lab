"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""


# orders DB

from .orders.owner_dao import OwnerDAO
owner_dao = OwnerDAO()
from .orders.property_dao import PropertyDAO
property_dao = PropertyDAO()
from .orders.amenity_dao import AmenityDAO
amenity_dao = AmenityDAO()
from .orders.property_amenity_dao import PropertyAmenityDAO
property_amenity_dao = PropertyAmenityDAO()
from .orders.review_dao import ReviewDAO
review_dao = ReviewDAO()
from .orders.owner_details_dao import OwnerDetailsDAO
owner_details_dao = OwnerDetailsDAO()
from .orders.user_dao import UserDAO
user_dao = UserDAO()


# from .orders.client_dao import ClientDAO
# from .orders.client_type_dao import ClientTypeDAO
# from .orders.user_dao import UsersDAO
# from .orders.booking_dao import BookingDAO
# from .orders.author_dao import AuthorDAO
# from .orders.book_dao import BookDAO
#
# client_dao = ClientDAO()
# client_type_dao = ClientTypeDAO()
# user_dao = UsersDAO()
# booking_dao = BookingDAO()
# author_dao = AuthorDAO()
# book_dao = BookDAO()
