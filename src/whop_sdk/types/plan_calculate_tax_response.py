# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PlanCalculateTaxResponse"]


class PlanCalculateTaxResponse(BaseModel):
    currency: str
    """Three-letter ISO 4217 currency code for the returned amounts."""

    status: Literal["calculated", "not_calculated"]
    """Whether Whop calculated tax for this preview.

    `not_calculated` means no tax could be determined, so `tax_amount` is 0 and
    `total` equals `subtotal`.
    """

    subtotal: int
    """Plan price in the currency's smallest unit, for example cents.

    For exclusive tax, this is the pre-tax amount; for inclusive tax, it already
    includes tax and equals the total.
    """

    tax_amount: int
    """Calculated tax amount in the currency's smallest unit.

    For exclusive tax, this is added on top of the subtotal; for inclusive tax, it
    is the portion of the subtotal that is tax.
    """

    tax_behavior: Literal["exclusive", "inclusive"]
    """
    Whether tax is added on top of the plan price or already included in it for this
    buyer's location.
    """

    total: int
    """Amount the buyer would pay in the currency's smallest unit."""
