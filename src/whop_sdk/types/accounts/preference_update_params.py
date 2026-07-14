# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PreferenceUpdateParams", "AdsPaymentMethods", "AdsPaymentMethodsPrimary", "AdsPaymentMethodsBackup"]


class PreferenceUpdateParams(TypedDict, total=False):
    ads_payment_methods: AdsPaymentMethods
    """How the account pays for Whop Ads spend.

    `primary` is charged first; `backup` covers the charge when the primary fails.
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
    """
    Optional when the primary is `platform_balance`; omitting it removes any configured card. Required (as `platform_balance`) when the primary is `card`.
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
    """
    Optional when the primary is `platform_balance`; omitting it removes any
    configured card. Required (as `platform_balance`) when the primary is `card`.
    """
