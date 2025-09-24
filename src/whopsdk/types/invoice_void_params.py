# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InvoiceVoidParams"]


class InvoiceVoidParams(TypedDict, total=False):
    body_id: Required[Annotated[str, PropertyInfo(alias="id")]]

    client_mutation_id: Optional[str]
