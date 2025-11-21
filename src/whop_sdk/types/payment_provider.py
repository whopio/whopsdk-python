# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["PaymentProvider"]

PaymentProvider: TypeAlias = Literal[
    "stripe", "coinbase", "paypal", "apple", "sezzle", "splitit", "platform_balance", "multi_psp"
]
