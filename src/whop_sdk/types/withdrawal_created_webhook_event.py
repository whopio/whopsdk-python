# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WithdrawalCreatedWebhookEvent", "Data", "DataPayoutMethod", "DataPayoutMethodSupportedPayoutMethod"]


class DataPayoutMethodSupportedPayoutMethod(BaseModel):
    """Supported payout method display details."""

    icon_url: Optional[str] = None
    """Supported payout method icon URL."""

    payer_name: Optional[str] = None
    """Supported payout method display name."""


class DataPayoutMethod(BaseModel):
    """The saved payout method used.

    Requires payout:destination:read; null without it.
    """

    nickname: Optional[str] = None
    """Saved payout method nickname."""

    supported_payout_method: Optional[DataPayoutMethodSupportedPayoutMethod] = None
    """Supported payout method display details."""


class Data(BaseModel):
    id: str
    """Payout ID, prefixed `wdrl_`."""

    amount: float
    """The payout amount in whole currency units."""

    created_at: datetime
    """When the payout was created."""

    currency: str
    """Payout currency."""

    estimated_arrival: Optional[datetime] = None
    """Estimated time the funds become available in the destination account."""

    fee_amount: float
    """The fee charged for the payout, in the payout currency."""

    notes: Optional[str] = None
    """
    Free-form notes attached by the payout creator, or `null` when none were
    provided. Maximum 255 characters.
    """

    object: Literal["payout"]

    payer_name: Optional[str] = None
    """Name of the entity processing the payout."""

    payout_method: Optional[DataPayoutMethod] = None
    """The saved payout method used.

    Requires payout:destination:read; null without it.
    """

    payout_request_id: Optional[str] = None
    """Payout request ID, prefixed `cofr_`, returned by `POST /payouts`.

    Match it to the settled payout in `GET /payouts`. Returns `null` for payouts not
    created by `POST /payouts`.
    """

    speed: Literal["standard", "instant"]
    """Payout delivery speed."""

    status: Literal["requested", "awaiting_payment", "in_transit", "completed", "failed", "canceled", "denied"]
    """Current payout status."""

    trace_code: Optional[str] = None
    """ACH trace number the recipient's bank can use to locate this payout.

    Assigned when the payout is submitted to the bank, so it is `null` before then
    and on payouts not sent over ACH.
    """


class WithdrawalCreatedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    api_version_date: Optional[str] = None
    """The dated API version (Api-Version-Date) the payload is serialized to"""

    data: Data

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["withdrawal.created"]
    """The webhook event type"""

    company_id: Optional[str] = None
    """The account ID that this webhook event is associated with"""
