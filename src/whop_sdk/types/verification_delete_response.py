# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["VerificationDeleteResponse"]


class VerificationDeleteResponse(BaseModel):
    id: Optional[str] = None
    """Deleted verification ID."""

    deleted: Optional[bool] = None
    """Whether the verification was unlinked."""
