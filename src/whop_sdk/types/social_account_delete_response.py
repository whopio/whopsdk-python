# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SocialAccountDeleteResponse"]


class SocialAccountDeleteResponse(BaseModel):
    id: str
    """ID of the disconnected social account."""

    deleted: bool
    """Always true."""
