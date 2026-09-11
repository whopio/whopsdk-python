# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["FeeMarkupType"]

FeeMarkupType: TypeAlias = Literal[
    "crypto_withdrawal_markup",
    "rtp_withdrawal_markup",
    "next_day_bank_withdrawal_markup",
    "bank_wire_withdrawal_markup",
    "digital_wallet_withdrawal_markup",
    "transfer_markup",
    "crypto_deposit_markup",
    "bank_deposit_markup",
    "crypto_swap_markup",
]
