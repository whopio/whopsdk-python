# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ReceiptStatus"]

ReceiptStatus: TypeAlias = Literal["draft", "open", "paid", "pending", "uncollectible", "unresolved", "void"]
