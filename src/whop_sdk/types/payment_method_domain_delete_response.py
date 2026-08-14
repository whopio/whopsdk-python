# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PaymentMethodDomainDeleteResponse"]


class PaymentMethodDomainDeleteResponse(BaseModel):
    id: str

    deleted: bool
