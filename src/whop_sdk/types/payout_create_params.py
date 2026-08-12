# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PayoutCreateParams"]


class PayoutCreateParams(TypedDict, total=False):
    amount: Required[float]
    """The amount to pay out in the specified currency."""

    payout_method_id: Required[str]
    """The saved payout method to deliver to (a potk\\__ identifier)."""

    account_id: str
    """Account to pay out from, prefixed `biz_`.

    Provide exactly one of `account_id` or `user_id`.
    """

    acknowledge_bank_warning: bool
    """
    Set to `true` to continue when the destination bank could not confirm the payout
    method account holder's name. Defaults to `false`; when this warning applies,
    the payout is refused so the account holder can correct the name or link their
    bank first.
    """

    currency: str
    """The currency to pay out.

    Balances are held per currency and the payout draws only from the balance in
    this currency, so match the currency the funds arrived in — for example `cad`
    for an account funded by CAD transfers. Defaults to `usd`.
    """

    api_idempotency_key: Annotated[Optional[str], PropertyInfo(alias="idempotency_key")]
    """A unique key that makes retries safe.

    Retrying with the same key returns the original payout instead of paying out
    twice. Also accepted as the `Idempotency-Key` header.
    """

    notes: Optional[str]
    """Free-form notes to attach to the payout, with a maximum of 255 characters.

    Omit or pass `null` for no notes.
    """

    platform_covers_fees: bool
    """
    Whether the parent platform covers the payout fee instead of the account being
    paid out. Omit to use the platform's configured fee coverage policy; pass
    `false` to opt out of it. `true` is only accepted for accounts that belong to a
    platform, and requires the platform's policy to cover this payout method's
    category or a caller authorized to manage the platform's child account fees.
    """

    speed: Literal["standard", "instant"]
    """How fast the funds should arrive.

    `instant` is only accepted when the account and payout method are eligible;
    otherwise the payout is rejected.
    """

    user_id: str
    """User to pay out from, prefixed `user_`.

    Provide exactly one of `account_id` or `user_id`.
    """
