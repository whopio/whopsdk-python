# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AccessTokenCreateParams"]


class AccessTokenCreateParams(TypedDict, total=False):
    scoped_actions: Required[SequenceNotStr[str]]
    """Array of desired scoped actions for the access token.

    This list must be a subset of the API keys's existing permissions. Otherwise, an
    error will be raised.
    """

    target_resource_id: Required[str]
    """
    The ID of the target resource (Company, User, etc.) for which the access token
    is being created.
    """

    target_resource_type: Required[Literal["company", "product", "experience", "app", "user"]]
    """The type of the target resource (company, user, product, experience, etc.)."""

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The expiration timestamp for the access token.

    If not provided, a default expiration time of 1 hour will be used. The
    expiration can be set to a maximum of 3 hours from the current time.
    """
