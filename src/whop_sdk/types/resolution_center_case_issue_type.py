# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ResolutionCenterCaseIssueType"]

ResolutionCenterCaseIssueType: TypeAlias = Literal[
    "forgot_to_cancel",
    "item_not_received",
    "significantly_not_as_described",
    "unauthorized_transaction",
    "product_unacceptable",
]
