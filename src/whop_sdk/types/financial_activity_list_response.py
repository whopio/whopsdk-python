# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "FinancialActivityListResponse",
    "Data",
    "DataCurrency",
    "DataResource",
    "DataResourceUnionMember0",
    "DataResourceUnionMember1",
    "DataResourceUnionMember2",
    "DataResourceUnionMember2Owner",
    "DataResourceUnionMember2OwnerUnionMember0",
    "DataResourceUnionMember2OwnerUnionMember1",
    "DataResourceUnionMember3",
    "DataResourceUnionMember3Bank",
    "DataResourceUnionMember3Card",
    "DataResourceUnionMember4",
    "DataResourceUnionMember5",
    "DataSource",
    "DataSourcePayoutDestination",
    "PageInfo",
]


class DataCurrency(BaseModel):
    code: str

    precision: str
    """Precision factor for the currency, for example 100000000 for USD."""


class DataResourceUnionMember0(BaseModel):
    id: str

    logo_url: Optional[str] = None

    object: Literal["account"]

    route: Optional[str] = None

    title: Optional[str] = None


class DataResourceUnionMember1(BaseModel):
    id: str

    name: Optional[str] = None

    object: Literal["user"]

    profile_picture_url: Optional[str] = None

    username: Optional[str] = None


class DataResourceUnionMember2OwnerUnionMember0(BaseModel):
    id: str

    logo_url: Optional[str] = None

    object: Literal["account"]

    route: Optional[str] = None

    title: Optional[str] = None


class DataResourceUnionMember2OwnerUnionMember1(BaseModel):
    id: str

    name: Optional[str] = None

    object: Literal["user"]

    profile_picture_url: Optional[str] = None

    username: Optional[str] = None


DataResourceUnionMember2Owner: TypeAlias = Union[
    DataResourceUnionMember2OwnerUnionMember0, DataResourceUnionMember2OwnerUnionMember1, None
]


class DataResourceUnionMember2(BaseModel):
    id: str

    object: Literal["ledger_account"]

    owner: Optional[DataResourceUnionMember2Owner] = None


class DataResourceUnionMember3Bank(BaseModel):
    account_name: Optional[str] = None

    account_type: Optional[str] = None

    bank_name: Optional[str] = None

    last4: Optional[str] = None


class DataResourceUnionMember3Card(BaseModel):
    brand: Optional[str] = None

    exp_month: Optional[int] = None

    exp_year: Optional[int] = None

    last4: Optional[str] = None


class DataResourceUnionMember3(BaseModel):
    id: str

    bank: Optional[DataResourceUnionMember3Bank] = None

    card: Optional[DataResourceUnionMember3Card] = None

    email_identifier: Optional[str] = None

    gateway_type: Optional[str] = None

    object: Literal["payment_method"]

    payment_method_type: Optional[str] = None


class DataResourceUnionMember4(BaseModel):
    id: str

    account_reference: Optional[str] = None

    destination_currency_code: Optional[str] = None

    institution_name: Optional[str] = None

    nickname: Optional[str] = None

    object: Literal["payout_method"]

    provider: Optional[str] = None


class DataResourceUnionMember5(BaseModel):
    id: str

    merchant_category: Optional[str] = None

    merchant_icon_url: Optional[str] = None

    merchant_name: Optional[str] = None

    object: Literal["card_transaction"]

    status: Optional[str] = None

    usd_amount: Optional[str] = None
    """The processor-settled USD amount as a decimal string.

    The ledger's USDT leg is posted 1:1 from this value.
    """


DataResource: TypeAlias = Union[
    DataResourceUnionMember0,
    DataResourceUnionMember1,
    DataResourceUnionMember2,
    DataResourceUnionMember3,
    DataResourceUnionMember4,
    DataResourceUnionMember5,
    None,
]


class DataSourcePayoutDestination(BaseModel):
    """Payout destination display info (withdrawal sources only)."""

    icon_url: Optional[str] = None

    payer_name: Optional[str] = None


class DataSource(BaseModel):
    id: str

    object: str

    chain: Optional[str] = None
    """
    Chain the deposit landed on, for example plasma (onchain_transaction sources
    only).
    """

    created_at: Optional[datetime] = None
    """
    Withdrawal creation time as an ISO 8601 timestamp (withdrawal sources only;
    requires payout:withdrawal:read).
    """

    estimated_arrival: Optional[datetime] = None
    """
    Estimated arrival as an ISO 8601 timestamp (withdrawal sources only; requires
    payout:withdrawal:read).
    """

    from_amount: Optional[str] = None
    """Amount converted out of from_currency as a decimal string (swap sources only)."""

    from_currency: Optional[str] = None
    """Lowercase currency code converted from (swap sources only)."""

    payer_name: Optional[str] = None
    """
    Name of the entity processing the payout (withdrawal sources only; requires
    payout:withdrawal:read).
    """

    payout_destination: Optional[DataSourcePayoutDestination] = None
    """Payout destination display info (withdrawal sources only)."""

    payout_token_nickname: Optional[str] = None
    """Saved payout destination nickname (withdrawal sources only)."""

    sender_address: Optional[str] = None
    """
    Sender wallet address or onramp provider identifier (onchain_transaction sources
    only).
    """

    status: Optional[str] = None
    """
    Withdrawal lifecycle status (withdrawal sources only; requires
    payout:withdrawal:read).
    """

    to_amount: Optional[str] = None
    """Amount received in to_currency as a decimal string (swap sources only)."""

    to_currency: Optional[str] = None
    """Lowercase currency code converted to (swap sources only)."""

    tx_hash: Optional[str] = None
    """On-chain transaction hash (onchain_transaction and swap sources only)."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, builtins.object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> builtins.object: ...
    else:
        __pydantic_extra__: Dict[str, builtins.object]


class Data(BaseModel):
    id: str

    amount: str
    """Signed amount in the currency's smallest precision units."""

    created_at: Optional[datetime] = None

    currency: DataCurrency

    line_type: str

    object: Literal["ledger_activity"]

    posted_at: datetime

    resource: Optional[DataResource] = None

    source: Optional[DataSource] = None


class PageInfo(BaseModel):
    end_cursor: Optional[str] = None

    has_next_page: bool

    has_previous_page: bool

    start_cursor: Optional[str] = None


class FinancialActivityListResponse(BaseModel):
    data: List[Data]

    page_info: PageInfo
