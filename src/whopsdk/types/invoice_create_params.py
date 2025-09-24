# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["InvoiceCreateParams", "Plan", "PlanCustomField", "PlanReleaseMethodSettings", "AccessPass"]


class InvoiceCreateParams(TypedDict, total=False):
    collection_method: Required[Literal["send_invoice", "charge_automatically"]]
    """The method of collection for an invoice."""

    due_date: Required[int]
    """A valid timestamp in seconds, transported as an integer"""

    plan: Required[Plan]
    """The properties of the plan to create for this invoice."""

    access_pass: Optional[AccessPass]
    """The properties of the access pass to create for this invoice."""

    access_pass_id: Optional[str]
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    charge_buyer_fee: Optional[bool]
    """Represents `true` or `false` values."""

    client_mutation_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    customer_name: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    email_address: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    member_id: Optional[str]
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    payment_token_id: Optional[str]
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """


class PlanCustomField(TypedDict, total=False):
    field_type: Required[Literal["text"]]

    name: Required[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    id: Optional[str]
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    order: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    placeholder: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    required: Optional[bool]
    """Represents `true` or `false` values."""


class PlanReleaseMethodSettings(TypedDict, total=False):
    expires_at: Optional[int]
    """A valid timestamp in seconds, transported as an integer"""

    max_entries: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    nft_weighted_entries: Optional[bool]
    """Represents `true` or `false` values."""

    starts_at: Optional[int]
    """A valid timestamp in seconds, transported as an integer"""


class Plan(TypedDict, total=False):
    ach_payments: Optional[bool]
    """Represents `true` or `false` values."""

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
    """The available currencies on the platform"""

    billing_period: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    card_payments: Optional[bool]
    """Represents `true` or `false` values."""

    coinbase_commerce_accepted: Optional[bool]
    """Represents `true` or `false` values."""

    custom_fields: Optional[Iterable[PlanCustomField]]

    description: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    expiration_days: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    initial_price: Optional[float]
    """A float that can be a string"""

    internal_notes: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    offer_cancel_discount: Optional[bool]
    """Represents `true` or `false` values."""

    paypal_accepted: Optional[bool]
    """Represents `true` or `false` values."""

    plan_type: Optional[Literal["renewal", "one_time"]]
    """The type of plan that can be attached to an access pass"""

    platform_balance_accepted: Optional[bool]
    """Represents `true` or `false` values."""

    redirect_url: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    release_method: Optional[Literal["buy_now", "waitlist", "raffle"]]
    """The methods of how a plan can be released (including raffles and waitlists)."""

    release_method_settings: Optional[PlanReleaseMethodSettings]

    renewal_price: Optional[float]
    """A float that can be a string"""

    split_pay_required_payments: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    splitit_accepted: Optional[bool]
    """Represents `true` or `false` values."""

    stock: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    trial_period_days: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    unlimited_stock: Optional[bool]
    """Represents `true` or `false` values."""

    visibility: Optional[Literal["visible", "hidden", "archived", "quick_link"]]
    """Visibility of a resource"""


class AccessPass(TypedDict, total=False):
    title: Required[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    product_tax_code_id: Optional[str]
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """
