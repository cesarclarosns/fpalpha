from pydantic import BaseModel, ConfigDict
from typing import List


class BaseValue(BaseModel):
    value: str


class OtherFamily(BaseModel):
    name: str
    relationship: str

    def __hash__(self):  # make hashable BaseModel subclass
        return hash((type(self),) + tuple(self.__dict__.values()))


class Family(BaseModel):
    spouse: List[str]
    children: List[str]
    other_family: List[OtherFamily]
    self: List[str]


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
    model_config = ConfigDict(extra="allow")

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
    model_config = ConfigDict(extra="allow")

    title: BaseValue
    dateOfTrust: str
    grantor: List[str]
    trustee: List[Trustee]
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


class FamilyTrustWill(BaseModel):
    family: Family
    will: List[Will]
    trusts: List[Trust]
