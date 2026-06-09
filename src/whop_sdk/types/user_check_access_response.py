# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .shared.access_level import AccessLevel

__all__ = ["UserCheckAccessResponse"]


class UserCheckAccessResponse(BaseModel):
    """The result of a has access check for the developer API"""

    access_level: AccessLevel
    """The permission level of the user"""

    has_access: bool
    """Whether the user has access to the resource"""
