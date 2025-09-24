# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["InvoiceListParams", "Filters"]


class InvoiceListParams(TypedDict, total=False):
    company_id: Required[str]
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    after: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    before: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    direction: Optional[Literal["asc", "desc"]]
    """The direction of the sort."""

    filters: Optional[Filters]
    """Filters for the invoices table."""

    first: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    last: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    order: Optional[Literal["id", "created_at", "due_date"]]
    """Which columns can be used to sort."""


class Filters(TypedDict, total=False):
    access_pass_ids: Optional[SequenceNotStr[str]]

    collection_methods: Optional[List[Literal["send_invoice", "charge_automatically"]]]

    statuses: Optional[List[Literal["open", "paid", "past_due", "void"]]]
