# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ExportListParams"]


class ExportListParams(TypedDict, total=False):
    account_id: str
    """The account to list exports for, prefixed `biz_`.

    Defaults to the credential's account.
    """

    created_after: str
    """Only return exports created at or after this ISO 8601 timestamp."""

    created_before: str
    """Only return exports created at or before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """The sort direction."""

    order: Literal["created_at"]
    """The field to sort by."""

    resource: Literal[
        "ad_campaigns",
        "ad_groups",
        "ads",
        "audiences",
        "bounties",
        "bounty_submissions",
        "disputes",
        "events",
        "financial-activity",
        "members",
        "memberships",
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
        "ledger_lines",
        "withdrawal_lines",
    ]
    """Only return exports of this resource."""

    status: Literal["pending", "processing", "completed", "failed", "expired"]
    """Only return exports in this status."""
