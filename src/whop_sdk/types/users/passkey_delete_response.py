# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PasskeyDeleteResponse"]


class PasskeyDeleteResponse(BaseModel):
    id: str
    """The ID of the deleted passkey."""

    deleted: bool
    """Always `true`: the passkey was removed."""
