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
    """The positive number of tokens to transact. For example, 100.0 for 100 tokens."""

    company_id: Required[str]
    """
    The unique identifier of the company to create the transaction in, starting with
    'biz\\__'.
    """

    destination_user_id: Required[str]
    """The unique identifier of the user receiving the tokens.

    Required when the transaction type is 'transfer'.
    """

    transaction_type: Required[Literal["transfer"]]

    user_id: Required[str]
    """
    The unique identifier of the user whose token balance will be affected, starting
    with 'user\\__'.
    """

    description: Optional[str]
    """A human-readable description of why the transaction was created."""

    idempotency_key: Optional[str]
    """A unique key to prevent duplicate transactions.

    Use a UUID or similar unique string.
    """


class CreateCompanyTokenTransactionInputTransactionTypeAdd(TypedDict, total=False):
    amount: Required[float]
    """The positive number of tokens to transact. For example, 100.0 for 100 tokens."""

    company_id: Required[str]
    """
    The unique identifier of the company to create the transaction in, starting with
    'biz\\__'.
    """

    transaction_type: Required[Literal["add"]]

    user_id: Required[str]
    """
    The unique identifier of the user whose token balance will be affected, starting
    with 'user\\__'.
    """

    description: Optional[str]
    """A human-readable description of why the transaction was created."""

    idempotency_key: Optional[str]
    """A unique key to prevent duplicate transactions.

    Use a UUID or similar unique string.
    """


class CreateCompanyTokenTransactionInputTransactionTypeSubtract(TypedDict, total=False):
    amount: Required[float]
    """The positive number of tokens to transact. For example, 100.0 for 100 tokens."""

    company_id: Required[str]
    """
    The unique identifier of the company to create the transaction in, starting with
    'biz\\__'.
    """

    transaction_type: Required[Literal["subtract"]]

    user_id: Required[str]
    """
    The unique identifier of the user whose token balance will be affected, starting
    with 'user\\__'.
    """

    description: Optional[str]
    """A human-readable description of why the transaction was created."""

    idempotency_key: Optional[str]
    """A unique key to prevent duplicate transactions.

    Use a UUID or similar unique string.
    """


CompanyTokenTransactionCreateParams: TypeAlias = Union[
    CreateCompanyTokenTransactionInputTransactionTypeTransfer,
    CreateCompanyTokenTransactionInputTransactionTypeAdd,
    CreateCompanyTokenTransactionInputTransactionTypeSubtract,
]
