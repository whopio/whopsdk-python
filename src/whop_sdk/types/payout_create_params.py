# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PayoutCreateParams"]


class PayoutCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account to pay out from (a biz\\__ identifier)."""

    amount: Required[float]
    """The amount to pay out in the specified currency."""

    payout_method_id: Required[str]
    """The saved payout method to deliver to (a potk\\__ identifier)."""

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

    speed: Literal["standard", "instant"]
    """How fast the funds should arrive.

    `instant` is only accepted when the account and payout method are eligible;
    otherwise the payout is rejected.
    """
