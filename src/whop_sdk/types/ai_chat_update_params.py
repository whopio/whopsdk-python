# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AIChatUpdateParams"]


class AIChatUpdateParams(TypedDict, total=False):
    current_company_id: Optional[str]
    """
    The unique identifier of the company to set as context for the AI chat (e.g.,
    "biz_XXXXX").
    """

    title: Optional[str]
    """The new display title for the AI chat thread (e.g., "Help with billing")."""
