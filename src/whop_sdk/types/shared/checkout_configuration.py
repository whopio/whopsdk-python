# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CheckoutConfiguration"]


class CheckoutConfiguration(BaseModel):
    id: str

    account_id: str
    """Account ID, prefixed `biz_`."""

    affiliate_code: Optional[str] = None
    """Affiliate code applied at checkout, or `null` when none is set."""

    created_at: str
    """When the checkout configuration was created, as an ISO 8601 timestamp."""

    currency: Optional[str] = None
    """
    Currency used for setup-mode payment method availability; defaults to `usd` when
    omitted.
    """

    metadata: Optional[object] = None
    """Custom key-value metadata copied to payments and memberships.

    `null` without the `checkout_configuration:basic:read` scope.
    """

    mode: str
    """
    Checkout mode: `payment` collects payment now; `setup` saves payment details for
    later.
    """

    payment_method_configuration: Optional[object] = None
    """Payment method overrides for this checkout.

    `null` when it uses the plan or platform defaults.
    """

    plan: Optional[object] = None
    """Plan used for payment checkout. `null` in setup mode."""

    purchase_url: Optional[str] = None
    """Checkout URL you can send to customers."""

    redirect_url: Optional[str] = None
    """
    URL customers are sent to after checkout, or `null` when no redirect is
    configured.
    """

    three_ds_level: Optional[str] = None
    """3D Secure behavior for this checkout, or `null` to use the account default."""

    updated_at: str
    """When the checkout configuration was last updated, as an ISO 8601 timestamp."""
