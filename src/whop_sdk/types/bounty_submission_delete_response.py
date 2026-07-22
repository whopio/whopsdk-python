# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BountySubmissionDeleteResponse"]


class BountySubmissionDeleteResponse(BaseModel):
    id: str
    """ID of the cancelled submission."""

    deleted: bool
    """Always true."""
