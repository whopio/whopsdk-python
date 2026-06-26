# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DepositCreateResponse", "Methods", "MethodsBank", "MethodsBankCurrency", "MethodsCrypto"]


class MethodsBankCurrency(BaseModel):
    account_number: Optional[str] = None
    """Bank account number for deposits in this currency."""

    currency: str
    """Currency supported by these bank instructions."""

    deposit_bank_name: Optional[str] = None
    """Receiving bank name."""

    deposit_beneficiary_name: Optional[str] = None
    """Beneficiary name to use for transfer."""

    deposit_reference: Optional[str] = None
    """Reference to include with bank transfer."""

    rails: List[str]
    """Active deposit rails for this currency, such as `ach`, `wire`, or `sepa`."""

    routing_number: Optional[str] = None
    """Bank routing number for deposits in this currency."""


class MethodsBank(BaseModel):
    """Bank deposit details.

    Only present when bank deposits are active for the destination account.
    """

    currencies: List[MethodsBankCurrency]
    """Bank transfer currencies available for this deposit."""


class MethodsCrypto(BaseModel):
    """Crypto wallet addresses available for this deposit."""

    evm: str
    """EVM-compatible deposit address."""

    solana: str
    """Solana deposit address."""

    wallet: str
    """Primary wallet address for destination account."""


class Methods(BaseModel):
    """Available deposit methods for destination."""

    bank: Optional[MethodsBank] = None
    """Bank deposit details.

    Only present when bank deposits are active for the destination account.
    """

    crypto: MethodsCrypto
    """Crypto wallet addresses available for this deposit."""


class DepositCreateResponse(BaseModel):
    account_id: Optional[str] = None
    """Account ID of the destination owner. Null for raw wallet address destinations."""

    hosted_url: Optional[str] = None
    """URL of the hosted deposit page. Only present for business destinations."""

    metadata: Dict[str, object]
    """Metadata from the request."""

    methods: Methods
    """Available deposit methods for destination."""

    object: Literal["deposit"]

    amount: Optional[str] = None
    """Requested deposit amount."""
