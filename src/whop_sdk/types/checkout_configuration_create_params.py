# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared.currency import Currency
from .shared.tax_type import TaxType
from .shared.plan_type import PlanType
from .shared.visibility import Visibility
from .payment_method_types import PaymentMethodTypes
from .shared.business_types import BusinessTypes
from .shared.industry_types import IndustryTypes
from .shared.release_method import ReleaseMethod
from .shared.global_affiliate_status import GlobalAffiliateStatus

__all__ = [
    "CheckoutConfigurationCreateParams",
    "CreateCheckoutSessionInputModePaymentWithPlan",
    "CreateCheckoutSessionInputModePaymentWithPlanPlan",
    "CreateCheckoutSessionInputModePaymentWithPlanPlanCustomField",
    "CreateCheckoutSessionInputModePaymentWithPlanPlanImage",
    "CreateCheckoutSessionInputModePaymentWithPlanPlanImageAttachmentInputWithDirectUploadID",
    "CreateCheckoutSessionInputModePaymentWithPlanPlanImageAttachmentInputWithID",
    "CreateCheckoutSessionInputModePaymentWithPlanPlanPaymentMethodConfiguration",
    "CreateCheckoutSessionInputModePaymentWithPlanPlanProduct",
    "CreateCheckoutSessionInputModePaymentWithPlanPaymentMethodConfiguration",
    "CreateCheckoutSessionInputModePaymentWithPlanID",
    "CreateCheckoutSessionInputModePaymentWithPlanIDPaymentMethodConfiguration",
    "CreateCheckoutSessionInputModeSetup",
    "CreateCheckoutSessionInputModeSetupPaymentMethodConfiguration",
]


class CreateCheckoutSessionInputModePaymentWithPlan(TypedDict, total=False):
    plan: Required[CreateCheckoutSessionInputModePaymentWithPlanPlan]
    """Pass this object to create a new plan for this checkout configuration"""

    affiliate_code: Optional[str]
    """The affiliate code to use for the checkout configuration"""

    currency: Optional[Currency]
    """The available currencies on the platform"""

    metadata: Optional[Dict[str, object]]
    """The metadata to use for the checkout configuration"""

    mode: Literal["payment"]

    payment_method_configuration: Optional[CreateCheckoutSessionInputModePaymentWithPlanPaymentMethodConfiguration]
    """This currently only works for configurations made in 'setup' mode.

    The explicit payment method configuration for the checkout session. If not
    provided, the platform or company's defaults will apply.
    """

    redirect_url: Optional[str]
    """The URL to redirect the user to after the checkout configuration is created"""


class CreateCheckoutSessionInputModePaymentWithPlanPlanCustomField(TypedDict, total=False):
    field_type: Required[Literal["text"]]
    """The type of the custom field."""

    name: Required[str]
    """The name of the custom field."""

    id: Optional[str]
    """The ID of the custom field (if being updated)"""

    order: Optional[int]
    """The order of the field."""

    placeholder: Optional[str]
    """The placeholder value of the field."""

    required: Optional[bool]
    """Whether or not the field is required."""


class CreateCheckoutSessionInputModePaymentWithPlanPlanImageAttachmentInputWithDirectUploadID(TypedDict, total=False):
    """Input for an attachment"""

    direct_upload_id: Required[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """


class CreateCheckoutSessionInputModePaymentWithPlanPlanImageAttachmentInputWithID(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """


CreateCheckoutSessionInputModePaymentWithPlanPlanImage: TypeAlias = Union[
    CreateCheckoutSessionInputModePaymentWithPlanPlanImageAttachmentInputWithDirectUploadID,
    CreateCheckoutSessionInputModePaymentWithPlanPlanImageAttachmentInputWithID,
]


class CreateCheckoutSessionInputModePaymentWithPlanPlanPaymentMethodConfiguration(TypedDict, total=False):
    """The explicit payment method configuration for the plan.

    If not provided, the platform or company's defaults will apply.
    """

    disabled: Required[List[PaymentMethodTypes]]
    """An array of payment method identifiers that are explicitly disabled.

    Only applies if the include_platform_defaults is true.
    """

    enabled: Required[List[PaymentMethodTypes]]
    """An array of payment method identifiers that are explicitly enabled.

    This means these payment methods will be shown on checkout. Example use case is
    to only enable a specific payment method like cashapp, or extending the platform
    defaults with additional methods.
    """

    include_platform_defaults: Required[bool]
    """
    Whether Whop's platform default payment method enablement settings are included
    in this configuration. The full list of default payment methods can be found in
    the documentation at docs.whop.com/payments.
    """


class CreateCheckoutSessionInputModePaymentWithPlanPlanProduct(TypedDict, total=False):
    """Pass this object to create a new product for this plan.

    We will use the product external identifier to find or create an existing product.
    """

    external_identifier: Required[str]
    """A unique ID used to find or create a product.

    When provided during creation, we will look for an existing product with this
    external identifier — if found, it will be updated; otherwise, a new product
    will be created.
    """

    title: Required[str]
    """The title of the product."""

    business_type: Optional[BusinessTypes]
    """The different business types a company can be."""

    collect_shipping_address: Optional[bool]
    """Whether or not to collect shipping information at checkout from the customer."""

    custom_statement_descriptor: Optional[str]
    """The custom statement descriptor for the product i.e.

    WHOP\\**SPORTS, must be between 5 and 22 characters, contain at least one letter,
    and not contain any of the following characters: <, >, \\,, ', "
    """

    description: Optional[str]
    """A written description of the product."""

    global_affiliate_percentage: Optional[float]
    """The percentage of the revenue that goes to the global affiliate program."""

    global_affiliate_status: Optional[GlobalAffiliateStatus]
    """The different statuses of the global affiliate program for a product."""

    headline: Optional[str]
    """The headline of the product."""

    industry_type: Optional[IndustryTypes]
    """The different industry types a company can be in."""

    product_tax_code_id: Optional[str]
    """The ID of the product tax code to apply to this product."""

    redirect_purchase_url: Optional[str]
    """The URL to redirect the customer to after a purchase."""

    route: Optional[str]
    """The route of the product."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class CreateCheckoutSessionInputModePaymentWithPlanPlan(TypedDict, total=False):
    """Pass this object to create a new plan for this checkout configuration"""

    company_id: Required[str]
    """The company the plan should be created for."""

    currency: Required[Currency]
    """The respective currency identifier for the plan."""

    application_fee_amount: Optional[float]
    """The application fee amount collected by the platform from this connected
    account.

    Must be less than the total payment amount. Only valid for connected accounts
    with a parent company.
    """

    billing_period: Optional[int]
    """The interval at which the plan charges (renewal plans)."""

    custom_fields: Optional[Iterable[CreateCheckoutSessionInputModePaymentWithPlanPlanCustomField]]
    """An array of custom field objects."""

    description: Optional[str]
    """The description of the plan."""

    expiration_days: Optional[int]
    """The interval at which the plan charges (expiration plans)."""

    force_create_new_plan: Optional[bool]
    """
    Whether to force the creation of a new plan even if one with the same attributes
    already exists.
    """

    image: Optional[CreateCheckoutSessionInputModePaymentWithPlanPlanImage]
    """An image for the plan. This will be visible on the product page to customers."""

    initial_price: Optional[float]
    """An additional amount charged upon first purchase."""

    internal_notes: Optional[str]
    """A personal description or notes section for the business."""

    override_tax_type: Optional[TaxType]
    """
    Whether or not the tax is included in a plan's price (or if it hasn't been set
    up)
    """

    payment_method_configuration: Optional[CreateCheckoutSessionInputModePaymentWithPlanPlanPaymentMethodConfiguration]
    """The explicit payment method configuration for the plan.

    If not provided, the platform or company's defaults will apply.
    """

    plan_type: Optional[PlanType]
    """The type of plan that can be attached to a product"""

    product: Optional[CreateCheckoutSessionInputModePaymentWithPlanPlanProduct]
    """Pass this object to create a new product for this plan.

    We will use the product external identifier to find or create an existing
    product.
    """

    product_id: Optional[str]
    """The product the plan is related to. Either this or product is required."""

    release_method: Optional[ReleaseMethod]
    """The methods of how a plan can be released."""

    renewal_price: Optional[float]
    """The amount the customer is charged every billing period."""

    split_pay_required_payments: Optional[int]
    """The number of payments required before pausing the subscription."""

    title: Optional[str]
    """The title of the plan. This will be visible on the product page to customers."""

    trial_period_days: Optional[int]
    """The number of free trial days added before a renewal plan."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class CreateCheckoutSessionInputModePaymentWithPlanPaymentMethodConfiguration(TypedDict, total=False):
    """This currently only works for configurations made in 'setup' mode.

    The explicit payment method configuration for the checkout session. If not provided, the platform or company's defaults will apply.
    """

    disabled: Required[List[PaymentMethodTypes]]
    """An array of payment method identifiers that are explicitly disabled.

    Only applies if the include_platform_defaults is true.
    """

    enabled: Required[List[PaymentMethodTypes]]
    """An array of payment method identifiers that are explicitly enabled.

    This means these payment methods will be shown on checkout. Example use case is
    to only enable a specific payment method like cashapp, or extending the platform
    defaults with additional methods.
    """

    include_platform_defaults: Required[bool]
    """
    Whether Whop's platform default payment method enablement settings are included
    in this configuration. The full list of default payment methods can be found in
    the documentation at docs.whop.com/payments.
    """


class CreateCheckoutSessionInputModePaymentWithPlanID(TypedDict, total=False):
    plan_id: Required[str]
    """The ID of the plan to use for the checkout configuration"""

    affiliate_code: Optional[str]
    """The affiliate code to use for the checkout configuration"""

    currency: Optional[Currency]
    """The available currencies on the platform"""

    metadata: Optional[Dict[str, object]]
    """The metadata to use for the checkout configuration"""

    mode: Literal["payment"]

    payment_method_configuration: Optional[CreateCheckoutSessionInputModePaymentWithPlanIDPaymentMethodConfiguration]
    """This currently only works for configurations made in 'setup' mode.

    The explicit payment method configuration for the checkout session. If not
    provided, the platform or company's defaults will apply.
    """

    redirect_url: Optional[str]
    """The URL to redirect the user to after the checkout configuration is created"""


class CreateCheckoutSessionInputModePaymentWithPlanIDPaymentMethodConfiguration(TypedDict, total=False):
    """This currently only works for configurations made in 'setup' mode.

    The explicit payment method configuration for the checkout session. If not provided, the platform or company's defaults will apply.
    """

    disabled: Required[List[PaymentMethodTypes]]
    """An array of payment method identifiers that are explicitly disabled.

    Only applies if the include_platform_defaults is true.
    """

    enabled: Required[List[PaymentMethodTypes]]
    """An array of payment method identifiers that are explicitly enabled.

    This means these payment methods will be shown on checkout. Example use case is
    to only enable a specific payment method like cashapp, or extending the platform
    defaults with additional methods.
    """

    include_platform_defaults: Required[bool]
    """
    Whether Whop's platform default payment method enablement settings are included
    in this configuration. The full list of default payment methods can be found in
    the documentation at docs.whop.com/payments.
    """


class CreateCheckoutSessionInputModeSetup(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company for which to generate the checkout configuration.

    Only required in setup mode.
    """

    mode: Required[Literal["setup"]]

    currency: Optional[Currency]
    """The available currencies on the platform"""

    metadata: Optional[Dict[str, object]]
    """The metadata to use for the checkout configuration"""

    payment_method_configuration: Optional[CreateCheckoutSessionInputModeSetupPaymentMethodConfiguration]
    """This currently only works for configurations made in 'setup' mode.

    The explicit payment method configuration for the checkout session. If not
    provided, the platform or company's defaults will apply.
    """

    redirect_url: Optional[str]
    """The URL to redirect the user to after the checkout configuration is created"""


class CreateCheckoutSessionInputModeSetupPaymentMethodConfiguration(TypedDict, total=False):
    """This currently only works for configurations made in 'setup' mode.

    The explicit payment method configuration for the checkout session. If not provided, the platform or company's defaults will apply.
    """

    disabled: Required[List[PaymentMethodTypes]]
    """An array of payment method identifiers that are explicitly disabled.

    Only applies if the include_platform_defaults is true.
    """

    enabled: Required[List[PaymentMethodTypes]]
    """An array of payment method identifiers that are explicitly enabled.

    This means these payment methods will be shown on checkout. Example use case is
    to only enable a specific payment method like cashapp, or extending the platform
    defaults with additional methods.
    """

    include_platform_defaults: Required[bool]
    """
    Whether Whop's platform default payment method enablement settings are included
    in this configuration. The full list of default payment methods can be found in
    the documentation at docs.whop.com/payments.
    """


CheckoutConfigurationCreateParams: TypeAlias = Union[
    CreateCheckoutSessionInputModePaymentWithPlan,
    CreateCheckoutSessionInputModePaymentWithPlanID,
    CreateCheckoutSessionInputModeSetup,
]
