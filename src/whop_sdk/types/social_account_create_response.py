# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SocialAccountCreateResponse"]


class SocialAccountCreateResponse(BaseModel):
    authorize_url: str
    """The OAuth authorization URL to redirect the user to."""
