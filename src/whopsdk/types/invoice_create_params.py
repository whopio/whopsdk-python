# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "InvoiceCreateParams",
    "Plan",
    "PlanCustomField",
    "PlanReleaseMethodSettings",
    "PlanRequirements",
    "AccessPass",
]


class InvoiceCreateParams(TypedDict, total=False):
    collection_method: Required[Literal["send_invoice", "charge_automatically"]]

    due_date: Required[int]

    plan: Required[Plan]

    access_pass: Optional[AccessPass]

    access_pass_id: Optional[str]

    charge_buyer_fee: Optional[bool]

    client_mutation_id: Optional[str]

    customer_name: Optional[str]

    email_address: Optional[str]

    member_id: Optional[str]

    payment_token_id: Optional[str]


class PlanCustomField(TypedDict, total=False):
    field_type: Required[Literal["text"]]

    name: Required[str]

    id: Optional[str]

    order: Optional[int]

    placeholder: Optional[str]

    required: Optional[bool]


class PlanReleaseMethodSettings(TypedDict, total=False):
    expires_at: Optional[int]

    max_entries: Optional[int]

    nft_weighted_entries: Optional[bool]

    starts_at: Optional[int]


class PlanRequirements(TypedDict, total=False):
    custom_password: str

    email_required: Literal[True]

    ownership_of_access_passes: SequenceNotStr[str]


class Plan(TypedDict, total=False):
    ach_payments: Optional[bool]

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

    billing_period: Optional[int]

    card_payments: Optional[bool]

    coinbase_commerce_accepted: Optional[bool]

    custom_fields: Optional[Iterable[PlanCustomField]]

    description: Optional[str]

    expiration_days: Optional[int]

    initial_price: Optional[float]

    internal_notes: Optional[str]

    offer_cancel_discount: Optional[bool]

    paypal_accepted: Optional[bool]

    plan_type: Optional[Literal["renewal", "one_time"]]

    platform_balance_accepted: Optional[bool]

    redirect_url: Optional[str]

    release_method: Optional[Literal["buy_now", "waitlist", "raffle"]]

    release_method_settings: Optional[PlanReleaseMethodSettings]

    renewal_price: Optional[float]

    requirements: Optional[PlanRequirements]

    split_pay_required_payments: Optional[int]

    splitit_accepted: Optional[bool]

    stock: Optional[int]

    trial_period_days: Optional[int]

    unlimited_stock: Optional[bool]

    visibility: Optional[Literal["visible", "hidden", "archived", "quick_link"]]


class AccessPass(TypedDict, total=False):
    title: Required[str]

    product_tax_code_id: Optional[str]
