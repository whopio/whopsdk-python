# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
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
    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    billing_reasons: List[BillingReasons]
    """Filter payments by their billing reason."""

    checkout_configuration_ids: SequenceNotStr[str]
    """Only return payments from these checkout configurations."""

    company_id: str
    """The unique identifier of the company to list payments for."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return payments created after this timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return payments created before this timestamp."""

    currencies: List[Currency]
    """Filter payments by their currency code."""

    direction: Direction
    """The sort direction for ordering results, either ascending or descending."""

    first: int
    """Returns the first _n_ elements from the list."""

    include_free: bool
    """Whether to include payments with a zero amount.

    Defaults to false, so zero-amount payments are omitted unless you set this to
    true — a company whose sales are all free plans returns an empty list without
    it.
    """

    last: int
    """Returns the last _n_ elements from the list."""

    order: Literal["final_amount", "created_at", "paid_at"]
    """The field to order results by, such as creation date."""

    plan_ids: SequenceNotStr[str]
    """Filter payments to only those associated with these specific plan identifiers."""

    product_ids: SequenceNotStr[str]
    """
    Filter payments to only those associated with these specific product
    identifiers.
    """

    query: str
    """Search payments by user ID, membership ID, user email, name, or username.

    Email filtering requires the member:email:read permission.
    """

    statuses: List[ReceiptStatus]
    """Filter payments by their current status."""

    substatuses: List[FriendlyReceiptStatus]
    """Filter payments by their current substatus for more granular filtering."""

    updated_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return payments last updated after this timestamp."""

    updated_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return payments last updated before this timestamp."""
