# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["CompanyCreateAPIKeyParams", "Permission"]


class CompanyCreateAPIKeyParams(TypedDict, total=False):
    child_company_id: Required[str]
    """The unique identifier of the connected account to create the API key for (e.g.

    'biz_xxx').
    """

    name: Optional[str]
    """A human-readable name for the API key, such as 'Production API Key'."""

    permissions: Optional[Iterable[Permission]]
    """Granular permission statements defining which actions this API key can perform.

    Either permissions or role must be provided.
    """

    role: Optional[Literal["owner", "admin", "moderator", "sales_manager", "advertiser"]]
    """The different system roles that can be assigned."""


class Permission(TypedDict, total=False):
    """Input for a single permissions statement"""

    actions: Required[SequenceNotStr[str]]
    """Actions covered by this statement"""

    grant: Required[bool]
    """Whether the actions are granted or denied"""

    resources: Required[SequenceNotStr[str]]
    """Resource identifiers.

    Can look like 'biz*xxxx' or 'biz_xxx|pass*_|exp*xxx' or 'biz_xxx|app_xxx' or
    'biz_xxx|pass_xxx|exp_xxx' or 'biz_xxx|pass_xxx' or 'biz_xxx|pass*_'
    """
