# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .company_token_transaction_type import CompanyTokenTransactionType

__all__ = ["CompanyTokenTransactionListParams"]


class CompanyTokenTransactionListParams(TypedDict, total=False):
    company_id: Required[str]
    """The unique identifier of the company to list token transactions for."""

    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""

    transaction_type: CompanyTokenTransactionType
    """Filter transactions by type."""

    user_id: str
    """Filter transactions to only those involving this specific user."""
