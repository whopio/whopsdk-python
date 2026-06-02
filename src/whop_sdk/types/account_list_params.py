# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
    page: int
    """The page number to retrieve"""

    per: int
    """The number of resources to return per page.

    There is a limit of 50 results per page.
    """
