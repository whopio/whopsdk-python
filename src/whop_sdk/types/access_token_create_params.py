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
    """The ID of the Company to generate the token for.

    The API key must have permission to access this Company, such as the being the
    company the API key belongs to or a sub-merchant of it
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The expiration timestamp for the access token.

    If not provided, a default expiration time of 1 hour will be used. The
    expiration can be set to a maximum of 3 hours from the current time.
    """

    scoped_actions: Optional[SequenceNotStr[str]]
    """Array of desired scoped actions for the access token.

    If sent as an empty array or not provided, all permissions from the
    authenticating credential (API key or OAuth token) will be available on the
    token. If sending an explicit list, they must be a subset of the credential's
    existing permissions. Otherwise, an error will be raised.
    """

    user_id: Optional[str]
    """The ID of the User to generate the token for.

    The API key must have permission to access this User.
    """
