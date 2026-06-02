# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .account_wallet import AccountWallet

__all__ = ["Account"]


class Account(BaseModel):
    id: str
    """The ID of the account, which will look like biz\\__******\\********"""

    created_at: str
    """When the account was created, as an ISO 8601 timestamp"""

    email: Optional[str] = None
    """The email address of the account owner"""

    metadata: object
    """Arbitrary key/value metadata supplied when the account was created"""

    wallet: Optional[AccountWallet] = None
    """The account's primary crypto wallet, or null if none has been provisioned"""
