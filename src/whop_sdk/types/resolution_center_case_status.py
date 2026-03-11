# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ResolutionCenterCaseStatus"]

ResolutionCenterCaseStatus: TypeAlias = Literal[
    "merchant_response_needed",
    "customer_response_needed",
    "merchant_info_needed",
    "customer_info_needed",
    "under_platform_review",
    "customer_won",
    "merchant_won",
    "customer_withdrew",
]
