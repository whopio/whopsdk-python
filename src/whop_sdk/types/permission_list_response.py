# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["PermissionListResponse", "Data"]


class Data(BaseModel):
    action: str
    """Permission action identifier, for example `company:basic:read`."""

    granted: bool
    """Whether the credential is granted the action for the resource."""


class PermissionListResponse(BaseModel):
    data: List[Data]
