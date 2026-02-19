# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .company_token_transaction_type import CompanyTokenTransactionType

__all__ = ["CompanyTokenTransactionListParams"]


class CompanyTokenTransactionListParams(TypedDict, total=False):
    company_id: Required[str]
    """The unique identifier of the company to list token transactions for."""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    transaction_type: Optional[CompanyTokenTransactionType]
    """The type of token transaction"""

    user_id: Optional[str]
    """Filter transactions to only those involving this specific user."""
