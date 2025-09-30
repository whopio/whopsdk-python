# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["InvoiceStatus"]

InvoiceStatus: TypeAlias = Literal["open", "paid", "past_due", "void"]
