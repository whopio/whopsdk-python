# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MembershipPauseParams"]


class MembershipPauseParams(TypedDict, total=False):
    resumes_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """When the membership should automatically resume payment collection.

    If not provided, the membership stays paused until manually resumed.
    """

    void_payments: Optional[bool]
    """
    Whether to void any outstanding past-due payments on this membership, preventing
    future collection attempts.
    """
