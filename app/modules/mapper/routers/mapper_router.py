from flask import Blueprint, request
from app.modules.mapper.libs.map_text_to_family_trust_will import (
    map_text_to_family_trust_will,
)


mapper_router = Blueprint("mapper", __name__, url_prefix="/mapper")


@mapper_router.route(
    "text-to-family-trust-will",
    methods=["POST"],
)
def create_map_text_to_family_trust_will():
    """
    Maps text to FamilyTrustWill.
    """

    text = request.get_data(as_text=True)

    family_trust_will = map_text_to_family_trust_will(text)

    return family_trust_will.model_dump(), 200
