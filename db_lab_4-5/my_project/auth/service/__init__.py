"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.owner_service import OwnerService
owner_service = OwnerService()
from .orders.property_service import PropertyService
property_service = PropertyService()
from .orders.amenity_service import AmenityService
amenity_service = AmenityService()
from .orders.property_amenity_service import PropertyAmenityService
property_amenity_service = PropertyAmenityService()
from .orders.review_service import ReviewService
review_service = ReviewService()
from .orders.owner_details_service import OwnerDetailsService
owner_details_service = OwnerDetailsService()



# from .orders.client_service import ClientService
# from .orders.client_type_service import ClientTypeService
# from .orders.user_service import UsersService
# from .orders.booking_service import BookingService
# from .orders.author_service import AuthorService
# from .orders.book_service import BookService
#
#
# client_service = ClientService()
# client_type_service = ClientTypeService()
# booking_service = BookingService()
# user_service = UsersService()
# author_service = AuthorService()
# book_service = BookService()
