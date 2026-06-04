# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IdentityProfileAttachParams"]


class IdentityProfileAttachParams(TypedDict, total=False):
    ledger_account_id: Required[str]
    """The ID of the LedgerAccount to attach the identity profile to."""
