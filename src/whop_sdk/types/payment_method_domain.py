# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentMethodDomain"]


class PaymentMethodDomain(BaseModel):
    id: str
    """Payment method domain ID, prefixed `pmd_`."""

    account_id: Optional[str] = None
    """ID of the account the domain is registered for, prefixed `biz_`."""

    created_at: str
    """When the domain was created, as an ISO 8601 timestamp."""

    hostname: str
    """Hostname the checkout is served from (e.g. `checkout.example.com`)."""

    provider: Literal["apple"]
    """Wallet provider the domain is registered with."""

    status: Literal["pending", "verified"]
    """Verification status.

    `pending` means the provider could not fetch the domain-association file yet;
    only `verified` domains show wallet payment methods at checkout.
    """

    updated_at: str
    """When the domain was last updated, as an ISO 8601 timestamp."""
