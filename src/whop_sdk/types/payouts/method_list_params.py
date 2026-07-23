# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MethodListParams"]


class MethodListParams(TypedDict, total=False):
    account_id: str
    """The owning account ID (a biz\\__ identifier). Provide this or user_id."""

    after: str
    """Cursor to fetch the page after (from page_info.end_cursor)."""

    amount: float
    """Optional withdrawal amount in whole currency units, for example `250.00`.

    When provided, each method includes a quote with the estimated fee, amount
    received, and delivery date for that amount.
    """

    before: str
    """Cursor to fetch the page before (from page_info.start_cursor)."""

    currency: str
    """Currency code of the amount, for example `usd`. Only meaningful with amount."""

    destination_currency: str
    """Currency the destination would deliver payouts in.

    Only meaningful with destination_id; required fields vary by destination
    currency.
    """

    destination_id: str
    """
    Narrows available*destinations to this one destination (a pd* identifier from a
    previous listing) and includes its required_fields — the values to collect to
    add it as a payout method. Implies include_available.
    """

    first: int
    """Number of payout methods to return from the start of the window."""

    include_available: bool
    """
    When true, the response also carries available_destinations — payout rails the
    account could add as a new payout method, with per-currency quotes when an
    amount is provided.
    """

    last: int
    """Number of payout methods to return from the end of the window."""

    status: Literal["created", "active", "broken"]
    """Optional status filter.

    `created` means saved but unused, `active` means a payout through it succeeded,
    `broken` means the last payout failed and the method needs fixing.
    """

    user_id: str
    """The owning user ID (a user\\__ identifier). Provide this or account_id."""
