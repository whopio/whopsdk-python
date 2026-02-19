# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .billing_reasons import BillingReasons
from .shared.currency import Currency
from .shared.direction import Direction
from .shared.receipt_status import ReceiptStatus
from .shared.friendly_receipt_status import FriendlyReceiptStatus

__all__ = ["PaymentListParams"]


class PaymentListParams(TypedDict, total=False):
    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    billing_reasons: Optional[List[BillingReasons]]
    """Filter payments by their billing reason."""

    company_id: Optional[str]
    """The unique identifier of the company to list payments for."""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return payments created after this timestamp."""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return payments created before this timestamp."""

    currencies: Optional[List[Currency]]
    """Filter payments by their currency code."""

    direction: Optional[Direction]
    """The direction of the sort."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    include_free: Optional[bool]
    """Whether to include payments with a zero amount."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    order: Optional[Literal["final_amount", "created_at", "paid_at"]]
    """The order to sort the results by."""

    plan_ids: Optional[SequenceNotStr[str]]
    """Filter payments to only those associated with these specific plan identifiers."""

    product_ids: Optional[SequenceNotStr[str]]
    """
    Filter payments to only those associated with these specific product
    identifiers.
    """

    query: Optional[str]
    """Search payments by user ID, membership ID, user email, name, or username.

    Email filtering requires the member:email:read permission.
    """

    statuses: Optional[List[ReceiptStatus]]
    """Filter payments by their current status."""

    substatuses: Optional[List[FriendlyReceiptStatus]]
    """Filter payments by their current substatus for more granular filtering."""
