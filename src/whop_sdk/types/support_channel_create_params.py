# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SupportChannelCreateParams"]


class SupportChannelCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to create the support chat in"""

    user_id: Required[str]
    """The ID (user_xxx) or username of the user to create the support chat for"""
