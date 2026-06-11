# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DepositCreateResponse", "Bank", "BankInstruction", "BankMethod", "DepositAddress", "Destination"]


class BankInstruction(BaseModel):
    account_number: Optional[str] = None

    currency: str

    deposit_bank_name: Optional[str] = None

    deposit_beneficiary_name: Optional[str] = None

    deposit_reference: Optional[str] = None

    routing_number: Optional[str] = None


class BankMethod(BaseModel):
    currency: str

    rail: str


class Bank(BaseModel):
    instructions: Optional[List[BankInstruction]] = None

    methods: List[BankMethod]

    onboarding_link: Optional[str] = None

    status: Literal[
        "not_started",
        "pending_identification",
        "pending_review",
        "requires_signing",
        "active",
        "user_required",
        "suspended",
    ]


class DepositAddress(BaseModel):
    evm: str

    solana: str


class Destination(BaseModel):
    address: str

    currency: str

    network: str

    account_id: Optional[str] = None


class DepositCreateResponse(BaseModel):
    bank: Optional[Bank] = None

    deposit_address: DepositAddress

    destination: Destination

    hosted_url: Optional[str] = None

    metadata: Dict[str, object]

    object: Literal["deposit"]

    amount: Optional[str] = None
