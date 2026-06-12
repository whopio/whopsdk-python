# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PlanCalculateTaxResponse"]


class PlanCalculateTaxResponse(BaseModel):
    currency: str
    """The three-letter ISO 4217 currency code of the amounts."""

    status: Literal["calculated", "not_calculated"]
    """Whether tax was successfully calculated.

    Returns not_calculated when tax could not be determined.
    """

    subtotal: int
    """The plan price in the currency's smallest unit, for example cents.

    For exclusive tax this is the pre-tax amount; for inclusive tax it already
    contains the tax and equals the total.
    """

    tax_amount: int
    """The tax owed, in the currency's smallest unit.

    For exclusive tax it is added on top of the subtotal; for inclusive tax it is
    the portion already contained in the subtotal.
    """

    tax_behavior: Literal["exclusive", "inclusive"]
    """
    Whether tax is added on top of the price (exclusive) or already included in it
    (inclusive).
    """

    total: int
    """The total amount the buyer pays, in the currency's smallest unit."""
