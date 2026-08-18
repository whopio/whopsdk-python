# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .card_brands import CardBrands
from .shared.direction import Direction
from .payment_method_types import PaymentMethodTypes

__all__ = ["PaymentMethodListParams"]


class PaymentMethodListParams(TypedDict, total=False):
    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    broken: Optional[bool]
    """
    Filter by whether the stored credential has permanently stopped charging, such
    as a vault entry its provider closed.
    """

    card_brands: Optional[List[CardBrands]]
    """Only return cards on these networks, such as the networks the seller accepts.

    Payment methods that are not cards are unaffected.
    """

    card_funding_types: Optional[List[Literal["credit", "debit", "prepaid"]]]
    """Only return cards funded this way.

    A card whose funding could not be determined is excluded, and payment methods
    that are not cards are unaffected.
    """

    company_id: Optional[str]
    """The unique identifier of the company.

    Provide either this or member_id, not both. Omit both to address your own saved
    payment methods.
    """

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return payment methods created after this timestamp."""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return payment methods created before this timestamp."""

    direction: Optional[Direction]
    """The direction of the sort."""

    expired: Optional[bool]
    """Filter by expiry.

    Only a card can expire, so `false` keeps every payment method that is not past
    its expiration month and `true` returns expired cards alone.
    """

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    future_usage: Optional[Literal["off_session", "on_session"]]
    """
    How a payment method will be charged after the buyer leaves — the same
    vocabulary as a confirmation token's setup_future_usage.
    """

    has_payer_document: Optional[bool]
    """
    Filter cards by whether they carry the payer identity document their payment
    provider requires. Payment methods that are not cards are unaffected.
    """

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    member_id: Optional[str]
    """The unique identifier of the member to list payment methods for.

    Omit this and company_id to list your own saved payment methods.
    """

    payment_method_types: Optional[List[PaymentMethodTypes]]
    """Only return payment methods of these types.

    Pass the eligible `type` values from the payment method types catalogue so the
    list holds nothing the purchase cannot take. An empty list returns no payment
    methods.
    """
