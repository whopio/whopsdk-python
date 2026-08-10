# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Export"]


class Export(BaseModel):
    id: str
    """Export ID, prefixed `exprt_`."""

    created_at: str
    """When the export was requested, as an ISO 8601 timestamp."""

    download_url: Optional[str] = None
    """A short-lived link to download the finished CSV.

    `null` until `status` is `completed`, and again once the export has expired.
    """

    expires_at: str
    """
    When the CSV is deleted and the export moves to `expired`, as an ISO 8601
    timestamp. Exports are retained for 30 days.
    """

    resource: Literal[
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
        "ledger_lines",
        "withdrawal_lines",
    ]
    """The resource that was exported, e.g. `receipts`, `members`, or `payouts`."""

    status: Literal["pending", "processing", "completed", "failed", "expired"]
    """
    `pending` or `processing` while the CSV is generated, `completed` when the
    download is ready, `failed` if it errored, `expired` once the CSV has been
    deleted.
    """

    updated_at: str
    """When the export last changed status, as an ISO 8601 timestamp."""
