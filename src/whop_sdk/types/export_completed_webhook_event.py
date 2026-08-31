# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExportCompletedWebhookEvent", "Data"]


class Data(BaseModel):
    id: str
    """Export ID, prefixed `exprt_`."""

    created_at: str
    """When the export was requested, as an ISO 8601 timestamp."""

    download_url: Optional[str] = None
    """A short-lived link to download the finished file.

    `null` until `status` is `completed`, and again once the export has expired.
    """

    expires_at: str
    """
    When the file is deleted and the export moves to `expired`, as an ISO 8601
    timestamp. Exports are retained for 30 days.
    """

    progress_percent: Optional[int] = None
    """Estimated completion percentage from 0 to 100."""

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
        "members",
        "receipts",
        "unclaimed_memberships",
        "memberships",
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
    `pending` or `processing` while the file is generated, `completed` when the
    download is ready, `failed` if it errored, `expired` once the file has been
    deleted.
    """

    updated_at: str
    """When the export last changed, as an ISO 8601 timestamp."""


class ExportCompletedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    api_version_date: Optional[str] = None
    """The dated API version (Api-Version-Date) the payload is serialized to"""

    data: Data

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["export.completed"]
    """The webhook event type"""

    account_id: Optional[str] = None
    """The account ID that this webhook event is associated with"""

    previous_attributes: Optional[object] = None
    """
    For some `.updated` events, the old values of the payload fields that changed,
    keyed by field name. Omitted when no capture is available for the event
    """
