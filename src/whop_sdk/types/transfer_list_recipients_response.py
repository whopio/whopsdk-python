# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["TransferListRecipientsResponse", "TransferRecipientUser", "TransferRecipientAccount"]


class TransferRecipientUser(BaseModel):
    id: str
    """User ID."""

    name: Optional[str] = None
    """User display name."""

    object: Literal["user"]

    profile_picture_url: Optional[str] = None
    """User profile image URL."""

    username: Optional[str] = None
    """User's username."""


class TransferRecipientAccount(BaseModel):
    id: str
    """Account ID."""

    logo_url: Optional[str] = None
    """Account logo URL."""

    object: Literal["account"]

    route: Optional[str] = None
    """Account route."""

    title: Optional[str] = None
    """Account display name."""


TransferListRecipientsResponse: TypeAlias = Union[TransferRecipientUser, TransferRecipientAccount]
