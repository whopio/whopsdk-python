# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SupportChannelCreateParams"]


class SupportChannelCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """The unique identifier of the company to create the support channel in."""

    user_id: Required[str]
    """The user ID (e.g.

    'user_xxxxx') or username of the customer to open a support channel for.
    """

    custom_name: Optional[str]
    """Optional custom display name for the support channel."""
