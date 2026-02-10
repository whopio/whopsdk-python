# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DmChannelCreateParams"]


class DmChannelCreateParams(TypedDict, total=False):
    with_user_ids: Required[SequenceNotStr[str]]
    """The list of user identifiers to include in the DM channel.

    Each entry can be an email, username, or user ID (e.g. 'user_xxxxx').
    """

    company_id: Optional[str]
    """The unique identifier of the company to scope this DM channel to.

    When set, the channel is visible only within that company context.
    """

    custom_name: Optional[str]
    """A custom display name for the DM channel. For example, 'Project Discussion'."""
