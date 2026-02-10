# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ExperienceCreateParams", "Logo"]


class ExperienceCreateParams(TypedDict, total=False):
    app_id: Required[str]
    """The unique identifier of the app that powers this experience."""

    company_id: Required[str]
    """The unique identifier of the company to create this experience for."""

    is_public: Optional[bool]
    """Whether the experience is publicly accessible without a membership."""

    logo: Optional[Logo]
    """A logo image displayed alongside the experience name."""

    name: Optional[str]
    """The display name of the experience. Defaults to the app's name if not provided."""

    section_id: Optional[str]
    """The unique identifier of the section to place the experience in."""


class Logo(TypedDict, total=False):
    """A logo image displayed alongside the experience name."""

    id: Required[str]
    """The ID of an existing file object."""
