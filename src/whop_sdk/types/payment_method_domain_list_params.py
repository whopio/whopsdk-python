# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentMethodDomainListParams"]


class PaymentMethodDomainListParams(TypedDict, total=False):
    account_id: str
    """Only domains registered for this account (`biz_` tag).

    Defaults to the caller's account plus its connected accounts.
    """

    after: str
    """Cursor to paginate forwards from."""

    before: str
    """Cursor to paginate backwards from."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only domains created after this ISO 8601 timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only domains created before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """Number of domains to return from the start of the window."""

    hostname: str
    """Only the domain with this exact hostname."""

    last: int
    """Number of domains to return from the end of the window."""

    order: Literal["created_at"]
    """Sort field."""

    provider: Literal["apple"]
    """Only domains registered with this wallet provider."""

    status: Literal["pending", "verified"]
    """Only domains with this verification status."""
