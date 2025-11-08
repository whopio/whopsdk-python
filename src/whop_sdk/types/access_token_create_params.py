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
    """Array of desired scoped actions for the access token."""

    target_resource_id: Required[str]
    """
    The ID of the target resource (Company or User) for which the access token is
    being created.
    """

    target_resource_type: Required[Literal["company", "product", "experience", "app", "user"]]
    """The type of the target resource (Company or User)."""

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The expiration timestamp for the access token.

    If not provided, a default expiration time will be used.
    """
