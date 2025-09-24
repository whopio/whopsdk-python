# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["InvoiceCreateParams", "Plan", "PlanCustomField", "PlanReleaseMethodSettings", "AccessPass"]


class InvoiceCreateParams(TypedDict, total=False):
    collection_method: Required[Literal["send_invoice", "charge_automatically"]]
    """The method of collection for this invoice.

    If using charge_automatically, you must provide a payment_token.
    """

    due_date: Required[int]
    """The date the invoice is due, if applicable."""

    plan: Required[Plan]
    """The properties of the plan to create for this invoice."""

    access_pass: Optional[AccessPass]
    """The properties of the access pass to create for this invoice.

    Include this if you want to create an invoice for a new product.
    """

    access_pass_id: Optional[str]
    """The access pass ID to create this invoice for.

    Include this if you want to create an invoice for an existing product.
    """

    charge_buyer_fee: Optional[bool]
    """Whether or not to charge the customer a buyer fee."""

    client_mutation_id: Optional[str]
    """A unique identifier for the client performing the mutation."""

    customer_name: Optional[str]
    """The name of the customer to create this invoice for.

    This is required if you want to create an invoice for a customer who does not
    have a member of your company yet.
    """

    email_address: Optional[str]
    """The email address to create this invoice for.

    This is required if you want to create an invoice for a user who does not have a
    member of your company yet.
    """

    member_id: Optional[str]
    """The member ID to create this invoice for.

    Include this if you want to create an invoice for an existing member. If you do
    not have a member ID, you must provide an email_address and customer_name.
    """

    payment_token_id: Optional[str]
    """The payment token ID to use for this invoice.

    If using charge_automatically, you must provide a payment_token.
    """


class PlanCustomField(TypedDict, total=False):
    field_type: Required[Literal["text"]]
    """The type of the custom field."""

    name: Required[str]
    """The name of the custom field."""

    id: Optional[str]
    """The ID of the custom field (if being updated)"""

    order: Optional[int]
    """The order of the field."""

    placeholder: Optional[str]
    """The placeholder value of the field."""

    required: Optional[bool]
    """Whether or not the field is required."""


class PlanReleaseMethodSettings(TypedDict, total=False):
    expires_at: Optional[int]
    """When the raffle will expire"""

    max_entries: Optional[int]
    """The maximum number of entries allowed for the raffle or waitlist"""

    nft_weighted_entries: Optional[bool]
    """
    If this is enabled, the raffle will get entries based off of how many NFTs the
    user owns
    """

    starts_at: Optional[int]
    """When the raffle will start"""


class Plan(TypedDict, total=False):
    ach_payments: Optional[bool]
    """Whether or not ACH payments are accepted"""

    base_currency: Optional[
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
        ]
    ]
    """The respective currency identifier for the plan."""

    billing_period: Optional[int]
    """The interval at which the plan charges (renewal plans)."""

    card_payments: Optional[bool]
    """Whether or not card payments are accepted"""

    coinbase_commerce_accepted: Optional[bool]
    """Marks whether coinbase commerce payments are/aren't accepted."""

    custom_fields: Optional[Iterable[PlanCustomField]]
    """An array of custom field objects."""

    description: Optional[str]
    """The description of the plan."""

    expiration_days: Optional[int]
    """The interval at which the plan charges (expiration plans)."""

    initial_price: Optional[float]
    """An additional amount charged upon first purchase."""

    internal_notes: Optional[str]
    """A personal description or notes section for the business."""

    offer_cancel_discount: Optional[bool]
    """Whether or not to offer a discount to cancel a subscription."""

    paypal_accepted: Optional[bool]
    """Marks whether paypal payments are/aren't accepted."""

    plan_type: Optional[Literal["renewal", "one_time"]]
    """Indicates if the plan is a one time payment or recurring."""

    platform_balance_accepted: Optional[bool]
    """Marks whether platform balance payments are/aren't accepted."""

    redirect_url: Optional[str]
    """The URL to redirect the customer to after purchase."""

    release_method: Optional[Literal["buy_now", "waitlist", "raffle"]]
    """This is the release method the business uses to sell this plan."""

    release_method_settings: Optional[PlanReleaseMethodSettings]
    """Configurable settings on how this plan is released."""

    renewal_price: Optional[float]
    """The amount the customer is charged every billing period."""

    split_pay_required_payments: Optional[int]
    """The number of payments required before pausing the subscription."""

    splitit_accepted: Optional[bool]
    """
    Marks whether payments using splitit, a payment processor, are/aren't accepted
    for the plan.
    """

    stock: Optional[int]
    """The number of units available for purchase."""

    trial_period_days: Optional[int]
    """The number of free trial days added before a renewal plan."""

    unlimited_stock: Optional[bool]
    """Limits/doesn't limit the number of units available for purchase."""

    visibility: Optional[Literal["visible", "hidden", "archived", "quick_link"]]
    """Shows or hides the plan from public/business view."""


class AccessPass(TypedDict, total=False):
    title: Required[str]
    """The title of the access pass."""

    product_tax_code_id: Optional[str]
    """The ID of the product tax code to apply to this access pass."""
