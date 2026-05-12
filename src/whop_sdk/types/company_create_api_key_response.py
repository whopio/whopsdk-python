# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CompanyCreateAPIKeyResponse"]


class CompanyCreateAPIKeyResponse(BaseModel):
    """An API key created for a child company, including the one-time secret key."""

    id: str
    """The unique identifier for the authorized api key."""

    name: Optional[str] = None
    """A user set name to identify an API key"""

    secret_key: str
    """The secret key used to authenticate requests. Only returned at creation time."""
