# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "EarningListResponse",
    "Account",
    "FinancialActivity",
    "Product",
    "Resource",
    "ResourceUnionMember0",
    "ResourceUnionMember0AlternativePaymentMethod",
    "ResourceUnionMember1",
    "ResourceUnionMember2",
]


class Account(BaseModel):
    """Referred account."""

    id: str
    """Referred account ID."""

    logo_url: Optional[str] = None
    """Referred account logo URL."""

    route: str
    """Referred account route."""

    title: str
    """Referred account display name."""


class FinancialActivity(BaseModel):
    amount: str
    """Line amount in its native currency."""

    amount_usd: str
    """Line amount in USD."""

    category: Optional[str] = None
    """Fee or cost category of the line."""

    created_at: Optional[datetime] = None

    currency: str
    """Currency of the native amount."""

    type: Literal["income", "expense"]
    """Whether the line is income Whop collected or a cost Whop paid."""


class Product(BaseModel):
    id: str

    route: str

    title: str


class ResourceUnionMember0AlternativePaymentMethod(BaseModel):
    image_url: Optional[str] = None

    name: str


class ResourceUnionMember0(BaseModel):
    id: str

    alternative_payment_method: Optional[ResourceUnionMember0AlternativePaymentMethod] = None

    brand: Optional[str] = None

    created_at: datetime

    currency: str

    last4: Optional[str] = None

    object: Literal["receipt"]

    payment_method_type: Optional[str] = None

    processor: Optional[str] = None


class ResourceUnionMember1(BaseModel):
    id: str

    created_at: datetime

    currency: str

    object: Literal["transfer"]


class ResourceUnionMember2(BaseModel):
    id: str

    created_at: datetime

    currency: Optional[str] = None

    merchant_name: Optional[str] = None

    object: Literal["card_transaction"]


Resource: TypeAlias = Union[Optional[ResourceUnionMember0], ResourceUnionMember1, ResourceUnionMember2, None]


class EarningListResponse(BaseModel):
    id: Optional[str] = None

    account: Optional[Account] = None
    """Referred account."""

    cancelation_reason: Optional[str] = None
    """Why the earning was canceled or reversed, if applicable."""

    commission_amount_usd: Optional[str] = None
    """What the referrer earns, in USD. Null until the earning settles."""

    created_at: datetime

    financial_activity: Optional[List[FinancialActivity]] = None
    """Income and cost lines behind this earning's commission.

    Null for earnings settled before this data was recorded.
    """

    income_source: Literal["sales", "ad_spend", "transfer", "card_interchange"]
    """
    Which income source the commission is on: product-sales gross profit, Whop Ads
    spend billed to the business, platform balance transfer fees, or Whop Card
    interchange.
    """

    object: Literal["partner_business_earning"]

    payout_at: Optional[datetime] = None

    payout_percentage: Optional[float] = None
    """The referrer's share of Whop's gross profit, as a fraction (0.3 = 30%).

    Null until the earning settles.
    """

    product: Optional[Product] = None

    resource: Optional[Resource] = None
    """
    The resource that generated the earning: the customer payment receipt for sales
    and ad spend earnings, the balance transfer for transfer earnings, or the card
    transaction for card interchange earnings.
    """

    second_tier: bool
    """Whether this earning is a second-tier (grandparent) commission."""

    status: Literal["awaiting_settlement", "pending", "completed", "canceled", "reversed"]
    """Current status of the earning."""

    transaction_amount_usd: str
    """The underlying transaction amount the commission's income comes from, in USD."""
