# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["RefundStatus"]

RefundStatus: TypeAlias = Literal["pending", "requires_action", "succeeded", "failed", "canceled"]
