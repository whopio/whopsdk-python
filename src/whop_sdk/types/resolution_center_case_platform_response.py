# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ResolutionCenterCasePlatformResponse"]

ResolutionCenterCasePlatformResponse: TypeAlias = Literal[
    "request_buyer_info", "request_merchant_info", "merchant_wins", "platform_refund", "merchant_refund"
]
