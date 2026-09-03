# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .card_brands import CardBrands
from .shared.direction import Direction
from .payment_method_types import PaymentMethodTypes

__all__ = ["PaymentMethodListParams"]


class PaymentMethodListParams(TypedDict, total=False):
    account_id: str
    """The unique identifier of the company.

    Provide either this or member_id, not both. Omit both to address your own saved
    payment methods.
    """

    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    broken: bool
    """
    Filter by whether the stored credential has permanently stopped charging, such
    as a vault entry its provider closed.
    """

    card_brands: List[CardBrands]
    """Only return cards on these networks, such as the networks the seller accepts.

    Payment methods that are not cards are unaffected.
    """

    card_funding_types: List[Literal["credit", "debit", "prepaid"]]
    """Only return cards funded this way.

    A card whose funding could not be determined is excluded, and payment methods
    that are not cards are unaffected.
    """

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return payment methods created after this timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return payment methods created before this timestamp."""

    direction: Direction
    """The sort direction for ordering results, either ascending or descending."""

    expired: bool
    """Filter by expiry.

    Only a card can expire, so `false` keeps every payment method that is not past
    its expiration month and `true` returns expired cards alone.
    """

    first: int
    """Returns the first _n_ elements from the list."""

    future_usage: Literal["off_session", "on_session"]
    """Only return methods that can be charged this way after the buyer leaves.

    Every stored credential answers either usage today, so this narrows nothing — it
    used to drop the buyer's platform balance, which now lists on its own endpoint
    instead of here.
    """

    has_payer_document: bool
    """
    Filter cards by whether they carry the payer identity document their payment
    provider requires. Payment methods that are not cards are unaffected.
    """

    last: int
    """Returns the last _n_ elements from the list."""

    member_id: str
    """The unique identifier of the member to list payment methods for.

    Omit this and account_id to list your own saved payment methods.
    """

    payment_method_types: List[PaymentMethodTypes]
    """Only return payment methods of these types.

    Pass the eligible `type` values from the payment method types catalogue so the
    list holds nothing the purchase cannot take. An empty list returns no payment
    methods.
    """
