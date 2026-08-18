# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MembershipTransferResponse"]


class MembershipTransferResponse(BaseModel):
    url: str
    """One-use URL the destination account opens to claim the membership."""
