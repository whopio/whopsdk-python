# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ProductCreateParams"]


class ProductCreateParams(TypedDict, total=False):
    title: Required[str]
    """The display name of the product. Maximum 80 characters."""

    account_id: str
    """The unique identifier of the account to create this product for."""

    collect_shipping_address: Optional[bool]
    """Whether to collect a shipping address at checkout."""

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
    ]
    """The call-to-action button label."""

    custom_cta_url: Optional[str]
    """A URL the call-to-action button links to."""

    custom_statement_descriptor: Optional[str]
    """Custom bank statement descriptor. Must start with WHOP\\**."""

    description: Optional[str]
    """A written description displayed on the product page."""

    global_affiliate_percentage: Optional[float]
    """The commission rate affiliates earn."""

    global_affiliate_status: Literal["enabled", "disabled"]
    """The enrollment status in the global affiliate program."""

    headline: Optional[str]
    """A short marketing headline for the product page."""

    labels: Optional[SequenceNotStr[str]]
    """Labels used to group products into collections.

    Stored lowercased and de-duplicated. Maximum 20 labels, 50 characters each.
    """

    member_affiliate_percentage: Optional[float]
    """The commission rate members earn."""

    member_affiliate_status: Literal["enabled", "disabled"]
    """The enrollment status in the member affiliate program."""

    metadata: Optional[object]
    """Custom key-value pairs to store on the product."""

    product_tax_code_id: Optional[str]
    """The unique identifier of the tax classification code.

    See the available
    [product categories](https://docs.numeral.com/essentials/product-categories).
    """

    redirect_purchase_url: Optional[str]
    """A URL to redirect the customer to after purchase."""

    route: Optional[str]
    """The URL slug for the product's public link."""

    send_welcome_message: Optional[bool]
    """
    Whether to send an automated welcome message via support chat when a user joins
    this product. Defaults to true.
    """

    visibility: str
    """Whether the product is visible to customers."""

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
