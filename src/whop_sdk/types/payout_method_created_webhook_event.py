# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PayoutMethodCreatedWebhookEvent", "Data", "DataCompany", "DataDestination"]


class DataCompany(BaseModel):
    """The company associated with this payout destination.

    Null if not linked to a specific company.
    """

    id: str
    """The unique identifier for the company."""


class DataDestination(BaseModel):
    """The payout destination configuration linked to this token.

    Null if not yet configured.
    """

    category: Literal["crypto", "rtp", "next_day_bank", "bank_wire", "digital_wallet", "unknown"]
    """The category of the payout destination"""

    country_code: str
    """The country code of the payout destination"""

    name: str
    """The name of the payer associated with the payout destination"""


class Data(BaseModel):
    """
    A configured payout destination where a user receives earned funds, such as a bank account or digital wallet.
    """

    id: str
    """The unique identifier for the payout token."""

    account_reference: Optional[str] = None
    """
    A masked identifier for the payout destination, such as the last four digits of
    a bank account or an email address. Null if no reference is available.
    """

    company: Optional[DataCompany] = None
    """The company associated with this payout destination.

    Null if not linked to a specific company.
    """

    created_at: datetime
    """The datetime the payout token was created."""

    currency: str
    """
    The three-letter ISO currency code that payouts are delivered in for this
    destination.
    """

    destination: Optional[DataDestination] = None
    """The payout destination configuration linked to this token.

    Null if not yet configured.
    """

    institution_name: Optional[str] = None
    """The name of the bank or financial institution receiving payouts.

    Null if not applicable or not provided.
    """

    is_default: bool
    """
    Whether this is the default payout destination for the associated payout
    account.
    """

    nickname: Optional[str] = None
    """A user-defined label to help identify this payout destination.

    Not sent to the provider. Null if no nickname has been set.
    """


class PayoutMethodCreatedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    api_version_date: Optional[str] = None
    """The dated API version (Api-Version-Date) the payload is serialized to"""

    data: Data
    """
    A configured payout destination where a user receives earned funds, such as a
    bank account or digital wallet.
    """

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["payout_method.created"]
    """The webhook event type"""

    company_id: Optional[str] = None
    """The account ID that this webhook event is associated with"""
