# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PaymentMethodDomainCreateParams"]


class PaymentMethodDomainCreateParams(TypedDict, total=False):
    hostname: Required[str]
    """Hostname to register (e.g. `checkout.example.com`)."""

    account_id: str
    """Account to register the domain for (`biz_` tag).

    Defaults to the caller's account.
    """
