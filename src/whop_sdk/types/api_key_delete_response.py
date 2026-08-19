# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["APIKeyDeleteResponse"]


class APIKeyDeleteResponse(BaseModel):
    id: str
    """The ID of the revoked key."""

    deleted: bool
    """Always `true`: the key was revoked."""
