# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["DisputeUploadEvidenceParams", "Document"]


class DisputeUploadEvidenceParams(TypedDict, total=False):
    documents: Required[Iterable[Document]]
    """The full set of evidence documents the dispute should carry.

    Replaces all previously uploaded documents.
    """


class Document(TypedDict, total=False):
    document_type: Required[
        Literal[
            "return_policy",
            "shipping_policy",
            "physical_fulfillment",
            "customer_order_history",
            "product_image",
            "prior_transactions",
            "customer_session",
            "digital_fulfillment",
            "subscription",
        ]
    ]
    """What kind of evidence the document is."""

    id: str
    """The ID of a file already stored on Whop, prefixed `file_`."""

    direct_upload_id: str
    """The ID returned by a direct upload."""

    file: FileTypes
    """The file itself.

    Send it as a file part to upload and attach in one call, or use
    `id`/`direct_upload_id` for a file that is already stored.
    """
