# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["StatSchemaParams"]


class StatSchemaParams(TypedDict, total=False):
    resource_type: Required[Literal["wallet"]]
    """The type of resource to query. Currently only `wallet` is supported."""
