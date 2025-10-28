# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["BillingReasons"]

BillingReasons: TypeAlias = Literal[
    "subscription_create", "subscription_cycle", "subscription_update", "one_time", "manual", "subscription"
]
