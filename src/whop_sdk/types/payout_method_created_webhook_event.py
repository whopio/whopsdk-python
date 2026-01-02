# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PayoutMethodCreatedWebhookEvent", "Data", "DataCompany", "DataDestination"]


class DataCompany(BaseModel):
    """The company associated with the payout token"""

    id: str
    """The ID (tag) of the company."""


class DataDestination(BaseModel):
    """The payout destination associated with the payout token"""

    category: Literal["crypto", "rtp", "next_day_bank", "bank_wire", "digital_wallet", "unknown"]
    """The category of the payout destination"""

    country_code: str
    """The country code of the payout destination"""

    name: str
    """The name of the payer associated with the payout destination"""


class Data(BaseModel):
    """An object representing an user's setup payout destination."""

    id: str
    """The ID of the payout token"""

    company: Optional[DataCompany] = None
    """The company associated with the payout token"""

    currency: str
    """The currency code of the payout destination.

    This is the currency that payouts will be made in for this token.
    """

    destination: Optional[DataDestination] = None
    """The payout destination associated with the payout token"""

    is_default: bool
    """Whether this payout token is the default for the payout account"""

    nickname: Optional[str] = None
    """An optional nickname for the payout token to help the user identify it.

    This is not used by the provider and is only for the user's reference.
    """


class PayoutMethodCreatedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    data: Data
    """An object representing an user's setup payout destination."""

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["payout_method.created"]
    """The webhook event type"""
