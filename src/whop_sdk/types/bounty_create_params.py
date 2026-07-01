# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared.currency import Currency

__all__ = ["BountyCreateParams"]


class BountyCreateParams(TypedDict, total=False):
    base_unit_amount: Required[float]
    """The amount paid to each approved submission.

    The total bounty pool funded is this amount times accepted_submissions_limit,
    and must be at least 5 in the bounty's currency.
    """

    currency: Required[Currency]
    """The currency for the bounty pool funding amount."""

    description: Required[str]
    """The description of the bounty."""

    title: Required[str]
    """The title of the bounty."""

    accepted_submissions_limit: Optional[int]
    """The number of submissions that can be approved before the bounty closes.

    Defaults to 1. The total pool (base_unit_amount times this limit) must be at
    least 5 in the bounty's currency.
    """

    allowed_country_codes: Optional[SequenceNotStr[str]]
    """The ISO3166 country codes where this bounty should be visible.

    Empty means globally visible.
    """

    business_goal_type: Optional[
        Literal["clipping", "post_engagement", "owned_account_growth", "ugc_content", "local_activation", "other"]
    ]
    """What the poster is trying to accomplish with a workforce bounty.

    Used for product taxonomy and analytics, separate from the bounty's
    implementation type.
    """

    experience_id: Optional[str]
    """An optional experience to scope the bounty to."""

    origin_account_id: Optional[str]
    """The user (user*\\**) or company (biz*\\**) tag whose balance funds this bounty pool.

    Defaults to the requester's personal balance when omitted. The requester must be
    the user themself or an owner/admin of the company.
    """

    post_markdown_content: Optional[str]
    """Optional markdown body for the anchor forum post.

    Falls back to the bounty description when omitted.
    """

    post_title: Optional[str]
    """Optional title for the anchor forum post.

    Falls back to the bounty title when omitted.
    """

    scheduled_frequency: Optional[Literal["once", "hourly", "daily", "weekly", "monthly"]]
    """How often a scheduled bounty republishes a new bounty."""

    scheduled_publish_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """When to publish the bounty.

    When provided, the bounty is created as a hidden draft and published at this
    time instead of immediately. Must be in the future.
    """

    scheduled_timezone: Optional[str]
    """The IANA timezone used for recurring occurrences.

    Required when scheduled_publish_at is provided.
    """
