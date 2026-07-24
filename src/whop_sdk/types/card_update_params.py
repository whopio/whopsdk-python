# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CardUpdateParams", "Billing"]


class CardUpdateParams(TypedDict, total=False):
    account_id: str
    """The owning account ID (a biz\\__ identifier). Provide this or user_id."""

    billing: Billing
    """New billing address.

    Requires line1, city, region, postal_code, and country_code. On an invited card,
    passing billing alone (as the invited user) completes onboarding and starts card
    provisioning.
    """

    canceled: bool
    """Pass `true` to permanently cancel the card.

    A canceled card cannot be uncanceled. Cannot be combined with other fields.
    """

    frozen: bool
    """Pass `true` to freeze the card, `false` to unfreeze it."""

    name: str
    """A display name for the card."""

    pin: str
    """New 4-digit PIN. Can only be set on a card assigned to the acting user."""

    remove_limit: bool
    """Pass `true` to remove the spending limit (make the card unlimited)."""

    spend_limit: float
    """Spending limit amount, in dollars."""

    spend_limit_frequency: Literal["daily", "weekly", "monthly", "one_time"]
    """The spending limit window."""

    transaction_limit: float
    """Per-transaction limit amount, in dollars."""

    user_id: str
    """The owning user ID (a user\\__ identifier). Provide this or account_id."""


class Billing(TypedDict, total=False):
    """New billing address.

    Requires line1, city, region, postal_code, and country_code. On an invited card, passing billing alone (as the invited user) completes onboarding and starts card provisioning.
    """

    city: Required[str]
    """Billing city."""

    country_code: Required[str]
    """Billing country code, ISO 3166-1 alpha-2."""

    line1: Required[str]
    """Street address line 1."""

    postal_code: Required[str]
    """Billing postal code."""

    region: Required[str]
    """Billing region or state."""

    line2: str
    """Street address line 2."""
