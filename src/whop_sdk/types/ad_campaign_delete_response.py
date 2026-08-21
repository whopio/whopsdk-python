# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AdCampaignDeleteResponse"]


class AdCampaignDeleteResponse(BaseModel):
    id: str
    """ID of the deleted ad campaign."""

    deleted: bool
    """Always true."""
