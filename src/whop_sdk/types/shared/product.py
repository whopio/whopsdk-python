# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Product", "DefaultPlan", "DefaultPlanInitialPrice", "DefaultPlanRenewalPrice", "GalleryImage"]


class DefaultPlanInitialPrice(BaseModel):
    """What checkout charges up front.

    `amount` is `"0.00"` when the first charge is free, such as a trial.
    """

    amount: str
    """The amount in major units, as an exact decimal string — `"10.00"` is ten
    dollars.

    A string so no float rounds it in transit.
    """

    currency: str
    """Three-letter ISO 4217 currency code, lowercase."""

    decimals: int
    """
    How many decimal places the amount CARRIES — the precision the charge itself
    runs at.
    """

    display_decimals: int
    """How many decimal places to SHOW.

    Usually equal to `decimals`, and deliberately not always: COP is charged in
    centavos but written in whole pesos, so it is `2` and `0`. Format the number in
    your own locale using this.
    """


class DefaultPlanRenewalPrice(BaseModel):
    """The recurring charge every `billing_period` days.

    `amount` is `"0.00"` for one-time plans.
    """

    amount: str
    """The amount in major units, as an exact decimal string — `"10.00"` is ten
    dollars.

    A string so no float rounds it in transit.
    """

    currency: str
    """Three-letter ISO 4217 currency code, lowercase."""

    decimals: int
    """
    How many decimal places the amount CARRIES — the precision the charge itself
    runs at.
    """

    display_decimals: int
    """How many decimal places to SHOW.

    Usually equal to `decimals`, and deliberately not always: COP is charged in
    centavos but written in whole pesos, so it is `2` and `0`. Format the number in
    your own locale using this.
    """


class DefaultPlan(BaseModel):
    """Buyable plan to show and check out with.

    The configured default when that plan is buyable, otherwise the first buyable plan in product-page order. `null` when none is buyable.
    """

    id: str
    """Plan ID, prefixed `plan_`."""

    billing_period: Optional[float] = None
    """
    Number of days between recurring charges, such as 30 for monthly or 365 for
    annual. `null` for one-time plans.
    """

    expiration_days: Optional[float] = None
    """Access duration in days for expiration-based plans.

    `null` for plans without an expiration.
    """

    initial_price: DefaultPlanInitialPrice
    """What checkout charges up front.

    `amount` is `"0.00"` when the first charge is free, such as a trial.
    """

    plan_type: Literal["renewal", "one_time"]
    """Billing model for this plan: `one_time` or `renewal`."""

    renewal_price: DefaultPlanRenewalPrice
    """The recurring charge every `billing_period` days.

    `amount` is `"0.00"` for one-time plans.
    """

    title: Optional[str] = None
    """Plan display name shown to customers. `null` if no title has been set."""

    unlimited_stock: bool
    """Whether the plan has unlimited stock."""

    visibility: Literal["visible", "hidden", "archived", "quick_link"]
    """Where this plan can be seen. `visible` plans appear on the product page."""


class GalleryImage(BaseModel):
    """Gallery images for this product, ordered by position."""

    id: str
    """Gallery image ID."""

    content_type: Optional[str] = None
    """Uploaded file MIME type, such as image/jpeg."""

    url: Optional[str] = None
    """Pre-optimized URL for rendering this image on the client."""


class Product(BaseModel):
    id: str
    """Product ID, prefixed `prod_`."""

    account: Optional[object] = None
    """Account that sells this product."""

    created_at: str
    """When the product was created, as an ISO 8601 timestamp."""

    custom_cta: Optional[
        Literal[
            "get_access",
            "join",
            "order_now",
            "shop_now",
            "call_now",
            "donate_now",
            "contact_us",
            "sign_up",
            "subscribe",
            "purchase",
            "get_offer",
            "apply_now",
            "complete_order",
        ]
    ] = None
    """Call-to-action button label shown on the product purchase page."""

    custom_cta_url: Optional[str] = None
    """URL the call-to-action button links to instead of checkout."""

    custom_statement_descriptor: Optional[str] = None
    """Custom text label on customer's bank statement."""

    default_plan: Optional[DefaultPlan] = None
    """Buyable plan to show and check out with.

    The configured default when that plan is buyable, otherwise the first buyable
    plan in product-page order. `null` when none is buyable.
    """

    description: Optional[str] = None
    """Written description displayed on the product page. `null` if none is set."""

    external_identifier: Optional[str] = None
    """External identifier stored on the product for your own reference."""

    gallery_images: List[GalleryImage]

    global_affiliate_percentage: Optional[float] = None
    """Commission rate affiliates earn through the global affiliate program."""

    global_affiliate_status: Optional[Literal["enabled", "disabled"]] = None
    """Enrollment status in the global affiliate program."""

    headline: Optional[str] = None
    """Short marketing headline displayed on product page."""

    labels: List[str]

    marketplace_status: Literal["not_available", "pending_review", "live_marketplace"]
    """Listing state on the whop.com marketplace.

    `pending_review` means submitted and awaiting review; `live_marketplace` means
    approved and discoverable.
    """

    member_affiliate_percentage: Optional[float] = None
    """Commission rate members earn through the member affiliate program."""

    member_affiliate_status: Optional[Literal["enabled", "disabled"]] = None
    """Enrollment status in the member affiliate program."""

    member_count: float
    """Active memberships for this product; 0 if public member counts are disabled."""

    metadata: Optional[object] = None
    """Custom key-value pairs stored on the product."""

    owner_user: Optional[object] = None
    """User who owns the account selling this product."""

    product_tax_code: Optional[object] = None
    """Tax classification code for this product, or `null` if no tax code is set."""

    published_reviews_count: float
    """Published customer reviews for this product."""

    route: str
    """URL slug for the product's public link."""

    title: str
    """Product display name shown to customers."""

    updated_at: str
    """When the product was last updated, as an ISO 8601 timestamp."""

    verified: bool
    """Whether the product has been verified by Whop."""

    visibility: Optional[str] = None
    """Whether the product is publicly visible, hidden, or archived."""
