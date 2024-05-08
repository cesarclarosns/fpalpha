from pydantic import BaseModel
from typing import List, Optional


class BaseValue(BaseModel):
    value: str


class FamilyRelationship(BaseModel):
    name: str
    relationship: str


class Beneficiary(BaseModel):
    name: str
    value: str
    amount: str
    comment: str


class PrimaryBeneficiary(BaseModel):
    whenWillTransfer: str
    isItFirstDeathOrSecondDeath: str
    beneficiaries: List[Beneficiary]


class Asset(BaseModel):
    assetName: str
    assetType: str
    primaryBeneficiaries: List[PrimaryBeneficiary]


class MaterialInformation(BaseModel):
    value: str
    page: str
    paragraph: str


class Will(BaseModel):
    familyRelationships: List[FamilyRelationship]
    title: BaseValue
    executor: List[str]
    replacement_executor: List[str]
    guardian: List[str]
    state: List[str]
    willOwner: BaseValue
    dateOfWill: BaseValue
    assets: List[Asset]
    materialInformation: List[MaterialInformation]
    isItAPouroverWill: str
    whichPouroverTrust: str
    areThereTestamentaryTrusts: str
    whichTestamentaryTrust: str


class Trustee(BaseModel):
    name: str
    relation: str
    trusteeType: str
    trusteeTrusteeOrCoTrustee: str
    trusteeCanTrusteesActIndividually: str
    trusteeCanAnyCoTrusteeContinueAsSoleTrustee: str
    page: str
    paragraph: str


class Trust(BaseModel):
    familyRelationships: List[FamilyRelationship]
    title: BaseValue
    dateOfTrust: str
    grantor: List[str]
    trustee: List[Trustee]
    successor_trustee: List[Trustee]
    type: str
    state: List[str]
    assets: List[Asset]
    trustees: List[Trustee]
    subtype: str
    jointOrSingle: str
    grantorOrNonGrantorTrust: str
    resultingTrusts: str
    listsAssets: str
    materialInformation: List[MaterialInformation]


class TrustWill(BaseModel):
    will: List[Will]
    trusts: Optional[List[Trust]] = []
