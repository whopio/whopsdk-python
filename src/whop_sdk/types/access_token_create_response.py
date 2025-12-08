# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["AccessTokenCreateResponse"]


class AccessTokenCreateResponse(BaseModel):
    """An object representing an access token used for authenticating API requests."""

    token: str
    """The JWT access token string."""

    expires_at: datetime
    """The expiration timestamp of the access token."""
