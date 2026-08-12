# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MethodUpdateParams"]


class MethodUpdateParams(TypedDict, total=False):
    nickname: Required[str]
    """
    New label for the payout method, with at least one non-whitespace character and
    a maximum of 100 characters.
    """
