# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentCreateParams"]


class PaymentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account to charge for, prefixed `biz_`."""

    plan_id: Required[str]
    """The plan to charge for, prefixed `plan_`. It must belong to the account."""

    capture: Optional[bool]
    """Whether to capture a card payment immediately.

    Defaults to true. Pass false to place an authorization hold that must be
    captured in full within five days via the capture endpoint.
    """

    confirmation_token: Optional[str]
    """A confirmation token describing a payment method the buyer just supplied.

    Provide this instead of `member_id` and `payment_method_id`; the buyer is
    resolved from the token's billing email, or from `email`. The buyer may still
    have a step to complete — poll the payment's status for what to do next.
    """

    email: Optional[str]
    """
    Overrides the buyer email carried on the confirmation token, resolving or
    creating the user the payment belongs to. Ignored unless `confirmation_token` is
    provided, and when the token was created by a signed-in buyer.
    """

    member_id: Optional[str]
    """The member to charge, prefixed `mber_`.

    Required with `payment_method_id` unless `confirmation_token` is provided.
    """

    metadata: Optional[Dict[str, str]]
    """Custom metadata to attach to the payment."""

    payment_method_id: Optional[str]
    """The stored payment method to charge, prefixed `payt_`.

    It must belong to the member. Required unless `confirmation_token` is provided.
    """

    promo_code_id: Optional[str]
    """An active promo code to apply, prefixed `promo_`.

    It must belong to the account and be valid for the plan.
    """

    return_url: Optional[str]
    """Where the buyer continues after completing an off-site step.

    An absolute https URL without credentials, at most 2,048 characters. Ignored
    unless `confirmation_token` is provided.
    """

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
