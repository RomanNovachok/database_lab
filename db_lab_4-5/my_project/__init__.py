"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

import secrets
from http import HTTPStatus
from typing import Dict, Any
import os


from flask import Flask
from flask_restx import Api, Resource, Namespace
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

from my_project.auth.route import register_routes

# Database
db = SQLAlchemy()

todos = {}

def load_config():
    return {
        "SECRET_KEY": os.getenv("SECRET_KEY", "default_secret_key"),
        "DEBUG": os.getenv("DEBUG", "False").lower() == "true",
        "SQLALCHEMY_DATABASE_URI": (
            f"mysql+pymysql://{os.getenv('MYSQL_ROOT_USER')}:{os.getenv('MYSQL_ROOT_PASSWORD')}@localhost/your_database_name"
        ),
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }

def create_app(app_config: Dict[str, Any]) -> Flask:
    """
    Creates Flask application
    :param app_config: Flask configuration
    :return: Flask application object
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config.update(app_config)

    _init_db(app)
    register_routes(app)
    _init_swagger(app)

    return app


def _init_swagger(app: Flask) -> None:
    # Swagger / OpenAPI via Flask-RESTX
    restx_api = Api(
        app,
        version="1.0",
        doc="/swagger"  # Swagger UI will be available at /swagger
    )  # https://flask-restx.readthedocs.io/

    # Minimal health namespace
    health_ns = Namespace("health", path="/health", description="Health checks")

    @health_ns.route("")
    class Health(Resource):
        @staticmethod
        def get():
            # Ми змінили це повідомлення для перевірки CI/CD
            return {"status": "ok", "message": "Deployment is working! This is the new version."}, HTTPStatus.OK

    restx_api.add_namespace(health_ns)

    # Import and register RESTX namespaces lazily to avoid circular imports
    from my_project.auth.route.restx_api import register_restx_namespaces
    register_restx_namespaces(restx_api)


def _init_db(app: Flask) -> None:
    """
    Initializes DB with SQLAlchemy
    :param app: Flask application object
    """
    db.init_app(app)

    if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
        create_database(app.config["SQLALCHEMY_DATABASE_URI"])

    import my_project.auth.domain
    with app.app_context():
        db.create_all()
