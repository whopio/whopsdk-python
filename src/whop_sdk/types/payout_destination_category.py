# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["PayoutDestinationCategory"]

PayoutDestinationCategory: TypeAlias = Literal[
    "crypto", "rtp", "next_day_bank", "bank_wire", "digital_wallet", "unknown"
]
