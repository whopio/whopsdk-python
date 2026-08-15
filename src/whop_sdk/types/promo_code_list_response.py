# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PromoCodeListResponse", "Product"]


class Product(BaseModel):
    """
    Product the promo code is restricted to, or `null` when it is not product-scoped.
    """

    id: str
    """Product ID, prefixed `prod_`."""

    title: str
    """Product display name."""


class PromoCodeListResponse(BaseModel):
    id: str
    """Promo code ID, prefixed `promo_`."""

    amount_off: float
    """Discount amount. Percentage discounts are represented as a decimal fraction."""

    churned_users_only: bool
    """Whether the promo code is restricted to churned customers."""

    code: Optional[str] = None
    """Code entered at checkout."""

    created_at: str
    """When the promo code was created, as an ISO 8601 timestamp."""

    currency: Literal[
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
    """Currency used for a fixed-amount discount."""

    duration: Literal["forever", "once", "repeating"]
    """How long the discount applies."""

    existing_memberships_only: bool
    """Whether the promo code applies only to existing memberships."""

    expires_at: Optional[str] = None
    """When the promo code expires, as an ISO 8601 timestamp."""

    metadata: object
    """Custom key-value metadata stored on the promo code."""

    new_users_only: bool
    """Whether the promo code is restricted to new customers."""

    one_per_customer: bool
    """Whether each customer may redeem the promo code only once."""

    product: Optional[Product] = None
    """
    Product the promo code is restricted to, or `null` when it is not
    product-scoped.
    """

    promo_duration_months: Optional[int] = None
    """Billing intervals the discount applies to."""

    promo_type: Literal["percentage", "flat_amount"]
    """Whether the discount is percentage-based or a fixed amount."""

    status: Literal["active", "inactive", "archived"]
    """Promo code lifecycle status."""

    stock: int
    """Maximum uses when stock is limited."""

    unlimited_stock: bool
    """Whether the promo code has no redemption limit."""

    updated_at: str
    """When the promo code was updated, as an ISO 8601 timestamp."""

    uses: int
    """Memberships that used the promo code."""
