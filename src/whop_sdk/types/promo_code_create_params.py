# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared.currency import Currency
from .shared.promo_type import PromoType

__all__ = ["PromoCodeCreateParams"]


class PromoCodeCreateParams(TypedDict, total=False):
    amount_off: Required[float]
    """The discount amount.

    When promo_type is percentage, this is the percent off (e.g., 20 for 20% off).
    When promo_type is flat_amount, this is the currency amount off (e.g., 10.00 for
    $10.00 off).
    """

    base_currency: Required[Currency]
    """The three-letter ISO currency code for the promo code discount."""

    code: Required[str]
    """The alphanumeric code customers enter at checkout to apply the discount."""

    company_id: Required[str]
    """The unique identifier of the company to create this promo code for."""

    new_users_only: Required[bool]
    """
    Whether to restrict this promo code to only users who have never purchased from
    the company before.
    """

    promo_duration_months: Required[int]
    """The number of billing months the discount remains active.

    For example, 3 means the discount applies to the first 3 billing cycles.
    """

    promo_type: Required[PromoType]
    """The discount type, either percentage or flat_amount."""

    churned_users_only: Optional[bool]
    """
    Whether to restrict this promo code to only users who have previously churned
    from the company.
    """

    existing_memberships_only: Optional[bool]
    """
    Whether this promo code can only be applied to existing memberships, such as for
    cancellation retention offers.
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The datetime when the promo code expires and can no longer be used.

    Null means it never expires.
    """

    one_per_customer: Optional[bool]
    """Whether each customer can only use this promo code once."""

    plan_ids: Optional[SequenceNotStr[str]]
    """The identifiers of plans this promo code applies to.

    When product_id is also provided, only plans attached to that product are
    included.
    """

    product_id: Optional[str]
    """The identifier of the product to scope this promo code to.

    When provided, the promo code only applies to plans attached to this product.
    """

    stock: Optional[int]
    """The maximum number of times this promo code can be used.

    Ignored when unlimited_stock is true.
    """

    unlimited_stock: Optional[bool]
    """Whether the promo code can be used an unlimited number of times."""
