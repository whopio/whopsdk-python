# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["MemberMostRecentActions"]

MemberMostRecentActions: TypeAlias = Literal[
    "canceling",
    "churned",
    "finished_split_pay",
    "paused",
    "paid_subscriber",
    "paid_once",
    "expiring",
    "joined",
    "drafted",
    "left",
    "trialing",
    "pending_entry",
    "renewing",
    "past_due",
]
