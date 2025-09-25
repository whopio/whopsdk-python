# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypeAlias

__all__ = ["InvoiceStatus"]

InvoiceStatus: TypeAlias = Optional[Literal["open", "paid", "past_due", "void"]]
