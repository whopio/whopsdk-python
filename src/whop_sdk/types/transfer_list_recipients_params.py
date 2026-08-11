# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransferListRecipientsParams"]


class TransferListRecipientsParams(TypedDict, total=False):
    origin_id: Required[str]
    """
    The account sending the money: a company account ID (`biz_`), or a user ID
    (`user_`) for that user's own personal balance.
    """

    after: str
    """Cursor to fetch the page after (from page_info.end_cursor)."""

    first: int
    """Number of recipients per page.

    Search queries preserve the dashboard's 20-result maximum.
    """

    query: str
    """Search anyone on Whop by name or username, plus your own accounts by name or ID.

    Omit it to get the team around the balance, the people you follow, and your own
    accounts. The list is the same whether the balance belongs to a company or to
    you. Searching from a `biz_` origin additionally requires the member:basic:read
    scope. A credential scoped to a single company is the exception to the search
    itself: it only ever sees that company's own people. Complete email addresses
    return no matches.
    """
