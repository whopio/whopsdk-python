# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AudienceAddPeopleParams"]


class AudienceAddPeopleParams(TypedDict, total=False):
    file_id: Required[str]
    """The new customer CSV — a file id (`file_...`) returned by `POST /files`.

    Its headers must match the audience's saved column mapping.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
