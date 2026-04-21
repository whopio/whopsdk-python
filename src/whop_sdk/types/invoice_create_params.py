# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared.plan_type import PlanType
from .shared.visibility import Visibility
from .tax_identifier_type import TaxIdentifierType
from .payment_method_types import PaymentMethodTypes
from .shared.release_method import ReleaseMethod
from .shared.collection_method import CollectionMethod

__all__ = [
    "InvoiceCreateParams",
    "CreateInvoiceInputWithProduct",
    "CreateInvoiceInputWithProductPlan",
    "CreateInvoiceInputWithProductPlanCustomField",
    "CreateInvoiceInputWithProductPlanPaymentMethodConfiguration",
    "CreateInvoiceInputWithProductProduct",
    "CreateInvoiceInputWithProductBillingAddress",
    "CreateInvoiceInputWithProductLineItem",
    "CreateInvoiceInputWithProductID",
    "CreateInvoiceInputWithProductIDPlan",
    "CreateInvoiceInputWithProductIDPlanCustomField",
    "CreateInvoiceInputWithProductIDPlanPaymentMethodConfiguration",
    "CreateInvoiceInputWithProductIDBillingAddress",
    "CreateInvoiceInputWithProductIDLineItem",
]


class CreateInvoiceInputWithProduct(TypedDict, total=False):
    collection_method: Required[CollectionMethod]
    """How the invoice should be collected.

    Use charge_automatically to charge a stored payment method, or send_invoice to
    email the customer.
    """

    company_id: Required[str]
    """The unique identifier of the company to create this invoice for."""

    plan: Required[CreateInvoiceInputWithProductPlan]
    """
    The plan attributes defining the price, currency, and billing interval for this
    invoice.
    """

    product: Required[CreateInvoiceInputWithProductProduct]
    """The properties of the product to create for this invoice.

    Provide this to create a new product inline.
    """

    automatically_finalizes_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date and time when the invoice will be automatically finalized.

    For charge_automatically, triggers an automatic charge. For send_invoice, sends
    the invoice email to the customer at the specified time.
    """

    billing_address: Optional[CreateInvoiceInputWithProductBillingAddress]
    """Inline billing address to create a new mailing address for this invoice.

    Cannot be used together with mailing_address_id.
    """

    charge_buyer_fee: Optional[bool]
    """Whether to charge the customer a buyer fee on this invoice."""

    customer_name: Optional[str]
    """The name of the customer.

    Required when creating an invoice for a customer who is not yet a member of the
    company.
    """

    due_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date by which the invoice must be paid.

    Required unless save_as_draft is true.
    """

    email_address: Optional[str]
    """The email address of the customer.

    Required when creating an invoice for a customer who is not yet a member of the
    company.
    """

    line_items: Optional[Iterable[CreateInvoiceInputWithProductLineItem]]
    """Optional line items that break down the invoice total.

    When provided, the sum of (quantity \\** unit_price) for all items must equal the
    plan price.
    """

    mailing_address_id: Optional[str]
    """The unique identifier of an existing mailing address to attach to this invoice.

    Cannot be used together with billing_address.
    """

    member_id: Optional[str]
    """The unique identifier of an existing member to create this invoice for.

    If not provided, you must supply an email_address and customer_name.
    """

    payment_method_id: Optional[str]
    """The unique identifier of the payment method to charge.

    Required when collection_method is charge_automatically.
    """

    payment_token_id: Optional[str]
    """The payment token ID to use for this invoice.

    If using charge_automatically, you must provide a payment_token.
    """

    save_as_draft: Optional[bool]
    """When true, creates the invoice as a draft without sending or charging.

    Relaxes customer and due date requirements.
    """

    subscription_billing_anchor_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date that defines when the subscription billing cycle should start.

    When set on a renewal plan invoice, this anchors all future billing periods to
    this date.
    """


class CreateInvoiceInputWithProductPlanCustomField(TypedDict, total=False):
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


class CreateInvoiceInputWithProductPlanPaymentMethodConfiguration(TypedDict, total=False):
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


class CreateInvoiceInputWithProductPlan(TypedDict, total=False):
    """
    The plan attributes defining the price, currency, and billing interval for this invoice.
    """

    billing_period: Optional[int]
    """The interval in days at which the plan charges (renewal plans)."""

    custom_fields: Optional[Iterable[CreateInvoiceInputWithProductPlanCustomField]]
    """An array of custom field objects."""

    description: Optional[str]
    """The description of the plan."""

    expiration_days: Optional[int]
    """
    The number of days until the membership expires and revokes access (expiration
    plans). For example, 365 for a one-year access period.
    """

    initial_price: Optional[float]
    """An additional amount charged upon first purchase.

    Use only if a one time payment OR you want to charge an additional amount on top
    of the renewal price. Provided as a number in the specified currency. Eg: 10.43
    for $10.43
    """

    internal_notes: Optional[str]
    """A personal description or notes section for the business."""

    legacy_payment_method_controls: Optional[bool]
    """Whether this plan uses legacy payment method controls"""

    payment_method_configuration: Optional[CreateInvoiceInputWithProductPlanPaymentMethodConfiguration]
    """The explicit payment method configuration for the plan.

    If not provided, the platform or company's defaults will apply.
    """

    plan_type: Optional[PlanType]
    """The type of plan that can be attached to a product"""

    release_method: Optional[ReleaseMethod]
    """The methods of how a plan can be released."""

    renewal_price: Optional[float]
    """The amount the customer is charged every billing period.

    Use only if a recurring payment. Provided as a number in the specified currency.
    Eg: 10.43 for $10.43
    """

    stock: Optional[int]
    """The number of units available for purchase."""

    trial_period_days: Optional[int]
    """The number of free trial days added before a renewal plan."""

    unlimited_stock: Optional[bool]
    """When true, the plan has unlimited stock (stock field is ignored).

    When false, purchases are limited by the stock field.
    """

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class CreateInvoiceInputWithProductProduct(TypedDict, total=False):
    """The properties of the product to create for this invoice.

    Provide this to create a new product inline.
    """

    title: Required[str]
    """The title of the product."""

    product_tax_code_id: Optional[str]
    """The ID of the product tax code to apply to this product."""


class CreateInvoiceInputWithProductBillingAddress(TypedDict, total=False):
    """Inline billing address to create a new mailing address for this invoice.

    Cannot be used together with mailing_address_id.
    """

    city: Optional[str]
    """The city of the address."""

    country: Optional[str]
    """The country of the address."""

    line1: Optional[str]
    """The line 1 of the address."""

    line2: Optional[str]
    """The line 2 of the address."""

    name: Optional[str]
    """The name of the customer."""

    phone: Optional[str]
    """The phone number of the customer."""

    postal_code: Optional[str]
    """The postal code of the address."""

    state: Optional[str]
    """The state of the address."""

    tax_id_type: Optional[TaxIdentifierType]
    """The type of tax identifier"""

    tax_id_value: Optional[str]
    """The value of the tax identifier."""


class CreateInvoiceInputWithProductLineItem(TypedDict, total=False):
    """
    A single line item to include on the invoice, with a label, quantity, and unit price.
    """

    label: Required[str]
    """The label or description for this line item."""

    unit_price: Required[float]
    """The unit price for this line item.

    Provided as a number in the specified currency. Eg: 10.43 for $10.43
    """

    quantity: Optional[float]
    """The quantity of this line item. Defaults to 1."""


class CreateInvoiceInputWithProductID(TypedDict, total=False):
    collection_method: Required[CollectionMethod]
    """How the invoice should be collected.

    Use charge_automatically to charge a stored payment method, or send_invoice to
    email the customer.
    """

    company_id: Required[str]
    """The unique identifier of the company to create this invoice for."""

    plan: Required[CreateInvoiceInputWithProductIDPlan]
    """
    The plan attributes defining the price, currency, and billing interval for this
    invoice.
    """

    product_id: Required[str]
    """The unique identifier of an existing product to create this invoice for."""

    automatically_finalizes_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date and time when the invoice will be automatically finalized.

    For charge_automatically, triggers an automatic charge. For send_invoice, sends
    the invoice email to the customer at the specified time.
    """

    billing_address: Optional[CreateInvoiceInputWithProductIDBillingAddress]
    """Inline billing address to create a new mailing address for this invoice.

    Cannot be used together with mailing_address_id.
    """

    charge_buyer_fee: Optional[bool]
    """Whether to charge the customer a buyer fee on this invoice."""

    customer_name: Optional[str]
    """The name of the customer.

    Required when creating an invoice for a customer who is not yet a member of the
    company.
    """

    due_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date by which the invoice must be paid.

    Required unless save_as_draft is true.
    """

    email_address: Optional[str]
    """The email address of the customer.

    Required when creating an invoice for a customer who is not yet a member of the
    company.
    """

    line_items: Optional[Iterable[CreateInvoiceInputWithProductIDLineItem]]
    """Optional line items that break down the invoice total.

    When provided, the sum of (quantity \\** unit_price) for all items must equal the
    plan price.
    """

    mailing_address_id: Optional[str]
    """The unique identifier of an existing mailing address to attach to this invoice.

    Cannot be used together with billing_address.
    """

    member_id: Optional[str]
    """The unique identifier of an existing member to create this invoice for.

    If not provided, you must supply an email_address and customer_name.
    """

    payment_method_id: Optional[str]
    """The unique identifier of the payment method to charge.

    Required when collection_method is charge_automatically.
    """

    payment_token_id: Optional[str]
    """The payment token ID to use for this invoice.

    If using charge_automatically, you must provide a payment_token.
    """

    save_as_draft: Optional[bool]
    """When true, creates the invoice as a draft without sending or charging.

    Relaxes customer and due date requirements.
    """

    subscription_billing_anchor_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date that defines when the subscription billing cycle should start.

    When set on a renewal plan invoice, this anchors all future billing periods to
    this date.
    """


class CreateInvoiceInputWithProductIDPlanCustomField(TypedDict, total=False):
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


class CreateInvoiceInputWithProductIDPlanPaymentMethodConfiguration(TypedDict, total=False):
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


class CreateInvoiceInputWithProductIDPlan(TypedDict, total=False):
    """
    The plan attributes defining the price, currency, and billing interval for this invoice.
    """

    billing_period: Optional[int]
    """The interval in days at which the plan charges (renewal plans)."""

    custom_fields: Optional[Iterable[CreateInvoiceInputWithProductIDPlanCustomField]]
    """An array of custom field objects."""

    description: Optional[str]
    """The description of the plan."""

    expiration_days: Optional[int]
    """
    The number of days until the membership expires and revokes access (expiration
    plans). For example, 365 for a one-year access period.
    """

    initial_price: Optional[float]
    """An additional amount charged upon first purchase.

    Use only if a one time payment OR you want to charge an additional amount on top
    of the renewal price. Provided as a number in the specified currency. Eg: 10.43
    for $10.43
    """

    internal_notes: Optional[str]
    """A personal description or notes section for the business."""

    legacy_payment_method_controls: Optional[bool]
    """Whether this plan uses legacy payment method controls"""

    payment_method_configuration: Optional[CreateInvoiceInputWithProductIDPlanPaymentMethodConfiguration]
    """The explicit payment method configuration for the plan.

    If not provided, the platform or company's defaults will apply.
    """

    plan_type: Optional[PlanType]
    """The type of plan that can be attached to a product"""

    release_method: Optional[ReleaseMethod]
    """The methods of how a plan can be released."""

    renewal_price: Optional[float]
    """The amount the customer is charged every billing period.

    Use only if a recurring payment. Provided as a number in the specified currency.
    Eg: 10.43 for $10.43
    """

    stock: Optional[int]
    """The number of units available for purchase."""

    trial_period_days: Optional[int]
    """The number of free trial days added before a renewal plan."""

    unlimited_stock: Optional[bool]
    """When true, the plan has unlimited stock (stock field is ignored).

    When false, purchases are limited by the stock field.
    """

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class CreateInvoiceInputWithProductIDBillingAddress(TypedDict, total=False):
    """Inline billing address to create a new mailing address for this invoice.

    Cannot be used together with mailing_address_id.
    """

    city: Optional[str]
    """The city of the address."""

    country: Optional[str]
    """The country of the address."""

    line1: Optional[str]
    """The line 1 of the address."""

    line2: Optional[str]
    """The line 2 of the address."""

    name: Optional[str]
    """The name of the customer."""

    phone: Optional[str]
    """The phone number of the customer."""

    postal_code: Optional[str]
    """The postal code of the address."""

    state: Optional[str]
    """The state of the address."""

    tax_id_type: Optional[TaxIdentifierType]
    """The type of tax identifier"""

    tax_id_value: Optional[str]
    """The value of the tax identifier."""


class CreateInvoiceInputWithProductIDLineItem(TypedDict, total=False):
    """
    A single line item to include on the invoice, with a label, quantity, and unit price.
    """

    label: Required[str]
    """The label or description for this line item."""

    unit_price: Required[float]
    """The unit price for this line item.

    Provided as a number in the specified currency. Eg: 10.43 for $10.43
    """

    quantity: Optional[float]
    """The quantity of this line item. Defaults to 1."""


InvoiceCreateParams: TypeAlias = Union[CreateInvoiceInputWithProduct, CreateInvoiceInputWithProductID]
