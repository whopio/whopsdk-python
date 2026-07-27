# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .permission_action import PermissionAction

__all__ = ["PermissionListResponse", "Data"]


class Data(BaseModel):
    action: PermissionAction
    """A permission action identifier, such as `company:basic:read`."""

    granted: bool
    """Whether the credential is granted the action for the resource."""


class PermissionListResponse(BaseModel):
    data: List[Data]
