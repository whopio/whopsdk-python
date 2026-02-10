# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["AccessTokenCreateResponse"]


class AccessTokenCreateResponse(BaseModel):
    """
    A short-lived access token used to authenticate API requests on behalf of a user or application.
    """

    token: str
    """
    The signed JWT access token string to include in API request Authorization
    headers.
    """

    expires_at: datetime
    """
    The timestamp after which this access token is no longer valid and must be
    refreshed.
    """
