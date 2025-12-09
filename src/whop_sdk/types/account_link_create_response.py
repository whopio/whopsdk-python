# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["AccountLinkCreateResponse"]


class AccountLinkCreateResponse(BaseModel):
    """
    An object representing a url that a user can be directed to to access their account.
    """

    expires_at: datetime
    """The expiration timestamp of the url."""

    url: str
    """The URL to navigate the user to."""
