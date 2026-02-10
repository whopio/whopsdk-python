# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["AccountLinkCreateResponse"]


class AccountLinkCreateResponse(BaseModel):
    """
    A temporary, time-limited URL that grants a user access to an external account management page.
    """

    expires_at: datetime
    """The timestamp after which this account link URL is no longer valid."""

    url: str
    """The temporary URL to redirect the user to for account access.

    Expires at the time specified by expires_at.
    """
