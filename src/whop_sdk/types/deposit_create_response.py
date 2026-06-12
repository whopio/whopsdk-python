# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DepositCreateResponse", "Methods", "MethodsBank", "MethodsBankCurrency", "MethodsCrypto"]


class MethodsBankCurrency(BaseModel):
    account_number: Optional[str] = None

    currency: str

    deposit_bank_name: Optional[str] = None

    deposit_beneficiary_name: Optional[str] = None

    deposit_reference: Optional[str] = None

    rails: List[str]
    """Active deposit rails for this currency, e.g. ach, wire, sepa."""

    routing_number: Optional[str] = None


class MethodsBank(BaseModel):
    """Bank deposit details.

    Only present when bank deposits are active for the destination account.
    """

    currencies: List[MethodsBankCurrency]


class MethodsCrypto(BaseModel):
    evm: str

    solana: str

    wallet: str


class Methods(BaseModel):
    bank: Optional[MethodsBank] = None
    """Bank deposit details.

    Only present when bank deposits are active for the destination account.
    """

    crypto: MethodsCrypto


class DepositCreateResponse(BaseModel):
    account: Optional[str] = None
    """Account ID of the destination owner. Null for raw wallet address destinations."""

    hosted_url: Optional[str] = None
    """URL of the hosted deposit page. Only present for business destinations."""

    metadata: Dict[str, object]

    methods: Methods

    object: Literal["deposit"]

    amount: Optional[str] = None
