# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AccountReserve", "ByType", "UnlocksByDate"]


class ByType(BaseModel):
    """The total split by why each part is held.

    Only reasons holding a non-zero amount appear, so these can sum to less than `amount`, never more.
    """

    amount: str
    """Amount held for this reason, in native units, as a decimal string."""

    hold_period_days: Optional[int] = None
    """
    Days money is currently held for this reason before it unlocks, or `null` when
    release depends on something other than time. Money already held keeps the terms
    it was taken under.
    """

    percentage: Optional[float] = None
    """
    Percentage of each incoming payment currently held for this reason, or `null`
    when the reason is not a percentage of anything. Money already held keeps the
    release date it was given, which `unlocks_by_date` reflects.
    """

    type: Literal["regular", "bnpl", "sequra", "fraud_hold", "preshipment_hold"]
    """Why this part of the balance is held.

    `regular` is the account's standing risk reserve; `bnpl` and `sequra` cover
    buy-now-pay-later settlement; `preshipment_hold` covers a physical order that
    has not shipped yet; `fraud_hold` is held while activity is reviewed.
    """


class UnlocksByDate(BaseModel):
    """When the held money unlocks, one entry per day, earliest first.

    Money whose release depends on something other than a date is left out, so these can sum to less than `amount`, never more.
    """

    amount: str
    """
    Amount unlocking that day across every reason, in native units, as a decimal
    string.
    """

    date: str
    """The day this money unlocks, as an ISO 8601 date."""


class AccountReserve(BaseModel):
    amount: str
    """Total held in this currency, in native units, as a decimal string.

    `usd` and `usdt` are reported as one `usd` entry, matching how the balance row
    groups them.
    """

    by_type: List[ByType]

    currency: str
    """Lowercase ISO currency code, such as `usd` or `eur`."""

    unlocks_by_date: List[UnlocksByDate]
