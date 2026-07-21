# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

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
    """The payout currency. Defaults to usd."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
