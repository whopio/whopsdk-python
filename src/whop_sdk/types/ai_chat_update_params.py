# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AIChatUpdateParams"]


class AIChatUpdateParams(TypedDict, total=False):
    current_company_id: Optional[str]
    """The ID of the company to set as the current company in context for the AI chat"""

    title: Optional[str]
    """The new title for the AI chat"""
