# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SupportedMethodListParams"]


class SupportedMethodListParams(TypedDict, total=False):
    account_id: str
    """The owning account ID (a biz\\__ identifier). Provide this or user_id."""

    after: str
    """Cursor to fetch the page after (from page_info.end_cursor)."""

    amount: float
    """Optional withdrawal amount in whole currency units, for example `250.00`.

    When provided, each destination includes per-currency fee and delivery quotes.
    """

    before: str
    """Cursor to fetch the page before (from page_info.start_cursor)."""

    country: str
    """ISO 3166-1 alpha-2 country code for the bank account or wallet, such as `US`.

    Defaults to the payout account's country.
    """

    currency: str
    """Currency code of the amount, for example `usd`. Only meaningful with amount."""

    destination_currency: str
    """Currency the supported payout method would deliver payouts in.

    Only meaningful with supported_payout_method_id; required fields vary by
    destination currency.
    """

    first: int
    """Number of supported payout methods to return from the start of the window."""

    last: int
    """Number of supported payout methods to return from the end of the window."""

    supported_payout_method_id: str
    """
    Narrows the list to one supported payout method (a podst\\__ identifier) and
    includes the required_fields needed to save it as a payout method.
    """

    user_id: str
    """The owning user ID (a user\\__ identifier). Provide this or account_id."""
