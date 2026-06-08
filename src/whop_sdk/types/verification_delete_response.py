# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerificationDeleteResponse", "Rfi"]


class Rfi(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    description: Optional[str] = None

    error_message: Optional[str] = None

    status: Optional[Literal["outstanding", "invalid"]] = None

    type: Optional[str] = None


class VerificationDeleteResponse(BaseModel):
    id: Optional[str] = None
    """The identity profile ID, e.g. idpf\\__\\**"""

    address: Optional[object] = None

    business_name: Optional[str] = None

    business_structure: Optional[str] = None

    country: Optional[str] = None

    created_at: Optional[str] = None

    date_of_birth: Optional[str] = None

    first_name: Optional[str] = None

    kind: Optional[Literal["individual", "business"]] = None

    last_name: Optional[str] = None

    rfis: Optional[List[Rfi]] = None

    session_url: Optional[str] = None

    status: Optional[Literal["not_started", "pending", "approved", "rejected", "action_required"]] = None

    updated_at: Optional[str] = None
