# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AccountRegisterLlcResponse"]


class AccountRegisterLlcResponse(BaseModel):
    checkout_session_id: str
    """Checkout session ID, prefixed `ch_`."""

    checkout_url: str
    """Hosted checkout URL.

    Send the buyer here to pay for the formation; the filing is submitted once
    payment completes.
    """

    currency: str
    """Always `usd`."""

    total: int
    """Total due at checkout in USD cents."""
