# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UserCheckAccessResponse"]


class UserCheckAccessResponse(BaseModel):
    access_level: Literal["no_access", "admin", "customer"]

    has_access: bool
