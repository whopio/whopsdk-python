# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["VerificationStatus"]

VerificationStatus: TypeAlias = Literal[
    "requires_input",
    "processing",
    "verified",
    "canceled",
    "created",
    "started",
    "submitted",
    "approved",
    "declined",
    "resubmission_requested",
    "expired",
    "abandoned",
    "review",
]
