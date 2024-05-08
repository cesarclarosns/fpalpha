from pydantic import ValidationError


def handle_validation_error(e: ValidationError):
    return e.json(), 422
