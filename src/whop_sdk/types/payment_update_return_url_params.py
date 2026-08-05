# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PaymentUpdateReturnURLParams"]


class PaymentUpdateReturnURLParams(TypedDict, total=False):
    return_url: Required[str]
    """Where the buyer continues after completing an off-site step.

    Must be an absolute https URL without credentials, at most 2,048 characters.
    """
