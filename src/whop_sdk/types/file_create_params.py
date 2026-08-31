# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    filename: Required[str]
    """The name of the file including its extension, e.g. `terms.pdf`."""

    byte_size: int
    """The file's size in bytes.

    Required when `multipart` is `true`. Multipart uploads support at most 10,000
    parts of 5MB each (about 50 GB).
    """

    multipart: bool
    """Upload the file in 5MB parts.

    Required for files larger than 5GB; useful above ~100MB. The file must be larger
    than 5MB.
    """

    visibility: Literal["public", "private"]
    """
    `public` files are served via an unsigned CDN URL — use for assets anyone may
    see. `private` files are served via a signed, expiring URL — use for sensitive
    documents. Defaults to `private`.
    """

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
