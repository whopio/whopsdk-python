# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared.currency import Currency
from .withdrawal_speeds import WithdrawalSpeeds

__all__ = ["WithdrawalCreateParams"]


class WithdrawalCreateParams(TypedDict, total=False):
    amount: Required[float]
    """The amount to withdraw in the specified currency"""

    company_id: Required[str]
    """The ID of the company to withdraw from."""

    currency: Required[Currency]
    """The currency that is being withdrawn."""

    acknowledge_bank_warning: Optional[bool]
    """
    Set to true to continue when the bank could not confirm the account holder's
    name. The withdrawal is refused without it so the creator can fix the account or
    link their bank first.
    """

    idempotency_key: Optional[str]
    """A client-generated key that makes retries safe.

    Retrying with the same key returns the original withdrawal instead of creating a
    second one.
    """

    payout_method_id: Optional[str]
    """The ID of the payout method to use for the withdrawal."""

    platform_covers_fees: Optional[bool]
    """Whether the platform covers the payout fees."""

    speed: Optional[WithdrawalSpeeds]
    """The different speeds of withdrawals"""

    statement_descriptor: Optional[str]
    """Custom statement descriptor for the withdrawal.

    Must be between 5 and 22 characters and contain only alphanumeric characters.
    """
