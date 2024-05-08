from flask import Flask, Blueprint
from app.modules.mapper.routers import mapper_router
from app.config.app_settings import app_settings
from app.common.libs.error_handlers import handle_validation_error, ValidationError


def bootstrap():
    app = Flask(__name__)

    # Register error handlers
    app.register_error_handler(ValidationError, handle_validation_error)

    # Register routers
    api_router = Blueprint("api", __name__, url_prefix="/api")

    api_router.register_blueprint(mapper_router)

    app.register_blueprint(api_router)

    # Start app
    app.run(debug=app_settings.debug, port=app_settings.port)


if __name__ == "__main__":
    bootstrap()
