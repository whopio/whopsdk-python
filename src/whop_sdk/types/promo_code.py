# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .promo_duration import PromoDuration
from .shared.currency import Currency
from .promo_code_status import PromoCodeStatus
from .shared.promo_type import PromoType

__all__ = ["PromoCode", "Company", "Product"]


class Company(BaseModel):
    """The company for the promo code."""

    id: str
    """The ID of the company"""

    title: str
    """The written name of the company."""


class Product(BaseModel):
    """The product this promo code applies to"""

    id: str
    """The internal ID of the public product."""

    title: str
    """The title of the product. Use for Whop 4.0."""


class PromoCode(BaseModel):
    """An object representing a promo code for a plan."""

    id: str
    """The ID of the promo."""

    amount_off: float
    """The amount off (% or flat amount) for the promo."""

    churned_users_only: bool
    """Restricts promo use to only users who have churned from the company before."""

    code: Optional[str] = None
    """The specific code used to apply the promo at checkout."""

    company: Company
    """The company for the promo code."""

    created_at: datetime
    """The timestamp of when the promo was created."""

    currency: Currency
    """The monetary currency of the promo code."""

    duration: Optional[PromoDuration] = None
    """The duration setting for the promo code"""

    existing_memberships_only: bool
    """Restricts promo use to only be applied to already purchased memberships."""

    expires_at: Optional[datetime] = None
    """The date/time of when the promo expires."""

    new_users_only: bool
    """
    Restricts promo use to only users who have never purchased from the company
    before.
    """

    one_per_customer: bool
    """Restricts promo use to only be applied once per customer."""

    product: Optional[Product] = None
    """The product this promo code applies to"""

    promo_duration_months: Optional[int] = None
    """The number of months the promo is applied for."""

    promo_type: PromoType
    """The type (% or flat amount) of the promo."""

    status: PromoCodeStatus
    """Indicates if the promo code is live or disabled."""

    stock: int
    """The quantity limit on the number of uses."""

    unlimited_stock: bool
    """Whether or not the promo code has unlimited stock."""

    uses: int
    """The amount of times the promo codes has been used."""
