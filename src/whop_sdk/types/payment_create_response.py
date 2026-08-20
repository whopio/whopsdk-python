# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .shared.payment import Payment

__all__ = ["PaymentCreateResponse"]


class PaymentCreateResponse(Payment):
    """A payment represents a completed or attempted charge.

    Payments track the amount, status, currency, and payment method used.
    """

    client_secret: Optional[str] = None
    """
    The credential the buyer's surface presents to poll this payment and set its
    return URL. Returned when a payment created from a confirmation token is created
    or retrieved by a caller with the payment:charge permission. Null for payments
    created from a stored payment method or callers without payment:charge. It
    unlocks this payment and nothing else; treat it like a password for that one
    attempt.
    """
