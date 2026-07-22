# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["APIKeyListParams"]


class APIKeyListParams(TypedDict, total=False):
    resource_id: Required[str]
    """The company (`biz_`) or app (`app_`) tag to list API keys for."""

    resource_type: Required[Literal["account", "app"]]
    """The type of resource that owns the API keys."""

    after: str
    """A cursor; returns API keys after this position."""

    before: str
    """A cursor; returns API keys before this position."""

    created_after: Union[int, str]
    """Only return API keys created after this ISO 8601 timestamp."""

    created_before: Union[int, str]
    """Only return API keys created before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """The number of API keys to return (default 20, max 100)."""

    last: int
    """The number of API keys to return from the end of the range."""

    order: Literal["created_at"]
    """The field to sort API keys by."""
