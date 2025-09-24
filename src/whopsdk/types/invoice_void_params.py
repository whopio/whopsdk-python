# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["InvoiceVoidParams"]


class InvoiceVoidParams(TypedDict, total=False):
    client_mutation_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """
