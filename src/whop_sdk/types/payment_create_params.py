# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentCreateParams", "Plan", "PlanProduct"]


class PaymentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account to charge for, prefixed `biz_`."""

    capture: Optional[bool]
    """Whether to capture a card payment immediately.

    Defaults to true. Pass false to place an authorization hold that must be
    captured in full within five days via the capture endpoint.
    """

    confirmation_token: Optional[str]
    """A confirmation token describing a payment method the buyer just supplied.

    Provide this instead of `member_id` and `payment_method_id`; the buyer is
    resolved from the token's billing email, or from `email`. The buyer may still
    have a step to complete — poll the payment's status for what to do next.
    """

    email: Optional[str]
    """
    Overrides the buyer email carried on the confirmation token, resolving or
    creating the user the payment belongs to. Ignored unless `confirmation_token` is
    provided, and when the token was created by a signed-in buyer.
    """

    member_id: Optional[str]
    """The member to charge, prefixed `mber_`.

    Required with `payment_method_id` unless `confirmation_token` is provided.
    """

    metadata: Optional[Dict[str, str]]
    """Custom metadata to attach to the payment."""

    payment_method_id: Optional[str]
    """The stored payment method to charge, prefixed `payt_`.

    It must belong to the member. Required unless `confirmation_token` is provided.
    """

    plan: Plan
    """Find or create a plan for this payment.

    Mutually exclusive with `plan_id`. Creating a plan requires plan:create;
    creating or updating a product requires the corresponding product permission.
    """

    plan_id: str
    """The plan to charge for, prefixed `plan_`.

    It must belong to the account. Mutually exclusive with `plan`.
    """

    promo_code_id: Optional[str]
    """An active promo code to apply, prefixed `promo_`.

    It must belong to the account and be valid for the plan.
    """

    return_url: Optional[str]
    """Where the buyer continues after completing an off-site step.

    An absolute https URL without credentials, at most 2,048 characters. Ignored
    unless `confirmation_token` is provided.
    """

    statement_descriptor: Optional[str]
    """Overrides the text on the buyer's card statement for this payment only.

    Takes precedence over the product's and account's custom descriptors, and
    changes neither. Must start with `WHOP*`, be 5-22 characters, contain at least
    one letter, and use only Latin letters, numbers, spaces, underscores, hyphens,
    or asterisks.
    """

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class PlanProduct(TypedDict, total=False):
    """Find or create a product by external identifier.

    Mutually exclusive with product_id.
    """

    external_identifier: Required[str]
    """Your unique identifier for the product."""

    title: Required[str]
    """Product title."""

    collect_shipping_address: Optional[bool]
    """Whether to collect a shipping address at checkout."""

    custom_statement_descriptor: Optional[str]
    """Custom card statement descriptor for the product, starting with WHOP\\**."""

    description: Optional[str]
    """Product description."""

    global_affiliate_percentage: Optional[float]
    """Percentage of revenue paid to global affiliates."""

    global_affiliate_status: Optional[Literal["enabled", "disabled"]]
    """Global affiliate program status."""

    headline: Optional[str]
    """Product headline."""

    product_tax_code_id: Optional[str]
    """Product tax code identifier."""

    redirect_purchase_url: Optional[str]
    """Where to redirect the buyer after purchase."""

    route: Optional[str]
    """Product route."""

    visibility: Literal["visible", "hidden", "archived", "quick_link"]
    """Product visibility. Defaults to hidden."""


class Plan(TypedDict, total=False):
    """Find or create a plan for this payment.

    Mutually exclusive with `plan_id`. Creating a plan requires plan:create; creating or updating a product requires the corresponding product permission.
    """

    currency: Required[
        Literal[
            "usd",
            "sgd",
            "inr",
            "aud",
            "brl",
            "cad",
            "dkk",
            "eur",
            "nok",
            "gbp",
            "sek",
            "chf",
            "hkd",
            "huf",
            "jpy",
            "mxn",
            "myr",
            "pln",
            "czk",
            "nzd",
            "aed",
            "eth",
            "ape",
            "cop",
            "ron",
            "thb",
            "bgn",
            "idr",
            "dop",
            "php",
            "try",
            "krw",
            "twd",
            "vnd",
            "pkr",
            "clp",
            "uyu",
            "ars",
            "zar",
            "dzd",
            "tnd",
            "mad",
            "kes",
            "kwd",
            "jod",
            "all",
            "xcd",
            "amd",
            "bsd",
            "bhd",
            "bob",
            "bam",
            "khr",
            "crc",
            "xof",
            "egp",
            "etb",
            "gmd",
            "ghs",
            "gtq",
            "gyd",
            "ils",
            "jmd",
            "mop",
            "mga",
            "mur",
            "mdl",
            "mnt",
            "nad",
            "ngn",
            "mkd",
            "omr",
            "pyg",
            "pen",
            "qar",
            "rwf",
            "sar",
            "rsd",
            "lkr",
            "tzs",
            "ttd",
            "uzs",
            "rub",
            "btc",
            "cny",
            "usdt",
            "kzt",
            "awg",
            "whop_usd",
            "xau",
        ]
    ]
    """Currency code for the plan prices."""

    application_fee_amount: Optional[float]
    """
    Application fee collected by the platform in the plan currency (5.00 means $5.00
    for USD). Must be positive and below the initial price for one-time plans or
    renewal price for recurring plans. Paid to the parent account alongside other
    processing fees; collection is capped to remaining proceeds. Applies to
    subsequent payments on recurring plans. Only valid for connected accounts with a
    parent account.
    """

    billing_period: Optional[int]
    """Recurring billing interval in days."""

    description: Optional[str]
    """Plan description."""

    expiration_days: Optional[int]
    """Days until access expires."""

    force_create_new_plan: Optional[bool]
    """Create a new plan instead of reusing a matching plan."""

    initial_price: Optional[float]
    """Additional amount charged on the first purchase, in the plan currency.

    For recurring plans without a trial, the first charge includes this amount plus
    renewal_price.
    """

    internal_notes: Optional[str]
    """Internal notes for the account."""

    plan_type: Optional[Literal["renewal", "one_time"]]
    """Billing model for the plan."""

    product: Optional[PlanProduct]
    """Find or create a product by external identifier.

    Mutually exclusive with product_id.
    """

    product_id: Optional[str]
    """Existing product ID belonging to the account, prefixed `prod_`.

    Mutually exclusive with `product`.
    """

    renewal_price: Optional[float]
    """Recurring price in the plan currency."""

    title: Optional[str]
    """Plan title."""

    trial_period_days: Optional[int]
    """Free trial days before renewal."""

    visibility: Optional[Literal["visible", "hidden", "archived", "quick_link"]]
    """Whether the plan is visible to customers."""
