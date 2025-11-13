# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AccessTokenCreateParams", "CreateAccessTokenInputWithCompanyID", "CreateAccessTokenInputWithUserID"]


class CreateAccessTokenInputWithCompanyID(TypedDict, total=False):
    company_id: Required[str]
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

    If sent as an empty array or not provided, all permissions from the API key
    making the request will be available on the token. If sending an explicit list,
    they must be a subset of the API keys's existing permissions. Otherwise, an
    error will be raised.
    """


class CreateAccessTokenInputWithUserID(TypedDict, total=False):
    user_id: Required[str]
    """The ID of the User to generate the token for.

    The API key must have permission to access this User.
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The expiration timestamp for the access token.

    If not provided, a default expiration time of 1 hour will be used. The
    expiration can be set to a maximum of 3 hours from the current time.
    """

    scoped_actions: Optional[SequenceNotStr[str]]
    """Array of desired scoped actions for the access token.

    If sent as an empty array or not provided, all permissions from the API key
    making the request will be available on the token. If sending an explicit list,
    they must be a subset of the API keys's existing permissions. Otherwise, an
    error will be raised.
    """


AccessTokenCreateParams: TypeAlias = Union[CreateAccessTokenInputWithCompanyID, CreateAccessTokenInputWithUserID]
