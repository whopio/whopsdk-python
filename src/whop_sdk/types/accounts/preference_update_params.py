# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PreferenceUpdateParams", "AdsPaymentMethods", "AdsPaymentMethodsPrimary", "AdsPaymentMethodsBackup"]


class PreferenceUpdateParams(TypedDict, total=False):
    ads_payment_methods: AdsPaymentMethods
    """How the account pays for Whop Ads spend.

    `primary` is charged first; `backup` covers the charge when the primary fails.
    """

    ads_reporting_currency: str
    """
    Lowercase ISO currency code, such as `usd` or `eur`, used to display ad spend
    and stats. Defaults to `usd`.
    """

    ads_scheduling_timezone: str
    """IANA timezone (e.g.

    `America/New_York`) used to interpret campaign start/end times and to bucket
    reports. Cannot be cleared once set — pass a new value to change it.
    """


class AdsPaymentMethodsPrimary(TypedDict, total=False):
    type: Required[Literal["platform_balance", "card"]]
    """The funding source kind."""

    id: str
    """
    The funding source ID: a Whop balance (`ldgr_`) for `platform_balance`, or a
    payment method (`payt_`) for `card`. Optional for `platform_balance` — defaults
    to the account's default Whop balance. Required for `card`.
    """


class AdsPaymentMethodsBackup(TypedDict, total=False):
    """Optional second method charged if the primary fails.

    Any pairing is allowed (two cards, card+balance, balance+card); omit it to run on a single method. Must differ from the primary.
    """

    type: Required[Literal["platform_balance", "card"]]
    """The funding source kind."""

    id: str
    """
    The funding source ID: a Whop balance (`ldgr_`) for `platform_balance`, or a
    payment method (`payt_`) for `card`. Optional for `platform_balance` — defaults
    to the account's default Whop balance. Required for `card`.
    """


class AdsPaymentMethods(TypedDict, total=False):
    """How the account pays for Whop Ads spend.

    `primary` is charged first; `backup` covers the charge when the primary fails.
    """

    primary: Required[AdsPaymentMethodsPrimary]

    backup: AdsPaymentMethodsBackup
    """Optional second method charged if the primary fails.

    Any pairing is allowed (two cards, card+balance, balance+card); omit it to run
    on a single method. Must differ from the primary.
    """
