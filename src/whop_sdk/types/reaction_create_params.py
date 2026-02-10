# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ReactionCreateParams"]


class ReactionCreateParams(TypedDict, total=False):
    resource_id: Required[str]
    """The unique identifier of the message or forum post to react to."""

    emoji: Optional[str]
    """The emoji to react with, in shortcode or unicode format.

    For example, ':heart:' or a unicode emoji. Ignored in forums where reactions are
    always likes.
    """

    poll_option_id: Optional[str]
    """The unique identifier of a poll option to vote for.

    Only valid when the target message or post contains a poll.
    """
