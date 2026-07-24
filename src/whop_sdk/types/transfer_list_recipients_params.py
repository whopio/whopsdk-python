# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransferListRecipientsParams"]


class TransferListRecipientsParams(TypedDict, total=False):
    origin_id: Required[str]
    """The originating account ID, prefixed `biz_`."""

    after: str

    first: int
    """Number of recipients per page.

    Search queries preserve the dashboard's 20-result maximum.
    """

    query: str
    """Search users and accounts by name, username, or ID.

    Complete email addresses return no matches.
    """
