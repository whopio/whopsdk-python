# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PreferenceUpdateParams"]


class PreferenceUpdateParams(TypedDict, total=False):
    investigation_enabled: bool
    """Whether investigation mode is enabled for the user.

    Only meaningful for staff users with investigation access.
    """
