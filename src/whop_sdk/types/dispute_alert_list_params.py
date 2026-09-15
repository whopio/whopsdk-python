# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DisputeAlertListParams"]


class DisputeAlertListParams(TypedDict, total=False):
    account_id: str
    """Only alerts on this account's payments (`biz_` tag).

    Omit it to cover every account you can read.
    """

    after: str
    """Return results after this cursor.

    Use `page_info.end_cursor` from the previous response to fetch the next page.
    """

    before: str
    """Return results before this cursor.

    Use `page_info.start_cursor` from the previous response to fetch the previous
    page.
    """

    created_after: str
    """Only alerts Whop received after this ISO 8601 timestamp."""

    created_before: str
    """Only alerts Whop received before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """Number of results to return from the start of the range."""

    last: int
    """Number of results to return from the end of the range."""

    order: Literal["created_at", "reported_at", "amount"]
    """The field to sort alerts by."""

    payment_id: str
    """Only alerts on this payment (`pay_` tag). A payment can carry several."""

    type: Literal["early_fraud_warning", "dispute_alert", "rapid_dispute_resolution"]
    """Only alerts of this kind.

    `early_fraud_warning` for issuer fraud reports, `dispute_alert` for pre-dispute
    notices, `rapid_dispute_resolution` for Visa RDR cases the network already
    closed.
    """

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
