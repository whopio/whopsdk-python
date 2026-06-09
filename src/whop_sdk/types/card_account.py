# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardAccount"]


class CardAccount(BaseModel):
    auto_topup_enabled: bool
    """Whether auto-topup is enabled."""

    object: Literal["card_account"]

    auto_topup_target_usd: Optional[str] = None
    """Target balance (USD) to top up to."""

    auto_topup_threshold_usd: Optional[str] = None
    """Balance threshold (USD) that triggers an auto-topup."""
