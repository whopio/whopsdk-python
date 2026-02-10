# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExperienceUpdateParams", "Logo"]


class ExperienceUpdateParams(TypedDict, total=False):
    access_level: Optional[Literal["public", "private"]]
    """The different access levels for experiences (PUBLIC IS NEVER USED ANYMORE)."""

    is_public: Optional[bool]
    """Whether the experience is publicly accessible without a membership."""

    logo: Optional[Logo]
    """A logo image displayed alongside the experience name."""

    name: Optional[str]
    """The display name of the experience."""

    order: Optional[str]
    """The position of the experience within its section for display ordering."""

    section_id: Optional[str]
    """The unique identifier of the section to move the experience into."""


class Logo(TypedDict, total=False):
    """A logo image displayed alongside the experience name."""

    id: Required[str]
    """The ID of an existing file object."""
