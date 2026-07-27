# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ExportCreateParams"]


class ExportCreateParams(TypedDict, total=False):
    resource: Required[
        Literal[
            "ad_campaigns",
            "ad_groups",
            "ads",
            "members",
            "receipts",
            "unclaimed_memberships",
            "memberships",
            "tracking_links",
            "promo_codes",
            "resolutions",
            "disputes",
            "entries",
            "leads",
            "content_rewards_submissions",
            "invoices",
            "cancelation_reasons",
            "child_companies",
        ]
    ]
    """The resource to export, e.g. `receipts`, `members`, or `ads`."""

    account_id: str
    """The account to export from, prefixed `biz_`.

    Defaults to the credential's account.
    """

    columns: SequenceNotStr[str]
    """Column keys to include. Empty means all columns for the resource."""

    filters: object
    """Resource-specific filters, mirroring the dashboard table filters."""

    timezone: str
    """IANA timezone for date columns, e.g. `America/New_York`. Defaults to `UTC`."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
