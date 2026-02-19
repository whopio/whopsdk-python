# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .payout_destination_category import PayoutDestinationCategory

__all__ = ["PayoutMethodListResponse", "Company", "Destination"]


class Company(BaseModel):
    """The company associated with this payout destination.

    Null if not linked to a specific company.
    """

    id: str
    """The unique identifier for the company."""


class Destination(BaseModel):
    """The payout destination configuration linked to this token.

    Null if not yet configured.
    """

    category: PayoutDestinationCategory
    """The category of the payout destination"""

    country_code: str
    """The country code of the payout destination"""

    name: str
    """The name of the payer associated with the payout destination"""


class PayoutMethodListResponse(BaseModel):
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

    company: Optional[Company] = None
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

    destination: Optional[Destination] = None
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
