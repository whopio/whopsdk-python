# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["PersonListParams"]


class PersonListParams(TypedDict, total=False):
    account_id: str
    """The ID of the account, which will look like biz\\__******\\********.

    Optional for account API keys; required for credentials that can access multiple
    accounts.
    """

    after: str
    """A cursor for fetching people after a previous page."""

    audience_id: str
    """Only include people in this audience."""

    before: str
    """A cursor for fetching people before a later page."""

    country: str
    """
    Only include people whose most recent visit came from this ISO 3166-1 alpha-2
    country code.
    """

    custom_event: str
    """Only include people who fired this custom pixel event."""

    direction: Literal["asc", "desc"]
    """Sort direction. Defaults to desc."""

    email: str
    """Only include the person linked to this email address."""

    event_name: SequenceNotStr[str]
    """Only include people who fired any of these events, e.g.

    payment.completed or page.checkout.view.
    """

    first: int
    """The number of people to return (default 100, max 100)."""

    first_seen_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include people first seen at or after this ISO 8601 timestamp."""

    first_seen_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include people first seen before this ISO 8601 timestamp."""

    has_purchased: bool
    """true for customers only, false for people who have never purchased."""

    last_seen_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include people last seen at or after this ISO 8601 timestamp."""

    last_seen_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include people last seen before this ISO 8601 timestamp."""

    order: Literal[
        "first_seen_at",
        "last_seen_at",
        "first_purchase_at",
        "last_purchase_at",
        "purchase_count",
        "event_count",
        "ltv",
        "aov",
        "name",
        "email",
    ]
    """Column to sort by. Defaults to last_seen_at."""

    phone: str
    """Only include the person linked to this phone number."""

    query: str
    """
    Search people by name, email, phone, or whop user ID (case-insensitive substring
    match).
    """

    source: SequenceNotStr[str]
    """Only include people acquired from any of these sources.

    A source is a platform (google, meta, whop, direct), custom:<utm source>, an ad
    entity tag (adcamp*/adgrp*/ad\\__), or a referrer domain like example.com.
    """

    user_id: str
    """Only include the person linked to this whop user ID."""
