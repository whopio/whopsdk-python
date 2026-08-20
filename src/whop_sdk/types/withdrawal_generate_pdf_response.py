# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["WithdrawalGeneratePdfResponse"]


class WithdrawalGeneratePdfResponse(BaseModel):
    """A temporary link to a generated withdrawal PDF invoice."""

    expires_at: datetime
    """The timestamp after which the withdrawal PDF URL is no longer valid."""

    url: str
    """The temporary URL for downloading the withdrawal PDF invoice."""
