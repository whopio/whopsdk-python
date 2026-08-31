# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BountyListParams"]


class BountyListParams(TypedDict, total=False):
    account_id: str
    """Scope the list to this account (`biz_` tag).

    Requires read access to the account; account API keys may pass their own account
    or a connected account.
    """

    after: str
    """Cursor to paginate forwards from."""

    before: str
    """Cursor to paginate backwards from."""

    business_goal_type: Literal[
        "clipping",
        "post_engagement",
        "owned_account_growth",
        "ugc_content",
        "local_activation",
        "data_capture",
        "other",
    ]
    """Filter by the poster's declared goal.

    Bounties created before the goal taxonomy carry no goal and never match this
    filter.
    """

    country: str
    """Only bounties workable from this country, as an ISO 3166-1 alpha-2 code.

    Bounties with no country targeting are workable worldwide and always match.
    """

    created_after: str
    """Only bounties created after this ISO 8601 timestamp."""

    created_before: str
    """Only bounties created before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    experience_id: str
    """Only bounties posted to this forum experience, prefixed `exp_`.

    An unknown experience, or one outside the caller's scope, matches nothing.
    """

    first: int
    """Number of bounties to return from the start of the window."""

    last: int
    """Number of bounties to return from the end of the window."""

    order: Literal["created_at", "gross_paid_out_amount", "gross_reward_amount"]
    """Sort field."""

    query: str
    """Substring match on the bounty title or ID."""

    status: Literal["scheduled", "open", "closed", "completed", "canceled"]
    """Filter by lifecycle state."""

    user_id: str
    """List the bounties this user participated in (`user_` tag).

    Must be the authenticated user.
    """

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
