# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .billing_reasons import BillingReasons
from .shared.currency import Currency
from .shared.direction import Direction
from .shared.receipt_status import ReceiptStatus
from .shared.friendly_receipt_status import FriendlyReceiptStatus

__all__ = ["PaymentListParams"]


class PaymentListParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to list payments for"""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    billing_reasons: Optional[List[BillingReasons]]
    """The billing reason for the payment"""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The minimum creation date to filter by"""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The maximum creation date to filter by"""

    currencies: Optional[List[Currency]]
    """The currency of the payment."""

    direction: Optional[Direction]
    """The direction of the sort."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    include_free: Optional[bool]
    """Whether to include free payments."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    order: Optional[Literal["final_amount", "created_at", "paid_at"]]
    """The order to sort the results by."""

    plan_ids: Optional[SequenceNotStr[str]]
    """A specific plan."""

    product_ids: Optional[SequenceNotStr[str]]
    """A specific product."""

    statuses: Optional[List[ReceiptStatus]]
    """The status of the payment."""

    substatuses: Optional[List[FriendlyReceiptStatus]]
    """The substatus of the payment."""
