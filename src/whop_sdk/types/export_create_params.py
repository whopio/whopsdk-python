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
            "apps",
            "audiences",
            "bounties",
            "bounty_submissions",
            "card_transactions",
            "checkout_configurations",
            "disputes",
            "events",
            "financial-activity",
            "members",
            "memberships",
            "payout_methods",
            "payouts",
            "people",
            "plans",
            "products",
            "resolution_center_cases",
            "shipments",
            "social_accounts",
            "team_members",
            "transfers",
            "webhooks",
            "receipts",
            "unclaimed_memberships",
            "tracking_links",
            "promo_codes",
            "resolutions",
            "entries",
            "leads",
            "content_rewards_submissions",
            "invoices",
            "cancelation_reasons",
            "child_companies",
        ]
    ]
    """The resource to export, e.g. `payouts`, `receipts`, or `members`."""

    account_id: str
    """The account to export from, prefixed `biz_`.

    Defaults to the credential's account.
    """

    columns: SequenceNotStr[str]
    """Column keys to include. Empty means all columns for the resource."""

    filters: object
    """Resource-specific filters.

    For native REST resources (`payouts`, `transfers`, `memberships`) these are the
    resource's own list query params; for dashboard tables they mirror the dashboard
    table filters.
    """

    timezone: str
    """IANA timezone for date columns, e.g. `America/New_York`. Defaults to `UTC`."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
