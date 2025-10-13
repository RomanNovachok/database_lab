"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
import os
import secrets
from http import HTTPStatus
from typing import Dict, Any

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restx import Api, Resource, Namespace
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from my_project.auth.route import register_routes

# 1. Створюємо екземпляр SQLAlchemy тут, на верхньому рівні
db = SQLAlchemy()


def create_app(app_config: Dict[str, Any]) -> Flask:
    """
    Creates Flask application
    :param app_config: Flask configuration
    :return: Flask application object
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config.update(app_config)

    # Initialize JWT
    jwt = JWTManager(app)

    _init_db(app)
    register_routes(app)
    _init_swagger(app)

    return app


def _init_swagger(app: Flask) -> None:
    # Authorization scheme for Swagger UI
    authorizations = {
        "jwt": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
        }
    }

    restx_api = Api(
        app,
        version="1.0",
        # title="Real Estate API",
        # description="API for managing real estate properties with JWT authentication.",
        doc="/swagger",
        authorizations=authorizations,
        security="jwt"
    )

    # Minimal health namespace
    health_ns = Namespace("health", path="/health", description="Health checks")

    @health_ns.route("")
    class Health(Resource):
        @staticmethod
        def get():
            # Diagnostic check for the JWT secret key
            secret_key_from_config = app.config.get("JWT_SECRET_KEY")
            is_secret_set = bool(secret_key_from_config)
            
            return {
                "status": "ok",
                "message": "Deployment is working! This is the new version.",
                "jwt_secret_is_set": is_secret_set
            }, HTTPStatus.OK

    restx_api.add_namespace(health_ns)

    # Import and register RESTX namespaces
    from my_project.auth.route.restx_api import register_restx_namespaces
    register_restx_namespaces(restx_api)


def _init_db(app: Flask) -> None:
    """
    Initializes DB with SQLAlchemy
    :param app: Flask application object
    """
    # 2. Ініціалізуємо додаток з нашим об'єктом db
    db.init_app(app)

    with app.app_context():
        if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
            create_database(app.config["SQLALCHEMY_DATABASE_URI"])

        # Import all models here so that SQLAlchemy can see them
        import my_project.auth.domain
        db.create_all()

