# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExperienceListParams"]


class ExperienceListParams(TypedDict, total=False):
    account_id: Required[str]
    """The unique identifier of the company to list experiences for."""

    after: str
    """Returns the elements in the list that come after the specified cursor."""

    app_id: str
    """Filter to only experiences powered by this app identifier."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return experiences created after this timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return experiences created before this timestamp."""

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""

    product_id: str
    """Filter to only experiences attached to this product identifier."""
