# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExperienceListParams"]


class ExperienceListParams(TypedDict, total=False):
    after: str
    """A cursor; returns preferences after this position."""

    first: int
    """The number of preferences to return."""
