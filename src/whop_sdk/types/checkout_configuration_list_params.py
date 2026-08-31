# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CheckoutConfigurationListParams"]


class CheckoutConfigurationListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID, prefixed `biz_`."""

    after: str
    """Cursor for the next page of results."""

    created_after: str
    """Only return checkout configurations created after this ISO 8601 timestamp."""

    created_before: str
    """Only return checkout configurations created before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction. Defaults to `desc`."""

    first: int
    """Number of checkout configurations to return."""

    order: Literal["created_at"]
    """Field used to sort checkout configurations."""

    plan_id: str
    """Only return checkout configurations for this plan ID, prefixed `plan_`."""

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
