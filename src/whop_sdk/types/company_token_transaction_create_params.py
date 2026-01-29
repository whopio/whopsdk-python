# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "CompanyTokenTransactionCreateParams",
    "CreateCompanyTokenTransactionInputTransactionTypeTransfer",
    "CreateCompanyTokenTransactionInputTransactionTypeAdd",
    "CreateCompanyTokenTransactionInputTransactionTypeSubtract",
]


class CreateCompanyTokenTransactionInputTransactionTypeTransfer(TypedDict, total=False):
    amount: Required[float]
    """The positive amount of tokens"""

    company_id: Required[str]
    """The company ID"""

    destination_user_id: Required[str]
    """Required for transfers - the user to receive tokens"""

    transaction_type: Required[Literal["transfer"]]

    user_id: Required[str]
    """The user ID whose balance will change"""

    description: Optional[str]
    """Optional description for the transaction"""

    idempotency_key: Optional[str]
    """Optional key to prevent duplicate transactions"""


class CreateCompanyTokenTransactionInputTransactionTypeAdd(TypedDict, total=False):
    amount: Required[float]
    """The positive amount of tokens"""

    company_id: Required[str]
    """The company ID"""

    transaction_type: Required[Literal["add"]]

    user_id: Required[str]
    """The user ID whose balance will change"""

    description: Optional[str]
    """Optional description for the transaction"""

    idempotency_key: Optional[str]
    """Optional key to prevent duplicate transactions"""


class CreateCompanyTokenTransactionInputTransactionTypeSubtract(TypedDict, total=False):
    amount: Required[float]
    """The positive amount of tokens"""

    company_id: Required[str]
    """The company ID"""

    transaction_type: Required[Literal["subtract"]]

    user_id: Required[str]
    """The user ID whose balance will change"""

    description: Optional[str]
    """Optional description for the transaction"""

    idempotency_key: Optional[str]
    """Optional key to prevent duplicate transactions"""


CompanyTokenTransactionCreateParams: TypeAlias = Union[
    CreateCompanyTokenTransactionInputTransactionTypeTransfer,
    CreateCompanyTokenTransactionInputTransactionTypeAdd,
    CreateCompanyTokenTransactionInputTransactionTypeSubtract,
]
