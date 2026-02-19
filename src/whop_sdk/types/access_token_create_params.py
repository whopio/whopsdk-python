# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AccessTokenCreateParams"]


class AccessTokenCreateParams(TypedDict, total=False):
    company_id: Optional[str]
    """
    The unique identifier of the company to generate the token for, starting with
    'biz\\__'. The API key must have permission to access this company.
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The expiration timestamp for the access token.

    Defaults to 1 hour from now, with a maximum of 3 hours.
    """

    scoped_actions: Optional[SequenceNotStr[str]]
    """An array of permission scopes to grant to the access token.

    If empty or omitted, all permissions from the authenticating credential are
    inherited. Must be a subset of the credential's permissions.
    """

    user_id: Optional[str]
    """
    The unique identifier of the user to generate the token for, starting with
    'user\\__'. The API key must have permission to access this user.
    """
