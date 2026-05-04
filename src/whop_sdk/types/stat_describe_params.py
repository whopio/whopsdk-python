# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["StatDescribeParams"]


class StatDescribeParams(TypedDict, total=False):
    company_id: Optional[str]
    """Scope query to a specific company."""

    resource: Optional[str]
    """
    Resource path using : as separator (e.g., 'receipts', 'payments:membership',
    'receipts:gross_revenue').
    """

    user_id: Optional[str]
    """Scope query to a specific user."""
