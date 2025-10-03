# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["VisibilityFilter"]

VisibilityFilter: TypeAlias = Literal[
    "visible", "hidden", "archived", "quick_link", "all", "not_quick_link", "not_archived"
]
