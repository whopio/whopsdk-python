# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerificationRetrieveResponse", "Rfi"]


class Rfi(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    description: Optional[str] = None

    error_message: Optional[str] = None

    status: Optional[Literal["outstanding", "invalid"]] = None

    type: Optional[str] = None


class VerificationRetrieveResponse(BaseModel):
    id: str
    """The identity profile ID, e.g. idpf\\__\\**"""

    created_at: str

    kind: Literal["individual", "business"]

    rfis: List[Rfi]

    status: Literal["not_started", "pending", "approved", "rejected", "action_required"]

    updated_at: str

    address: Optional[object] = None

    business_name: Optional[str] = None

    business_structure: Optional[str] = None

    country: Optional[str] = None

    date_of_birth: Optional[str] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    session_url: Optional[str] = None
