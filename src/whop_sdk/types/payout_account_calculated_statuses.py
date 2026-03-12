# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["PayoutAccountCalculatedStatuses"]

PayoutAccountCalculatedStatuses: TypeAlias = Literal[
    "connected", "disabled", "action_required", "pending_verification", "verification_failed", "not_started"
]
