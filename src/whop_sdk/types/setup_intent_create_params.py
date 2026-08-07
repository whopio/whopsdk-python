# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .shared.currency import Currency

__all__ = [
    "SetupIntentCreateParams",
    "CreateSetupIntentInputWithConfirmationToken",
    "CreateSetupIntentInputWithPaymentMethodID",
]


class CreateSetupIntentInputWithConfirmationToken(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to save the payment method for."""

    confirmation_token: Required[str]
    """
    A confirmation token ID (ctok\\__) describing a payment method the buyer just
    supplied. Provide this or payment_method_id, not both.
    """

    currency: Optional[Currency]
    """The available currencies on the platform"""

    email: Optional[str]
    """
    Overrides the buyer email carried on the confirmation token, resolving or
    creating the Whop user the method belongs to. Ignored when the caller IS the
    buyer or the confirmation token was created by a signed-in buyer, and unless
    confirmation_token is provided.
    """

    metadata: Optional[Dict[str, object]]
    """Custom metadata to attach to the setup intent."""

    return_url: Optional[str]
    """Where the buyer continues after completing an off-site step.

    Must be an absolute https URL without credentials, at most 2,048 characters.
    """


class CreateSetupIntentInputWithPaymentMethodID(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to save the payment method for."""

    payment_method_id: Required[str]
    """An existing payment method (payt\\__) to re-verify and save.

    Provide this or confirmation_token, not both.
    """

    currency: Optional[Currency]
    """The available currencies on the platform"""

    email: Optional[str]
    """
    Overrides the buyer email carried on the confirmation token, resolving or
    creating the Whop user the method belongs to. Ignored when the caller IS the
    buyer or the confirmation token was created by a signed-in buyer, and unless
    confirmation_token is provided.
    """

    metadata: Optional[Dict[str, object]]
    """Custom metadata to attach to the setup intent."""

    return_url: Optional[str]
    """Where the buyer continues after completing an off-site step.

    Must be an absolute https URL without credentials, at most 2,048 characters.
    """


SetupIntentCreateParams: TypeAlias = Union[
    CreateSetupIntentInputWithConfirmationToken, CreateSetupIntentInputWithPaymentMethodID
]
