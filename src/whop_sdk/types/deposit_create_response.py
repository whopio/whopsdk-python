# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "DepositCreateResponse",
    "Methods",
    "MethodsBank",
    "MethodsBankCurrency",
    "MethodsCrypto",
    "MethodsCryptoSupportedCurrency",
]


class MethodsBankCurrency(BaseModel):
    account_number: Optional[str] = None
    """Bank account number for deposits in this currency."""

    currency: str
    """Currency supported by these bank instructions."""

    deposit_bank_address: Optional[str] = None
    """Receiving bank address."""

    deposit_bank_name: Optional[str] = None
    """Receiving bank name."""

    deposit_beneficiary_name: Optional[str] = None
    """Beneficiary name to use for transfer."""

    deposit_reference: Optional[str] = None
    """Reference to include with bank transfer."""

    rails: List[Literal["ach", "wire", "sepa", "fps", "chaps"]]
    """Active deposit rails for this currency."""

    routing_number: Optional[str] = None
    """Bank routing number for deposits in this currency."""

    swift_bic: Optional[str] = None
    """SWIFT/BIC code for international wires, when available."""


class MethodsBank(BaseModel):
    """Bank deposit details.

    Only present when bank deposits are active for the destination account.
    """

    currencies: List[MethodsBankCurrency]
    """Bank transfer currencies available for this deposit."""


class MethodsCryptoSupportedCurrency(BaseModel):
    icon_url: Optional[str] = None
    """Token icon URL. Null when no icon is available."""

    name: Literal[
        "ARB",
        "BNB",
        "ETH",
        "EURC",
        "HYPE",
        "PYUSD",
        "SOL",
        "USD1",
        "USDC",
        "USDC.e",
        "USDG",
        "USDT",
        "USDT0",
        "USDe",
        "USDm",
        "XO",
        "XPL",
        "pUSD",
        "wETH",
    ]
    """Token symbol."""


class MethodsCrypto(BaseModel):
    deposit_address: Optional[str] = None
    """Address to send funds to on this network.

    Null when the provider has not issued one yet.
    """

    icon_url: Optional[str] = None
    """Network icon URL."""

    name: Literal[
        "Ethereum",
        "Solana",
        "Base",
        "BNB Smart Chain",
        "Hyperliquid",
        "Hypercore",
        "MegaETH",
        "Polygon",
        "Plasma",
        "Arbitrum",
    ]
    """Network display name."""

    supported_currencies: List[MethodsCryptoSupportedCurrency]
    """Tokens accepted for deposit on this network."""


class Methods(BaseModel):
    """Available deposit methods for destination."""

    bank: Optional[MethodsBank] = None
    """Bank deposit details.

    Only present when bank deposits are active for the destination account.
    """

    crypto: List[MethodsCrypto]
    """
    Crypto networks available for this deposit, each with its on-chain deposit
    address and the tokens accepted on that network.
    """


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
