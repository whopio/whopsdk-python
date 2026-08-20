# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "PreferenceUpdateParams",
    "AdsPaymentMethods",
    "AdsPaymentMethodsPrimary",
    "AdsPaymentMethodsBackup",
    "AdsTripleWhaleIntegration",
]


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

    ads_triple_whale_integration: AdsTripleWhaleIntegration
    """Connects or disconnects the Triple Whale integration.

    Requires a connected Shopify store, since Triple Whale keys spend records by
    Shopify shop.
    """

    cards_auto_top_up: bool
    """Whether incoming funds are automatically moved to the account's cards balance.

    Requires a cards balance on the account.
    """

    dispute_fighter_enabled: bool
    """
    Whether Whop assembles and files the evidence response when this account's
    payments are disputed. Off by default; enabling it also opts the account into
    the success fee charged only on disputes it wins.
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


class AdsTripleWhaleIntegration(TypedDict, total=False):
    """Connects or disconnects the Triple Whale integration.

    Requires a connected Shopify store, since Triple Whale keys spend records by Shopify shop.
    """

    api_key: Required[Optional[str]]
    """
    A Triple Whale Data-In API key with the `Data-In Write: Ads` scope, validated
    against Triple Whale before it is stored. Pass `null` to disconnect. Connecting
    for the first time backfills the account's existing ad spend.
    """
