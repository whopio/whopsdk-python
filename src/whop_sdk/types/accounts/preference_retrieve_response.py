# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "PreferenceRetrieveResponse",
    "AdsAgreement",
    "AdsPaymentMethods",
    "AdsPaymentMethodsBackup",
    "AdsPaymentMethodsPrimary",
    "AdsTripleWhaleIntegration",
]


class AdsAgreement(BaseModel):
    """The account's Whop Ads services and payment authorization agreement.

    While `pending_signature`, campaign launch is blocked; sign by answering `requested_information` via `PATCH /verifications/{id}`.
    """

    accepted_at: Optional[str] = None
    """When the agreement was signed, as an ISO 8601 timestamp. `null` until signed."""

    agreement_version: Optional[str] = None
    """The agreement version signed or awaiting signature, as an ISO date.

    `null` when no signature is required.
    """

    printed_name: Optional[str] = None
    """The signer's printed full name. `null` until signed."""

    status: Literal["not_required", "pending_signature", "signed"]
    """Where the account's ads services agreement stands."""


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
    Balance name, present for account `platform_balance` entries (null for a
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
    Balance name, present for account `platform_balance` entries (null for a
    personal balance).
    """


class AdsPaymentMethods(BaseModel):
    """How the account pays for Whop Ads spend.

    `primary` is charged first; `backup` covers the charge when the primary fails. `null` until ads billing has been configured.
    """

    backup: Optional[AdsPaymentMethodsBackup] = None

    primary: Optional[AdsPaymentMethodsPrimary] = None


class AdsTripleWhaleIntegration(BaseModel):
    """
    The account's Triple Whale integration, which pushes Whop ad spend to Triple Whale's Data-In API so it reports as a `whop` channel.
    """

    masked_api_key: Optional[str] = None
    """The leading characters of the stored Data-In API key, followed by asterisks.

    The full key is never returned. `null` when no key is stored.
    """

    shop_domain: Optional[str] = None
    """
    The connected Shopify store domain spend is reported for, such as
    `acme.myshopify.com`. `null` when no store is connected.
    """

    status: Literal["connected", "not_connected", "requires_shopify_store"]
    """Where the integration stands.

    `requires_shopify_store` means no Shopify store is connected — Triple Whale keys
    records by Shopify shop, so no spend is reported until one is.
    """


class PreferenceRetrieveResponse(BaseModel):
    ads_agreement: AdsAgreement
    """The account's Whop Ads services and payment authorization agreement.

    While `pending_signature`, campaign launch is blocked; sign by answering
    `requested_information` via `PATCH /verifications/{id}`.
    """

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

    ads_triple_whale_integration: AdsTripleWhaleIntegration
    """
    The account's Triple Whale integration, which pushes Whop ad spend to Triple
    Whale's Data-In API so it reports as a `whop` channel.
    """

    cards_auto_top_up: bool
    """Whether incoming funds are automatically moved to the account's cards balance.

    `false` when the account has no cards balance.
    """

    dispute_fighter_enabled: bool
    """
    Whether Whop assembles and files the evidence response when this account's
    payments are disputed. Off by default; enabling it also opts the account into
    the success fee charged only on disputes it wins.
    """
