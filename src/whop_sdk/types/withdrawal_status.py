# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WithdrawalStatus"]

WithdrawalStatus: TypeAlias = Literal[
    "requested", "awaiting_payment", "in_transit", "completed", "failed", "canceled", "denied"
]
