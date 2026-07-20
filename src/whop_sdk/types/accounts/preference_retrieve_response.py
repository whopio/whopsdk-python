# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PreferenceRetrieveResponse", "AdsPaymentMethods", "AdsPaymentMethodsBackup", "AdsPaymentMethodsPrimary"]


class AdsPaymentMethodsBackup(BaseModel):
    id: str
    """
    The funding source ID: a Whop balance (`ldgr_`) for `platform_balance`, or a
    payment method (`payt_`) for `card`.
    """

    type: Literal["platform_balance", "card"]
    """The funding source kind: a Whop balance or a saved card."""

    card_brand: Optional[str] = None
    """Card brand, present for `card` entries."""

    exp_month: Optional[int] = None
    """Expiration month, present for `card` entries."""

    exp_year: Optional[int] = None
    """Expiration year, present for `card` entries."""

    icon_url: Optional[str] = None
    """Balance owner icon URL, present for `platform_balance` entries."""

    last4: Optional[str] = None
    """Last four digits, present for `card` entries."""

    title: Optional[str] = None
    """
    Balance name, present for company `platform_balance` entries (null for a
    personal balance).
    """


class AdsPaymentMethodsPrimary(BaseModel):
    id: str
    """
    The funding source ID: a Whop balance (`ldgr_`) for `platform_balance`, or a
    payment method (`payt_`) for `card`.
    """

    type: Literal["platform_balance", "card"]
    """The funding source kind: a Whop balance or a saved card."""

    card_brand: Optional[str] = None
    """Card brand, present for `card` entries."""

    exp_month: Optional[int] = None
    """Expiration month, present for `card` entries."""

    exp_year: Optional[int] = None
    """Expiration year, present for `card` entries."""

    icon_url: Optional[str] = None
    """Balance owner icon URL, present for `platform_balance` entries."""

    last4: Optional[str] = None
    """Last four digits, present for `card` entries."""

    title: Optional[str] = None
    """
    Balance name, present for company `platform_balance` entries (null for a
    personal balance).
    """


class AdsPaymentMethods(BaseModel):
    """How the account pays for Whop Ads spend.

    `primary` is charged first; `backup` covers the charge when the primary fails. `null` until ads billing has been configured.
    """

    backup: Optional[AdsPaymentMethodsBackup] = None

    primary: Optional[AdsPaymentMethodsPrimary] = None


class PreferenceRetrieveResponse(BaseModel):
    ads_payment_methods: Optional[AdsPaymentMethods] = None
    """How the account pays for Whop Ads spend.

    `primary` is charged first; `backup` covers the charge when the primary fails.
    `null` until ads billing has been configured.
    """

    ads_reporting_currency: str
    """
    Lowercase ISO currency code, such as `usd` or `eur`, used to display ad spend
    and stats. Defaults to `usd`.
    """

    ads_scheduling_timezone: str
    """IANA timezone (e.g.

    `America/New_York`) used to interpret campaign start/end times and to bucket
    reports. Defaults to `America/New_York` until explicitly overridden.
    """
