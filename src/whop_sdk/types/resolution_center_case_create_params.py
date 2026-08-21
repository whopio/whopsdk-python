# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResolutionCenterCaseCreateParams", "Attachment"]


class ResolutionCenterCaseCreateParams(TypedDict, total=False):
    message: Required[str]
    """The customer's explanation."""

    reason: Required[
        Literal[
            "fraudulent", "product_not_received", "not_as_described", "product_unacceptable", "subscription_canceled"
        ]
    ]
    """What went wrong. Uses the same vocabulary as `/disputes`."""

    receipt_id: Required[str]
    """The payment to open the case against (`pay_` tag)."""

    attachments: Iterable[Attachment]


class Attachment(TypedDict, total=False):
    id: str

    direct_upload_id: str
