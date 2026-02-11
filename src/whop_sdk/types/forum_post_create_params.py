# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .shared.currency import Currency
from .forum_post_visibility_type import ForumPostVisibilityType

__all__ = ["ForumPostCreateParams", "Attachment", "Poll", "PollOption"]


class ForumPostCreateParams(TypedDict, total=False):
    experience_id: Required[str]
    """The unique identifier of the experience to create this post in.

    For example, 'exp_xxxxx'. Pass 'public' along with company_id to automatically
    use the company's public forum.
    """

    attachments: Optional[Iterable[Attachment]]
    """A list of file attachments to include with the post, such as images or videos."""

    company_id: Optional[str]
    """The unique identifier of the company whose public forum to post in.

    Required when experience_id is 'public'. For example, 'biz_xxxxx'.
    """

    content: Optional[str]
    """The main body of the post in Markdown format.

    For example, 'Check out this **update**'. Hidden if the post is paywalled and
    the viewer has not purchased access.
    """

    is_mention: Optional[bool]
    """
    Whether to send this post as a mention notification to all users in the
    experience who have mentions enabled.
    """

    parent_id: Optional[str]
    """The unique identifier of the parent post to comment on.

    Omit this field to create a top-level post.
    """

    paywall_amount: Optional[float]
    """The price to unlock this post in the specified paywall currency.

    For example, 5.00 for $5.00. When set, users must purchase access to view the
    post content.
    """

    paywall_currency: Optional[Currency]
    """The available currencies on the platform"""

    pinned: Optional[bool]
    """Whether this post should be pinned to the top of the forum."""

    poll: Optional[Poll]
    """A poll to attach to this post, allowing members to vote on options."""

    title: Optional[str]
    """The title of the post, displayed prominently at the top.

    Required for paywalled posts as it remains visible to non-purchasers.
    """

    visibility: Optional[ForumPostVisibilityType]
    """The visibility types for forum posts"""


class Attachment(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing file object."""


class PollOption(TypedDict, total=False):
    """Input type for a single poll option"""

    id: Required[str]
    """Sequential ID for the poll option (starting from '1')"""

    text: Required[str]
    """The text of the poll option"""


class Poll(TypedDict, total=False):
    """A poll to attach to this post, allowing members to vote on options."""

    options: Required[Iterable[PollOption]]
    """The options for the poll. Must have sequential IDs starting from 1"""
