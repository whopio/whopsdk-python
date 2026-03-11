# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AuthorizedUserDeleteParams"]


class AuthorizedUserDeleteParams(TypedDict, total=False):
    company_id: Optional[str]
    """The ID of the company the authorized user belongs to.

    Optional if the authorized user ID is provided.
    """
