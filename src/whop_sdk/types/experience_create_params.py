# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ExperienceCreateParams"]


class ExperienceCreateParams(TypedDict, total=False):
    app_id: Required[str]
    """The ID of the app to create the experience for"""

    company_id: Required[str]
    """The ID of the company to create the experience for"""

    is_public: Optional[bool]
    """Whether the experience is publicly accessible"""

    name: Optional[str]
    """The name of the experience"""

    section_id: Optional[str]
    """The ID of the section to create the experience in"""
