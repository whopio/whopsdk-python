# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SocialAccountLeadFormsParams"]


class SocialAccountLeadFormsParams(TypedDict, total=False):
    account_id: Required[str]
    """The Account (a biz\\__ identifier) the social account is connected to."""
