# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ReactionDeleteParams"]


class ReactionDeleteParams(TypedDict, total=False):
    emoji: Optional[str]
    """The emoji to remove, in shortcode or unicode format.

    For example, ':heart:' or a unicode emoji. Required when the id refers to a
    message or post instead of a reaction.
    """
