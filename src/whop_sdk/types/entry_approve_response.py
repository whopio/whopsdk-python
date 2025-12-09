# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["EntryApproveResponse"]


class EntryApproveResponse(BaseModel):
    """An object representing an asynchronous job."""

    job_id: str
    """The ID of the job."""
