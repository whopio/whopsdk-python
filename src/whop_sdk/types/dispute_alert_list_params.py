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
    """A cursor; returns alerts after this position."""

    before: str
    """A cursor; returns alerts before this position."""

    created_after: str
    """Only alerts Whop received after this ISO 8601 timestamp."""

    created_before: str
    """Only alerts Whop received before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """The number of alerts to return (default 20, max 100)."""

    last: int
    """The number of alerts to return from the end of the range."""

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
