from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.owner_route import owner_bp
    app.register_blueprint(owner_bp)
    from .orders.property_routes import property_bp
    app.register_blueprint(property_bp)
    from .orders.amenity_route import amenity_bp
    app.register_blueprint(amenity_bp)
    from .orders.property_amenity_route import property_amenity_bp
    app.register_blueprint(property_amenity_bp)
    from .orders.review_route import review_bp
    app.register_blueprint(review_bp)
    from .orders.owner_details_route import owner_details_bp
    app.register_blueprint(owner_details_bp)
    from .orders.authentification_route import auth_bp
    app.register_blueprint(auth_bp)



    # from .orders.user_route import user_bp
    # from .orders.booking_route import booking_bp
    # from .orders.author_route import author_bp
    # from .orders.book_route import book_bp
    #
    # app.register_blueprint(user_bp)
    # app.register_blueprint(booking_bp)
    # app.register_blueprint(author_bp)
    # app.register_blueprint(book_bp)
    #