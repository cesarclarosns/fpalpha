from app.modules.mapper.models.family_trust_will import (
    FamilyTrustWill,
    Trust,
    Will,
    Family,
    OtherFamily,
)
from app.modules.mapper.models.trust_will import TrustWill
import re


def map_trust_will_to_family_trust_will(trust_will: TrustWill) -> FamilyTrustWill:
    """
    Maps TrustWill to FamilyTrustWill.
    """

    family_trust_will = FamilyTrustWill(
        family=Family(spouse=[], children=[], other_family=[], self=[]),
        trusts=[],
        will=[],
    )

    # Map trusts and family
    for trust in trust_will.trusts:
        # Map trust
        family_trust_will.trusts.append(Trust(**trust.model_dump()))

        # Map family from familyRelationships
        for familyRelationship in trust.familyRelationships:
            if familyRelationship.relationship == "Spouse":
                family_trust_will.family.spouse.append(familyRelationship.name)
            elif familyRelationship.relationship == "Child":
                family_trust_will.family.children.append(familyRelationship.name)
            elif familyRelationship.relationship == "Self":
                family_trust_will.family.self.append(familyRelationship.name)
            else:
                family_trust_will.family.other_family.append(
                    OtherFamily(**familyRelationship.model_dump())
                )

        # Map family from trustees
        for trustee in trust.trustee:
            if trustee.relation == "Spouse":
                family_trust_will.family.spouse.append(trustee.name)
            elif trustee.relation == "Child":
                family_trust_will.family.children.append(trustee.name)
            elif trustee.relation == "Self":
                family_trust_will.family.self.append(trustee.name)
            else:
                family_trust_will.family.other_family.append(
                    OtherFamily(name=trustee.name, relationship=trustee.relation)
                )

        # Map family from trustee
        for trustee in trust.trustees:
            if trustee.relation == "Spouse":
                family_trust_will.family.spouse.append(trustee.name)
            elif trustee.relation == "Child":
                family_trust_will.family.children.append(trustee.name)
            elif trustee.relation == "Self":
                family_trust_will.family.self.append(trustee.name)
            else:
                family_trust_will.family.other_family.append(
                    OtherFamily(name=trustee.name, relationship=trustee.relation)
                )

        # Map family from successor_trustee
        for trustee in trust.successor_trustee:
            if trustee.relation == "Spouse":
                family_trust_will.family.spouse.append(trustee.name)
            elif trustee.relation == "Child":
                family_trust_will.family.children.append(trustee.name)
            elif trustee.relation == "Self":
                family_trust_will.family.self.append(trustee.name)
            else:
                family_trust_will.family.other_family.append(
                    OtherFamily(name=trustee.name, relationship=trustee.relation)
                )

    # Map will and family
    for will in trust_will.will:
        # Map will
        family_trust_will.will.append(Will(**will.model_dump()))

        # Map family from familyRelationships
        for familyRelationship in will.familyRelationships:
            if familyRelationship.relationship == "Spouse":
                family_trust_will.family.spouse.append(familyRelationship.name)
            elif familyRelationship.relationship == "Child":
                family_trust_will.family.children.append(familyRelationship.name)
            elif familyRelationship.relationship == "Self":
                family_trust_will.family.self.append(familyRelationship.name)
            else:
                family_trust_will.family.other_family.append(
                    OtherFamily(**familyRelationship.model_dump())
                )

    # Remove repeated family members
    family_trust_will.family.spouse = list(set(family_trust_will.family.spouse))
    family_trust_will.family.children = list(set(family_trust_will.family.children))
    family_trust_will.family.self = list(set(family_trust_will.family.self))
    family_trust_will.family.other_family = list(
        set(family_trust_will.family.other_family)
    )

    return family_trust_will


def map_text_to_family_trust_will(text: str) -> FamilyTrustWill:
    """
    Maps text to FamilyTrustWill.
    """

    match = re.search(r"(?<=```JSON)(.*?)(?=```)", text, flags=re.DOTALL)
    if match is not None:
        text = match.group(1)

    json_data = text.replace("None", '""')
    trust_will = TrustWill.model_validate_json(json_data)

    return map_trust_will_to_family_trust_will(trust_will)
