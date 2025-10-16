# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ReactionCreateParams"]


class ReactionCreateParams(TypedDict, total=False):
    resource_id: Required[str]
    """The ID of the post or message to react to."""

    emoji: Optional[str]
    """The emoji to react with (e.g., :heart: or '😀').

    It will be ignored in forums, as everything will be :heart:
    """
