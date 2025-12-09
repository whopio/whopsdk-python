# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .checkout_modes import CheckoutModes
from .shared.currency import Currency
from .shared.plan_type import PlanType
from .shared.visibility import Visibility
from .payment_method_types import PaymentMethodTypes
from .shared.release_method import ReleaseMethod

__all__ = ["CheckoutConfigurationListResponse", "PaymentMethodConfiguration", "Plan"]


class PaymentMethodConfiguration(BaseModel):
    """The explicit payment method configuration for the session, if any.

    This currently only works in 'setup' mode. Use the plan's payment_method_configuration for payment method.
    """

    disabled: List[PaymentMethodTypes]
    """An array of payment method identifiers that are explicitly disabled.

    Only applies if the include_platform_defaults is true.
    """

    enabled: List[PaymentMethodTypes]
    """An array of payment method identifiers that are explicitly enabled.

    This means these payment methods will be shown on checkout. Example use case is
    to only enable a specific payment method like cashapp, or extending the platform
    defaults with additional methods.
    """

    include_platform_defaults: bool
    """
    Whether Whop's platform default payment method enablement settings are included
    in this configuration. The full list of default payment methods can be found in
    the documentation at docs.whop.com/payments.
    """


class Plan(BaseModel):
    """The plan to use for the checkout configuration"""

    id: str
    """The internal ID of the plan."""

    billing_period: Optional[int] = None
    """The interval at which the plan charges (renewal plans)."""

    currency: Currency
    """The respective currency identifier for the plan."""

    expiration_days: Optional[int] = None
    """The interval at which the plan charges (expiration plans)."""

    initial_price: float
    """The price a person has to pay for a plan on the initial purchase."""

    plan_type: PlanType
    """Indicates if the plan is a one time payment or recurring."""

    release_method: ReleaseMethod
    """This is the release method the business uses to sell this plan."""

    renewal_price: float
    """The price a person has to pay for a plan on the renewal purchase."""

    trial_period_days: Optional[int] = None
    """The number of free trial days added before a renewal plan."""

    visibility: Visibility
    """Shows or hides the plan from public/business view."""


class CheckoutConfigurationListResponse(BaseModel):
    """
    A checkout configuration object.
            Can be used to create a reusable custom configuration for a checkout, including attaching plans, affiliates and custom metadata to the checkout.
            This configuration can be re-used by multiple users.
            All successful payments and memberships resulting from a checkout will contain the passed metadata.
    """

    id: str
    """The ID of the checkout configuration"""

    affiliate_code: Optional[str] = None
    """The affiliate code to use for the checkout configuration"""

    company_id: str
    """The ID of the company to use for the checkout configuration"""

    currency: Optional[Currency] = None
    """The available currencies on the platform"""

    metadata: Optional[Dict[str, object]] = None
    """The metadata to use for the checkout configuration"""

    mode: CheckoutModes
    """The mode of the checkout session."""

    payment_method_configuration: Optional[PaymentMethodConfiguration] = None
    """The explicit payment method configuration for the session, if any.

    This currently only works in 'setup' mode. Use the plan's
    payment_method_configuration for payment method.
    """

    plan: Optional[Plan] = None
    """The plan to use for the checkout configuration"""

    purchase_url: str
    """A URL you can send to customers to complete a checkout.

    It looks like `/checkout/plan_xxxx?session={id}`
    """

    redirect_url: Optional[str] = None
    """The URL to redirect the user to after the checkout configuration is created"""
