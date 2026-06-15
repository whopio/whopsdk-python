# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProductCreateParams"]


class ProductCreateParams(TypedDict, total=False):
    title: Required[str]
    """The display name of the product. Maximum 80 characters."""

    collect_shipping_address: Optional[bool]
    """Whether to collect a shipping address at checkout."""

    company_id: str
    """The unique identifier of the company to create this product for."""

    custom_cta: Optional[str]
    """The call-to-action button label."""

    custom_cta_url: Optional[str]
    """A URL the call-to-action button links to."""

    custom_statement_descriptor: Optional[str]
    """Custom bank statement descriptor. Must start with WHOP\\**."""

    description: Optional[str]
    """A written description displayed on the product page."""

    global_affiliate_percentage: Optional[float]
    """The commission rate affiliates earn."""

    global_affiliate_status: str
    """The enrollment status in the global affiliate program."""

    headline: Optional[str]
    """A short marketing headline for the product page."""

    member_affiliate_percentage: Optional[float]
    """The commission rate members earn."""

    member_affiliate_status: str
    """The enrollment status in the member affiliate program."""

    metadata: Optional[object]
    """Custom key-value pairs to store on the product."""

    product_tax_code_id: Optional[str]
    """The unique identifier of the tax classification code."""

    redirect_purchase_url: Optional[str]
    """A URL to redirect the customer to after purchase."""

    route: Optional[str]
    """The URL slug for the product's public link."""

    visibility: str
    """Whether the product is visible to customers."""
