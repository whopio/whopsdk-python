# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["InvoiceVoidParams"]


class InvoiceVoidParams(TypedDict, total=False):
    client_mutation_id: Optional[str]
    """A unique identifier for the client performing the mutation."""
