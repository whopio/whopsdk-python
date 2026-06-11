# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["WalletSendResponse", "Send", "SendDestination", "SendSource", "ClaimLink", "ClaimLinkSource"]


class SendDestination(BaseModel):
    account_id: str

    address: str


class SendSource(BaseModel):
    account_id: str

    address: str


class Send(BaseModel):
    """Returned when sending to a recipient (`to`)."""

    amount: str

    currency: str

    destination: SendDestination

    object: Literal["send"]

    source: SendSource

    tx_hash: str


class ClaimLinkSource(BaseModel):
    account_id: str


class ClaimLink(BaseModel):
    """Returned when creating a claim link (`link: true`)."""

    id: str

    amount: str
    """Per-claim amount; a multi-claim link debits amount × redeemable_count."""

    claim_url: str
    """Shareable URL anyone can open to claim the funds."""

    currency: str

    expires_at: Optional[datetime] = None

    object: Literal["claim_link"]

    redeemable_count: int

    source: ClaimLinkSource

    status: str


WalletSendResponse: TypeAlias = Union[Send, ClaimLink]
