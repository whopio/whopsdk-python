# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WalletSendParams"]


class WalletSendParams(TypedDict, total=False):
    account_id: Required[str]
    """The sending account ID."""

    amount: Required[str]
    """USDT amount to send — or the per-claim USD amount when link is true."""

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Claim-link expiry as an ISO 8601 timestamp (link mode only).

    Defaults to 24 hours from creation.
    """

    link: bool
    """When true, creates a claim link instead of sending to a recipient.

    Mutually exclusive with to. Requires the airdrop_link:manage scope.
    """

    redeemable_count: int
    """How many different users can claim the link (link mode only). Defaults to 1."""

    to: str
    """Recipient user ID, business account ID, ledger account ID, or email.

    Omit when link is true.
    """
