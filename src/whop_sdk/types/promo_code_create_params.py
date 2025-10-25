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
    """The amount off (% or flat amount) for the promo."""

    base_currency: Required[Currency]
    """The monetary currency of the promo code."""

    code: Required[str]
    """The specific code used to apply the promo at checkout."""

    company_id: Required[str]
    """The id of the company to create the promo code for."""

    new_users_only: Required[bool]
    """
    Restricts promo use to only users who have never purchased from the company
    before.
    """

    promo_duration_months: Required[int]
    """The number of months this promo code is applied and valid for."""

    promo_type: Required[PromoType]
    """The type (% or flat amount) of the promo."""

    churned_users_only: Optional[bool]
    """Restricts promo use to only users who have churned from the company before."""

    existing_memberships_only: Optional[bool]
    """Whether this promo code is for existing memberships only (cancelations)"""

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date/time of when the promo expires."""

    one_per_customer: Optional[bool]
    """Restricts promo use to only be applied once per customer."""

    plan_ids: Optional[SequenceNotStr[str]]
    """The IDs of the plans that the promo code applies to.

    If product_id is provided, it will only apply to plans attached to that product
    """

    product_id: Optional[str]
    """The product to lock the promo code to, if any.

    If provided will filter out any plan ids not attached to this product
    """

    stock: Optional[int]
    """The quantity limit on the number of uses."""

    unlimited_stock: Optional[bool]
    """Whether or not the promo code should have unlimited stock."""
