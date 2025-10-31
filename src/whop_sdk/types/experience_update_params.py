# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ExperienceUpdateParams", "Logo"]


class ExperienceUpdateParams(TypedDict, total=False):
    access_level: Optional[Literal["public", "private"]]
    """The different access levels for experiences (PUBLIC IS NEVER USED ANYMORE)."""

    logo: Logo
    """The logo for the experience"""

    name: Optional[str]
    """The name of the experience."""

    order: Optional[str]
    """The order of the experience in the section."""

    section_id: Optional[str]
    """The ID of the section to update."""


class Logo(total=False):
    pass
