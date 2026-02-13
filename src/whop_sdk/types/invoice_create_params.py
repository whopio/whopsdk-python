# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared.plan_type import PlanType
from .shared.visibility import Visibility
from .shared.release_method import ReleaseMethod
from .shared.collection_method import CollectionMethod

__all__ = [
    "InvoiceCreateParams",
    "CreateInvoiceInputWithProductAndMemberID",
    "CreateInvoiceInputWithProductAndMemberIDPlan",
    "CreateInvoiceInputWithProductAndMemberIDPlanCustomField",
    "CreateInvoiceInputWithProductAndMemberIDProduct",
    "CreateInvoiceInputWithProductAndEmailAddress",
    "CreateInvoiceInputWithProductAndEmailAddressPlan",
    "CreateInvoiceInputWithProductAndEmailAddressPlanCustomField",
    "CreateInvoiceInputWithProductAndEmailAddressProduct",
    "CreateInvoiceInputWithProductIDAndMemberID",
    "CreateInvoiceInputWithProductIDAndMemberIDPlan",
    "CreateInvoiceInputWithProductIDAndMemberIDPlanCustomField",
    "CreateInvoiceInputWithProductIDAndEmailAddress",
    "CreateInvoiceInputWithProductIDAndEmailAddressPlan",
    "CreateInvoiceInputWithProductIDAndEmailAddressPlanCustomField",
]


class CreateInvoiceInputWithProductAndMemberID(TypedDict, total=False):
    collection_method: Required[CollectionMethod]
    """How the invoice should be collected.

    Use charge_automatically to charge a stored payment method, or send_invoice to
    email the customer.
    """

    company_id: Required[str]
    """The unique identifier of the company to create this invoice for."""

    due_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The date by which the invoice must be paid."""

    member_id: Required[str]
    """The unique identifier of an existing member to create this invoice for.

    If not provided, you must supply an email_address and customer_name.
    """

    plan: Required[CreateInvoiceInputWithProductAndMemberIDPlan]
    """
    The plan attributes defining the price, currency, and billing interval for this
    invoice.
    """

    product: Required[CreateInvoiceInputWithProductAndMemberIDProduct]
    """The properties of the product to create for this invoice.

    Provide this to create a new product inline.
    """

    automatically_finalizes_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date and time when the invoice will be automatically finalized and charged.

    Only valid when collection_method is charge_automatically. If not provided, the
    charge will be processed immediately.
    """

    charge_buyer_fee: Optional[bool]
    """Whether to charge the customer a buyer fee on this invoice."""

    customer_name: Optional[str]
    """The name of the customer.

    Required when creating an invoice for a customer who is not yet a member of the
    company.
    """

    payment_method_id: Optional[str]
    """The unique identifier of the payment method to charge.

    Required when collection_method is charge_automatically.
    """

    payment_token_id: Optional[str]
    """The payment token ID to use for this invoice.

    If using charge_automatically, you must provide a payment_token.
    """


class CreateInvoiceInputWithProductAndMemberIDPlanCustomField(TypedDict, total=False):
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


class CreateInvoiceInputWithProductAndMemberIDPlan(TypedDict, total=False):
    """
    The plan attributes defining the price, currency, and billing interval for this invoice.
    """

    billing_period: Optional[int]
    """The interval in days at which the plan charges (renewal plans)."""

    custom_fields: Optional[Iterable[CreateInvoiceInputWithProductAndMemberIDPlanCustomField]]
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


class CreateInvoiceInputWithProductAndMemberIDProduct(TypedDict, total=False):
    """The properties of the product to create for this invoice.

    Provide this to create a new product inline.
    """

    title: Required[str]
    """The title of the product."""

    product_tax_code_id: Optional[str]
    """The ID of the product tax code to apply to this product."""


class CreateInvoiceInputWithProductAndEmailAddress(TypedDict, total=False):
    collection_method: Required[CollectionMethod]
    """How the invoice should be collected.

    Use charge_automatically to charge a stored payment method, or send_invoice to
    email the customer.
    """

    company_id: Required[str]
    """The unique identifier of the company to create this invoice for."""

    due_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The date by which the invoice must be paid."""

    email_address: Required[str]
    """The email address of the customer.

    Required when creating an invoice for a customer who is not yet a member of the
    company.
    """

    plan: Required[CreateInvoiceInputWithProductAndEmailAddressPlan]
    """
    The plan attributes defining the price, currency, and billing interval for this
    invoice.
    """

    product: Required[CreateInvoiceInputWithProductAndEmailAddressProduct]
    """The properties of the product to create for this invoice.

    Provide this to create a new product inline.
    """

    automatically_finalizes_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date and time when the invoice will be automatically finalized and charged.

    Only valid when collection_method is charge_automatically. If not provided, the
    charge will be processed immediately.
    """

    charge_buyer_fee: Optional[bool]
    """Whether to charge the customer a buyer fee on this invoice."""

    customer_name: Optional[str]
    """The name of the customer.

    Required when creating an invoice for a customer who is not yet a member of the
    company.
    """

    payment_method_id: Optional[str]
    """The unique identifier of the payment method to charge.

    Required when collection_method is charge_automatically.
    """

    payment_token_id: Optional[str]
    """The payment token ID to use for this invoice.

    If using charge_automatically, you must provide a payment_token.
    """


class CreateInvoiceInputWithProductAndEmailAddressPlanCustomField(TypedDict, total=False):
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


class CreateInvoiceInputWithProductAndEmailAddressPlan(TypedDict, total=False):
    """
    The plan attributes defining the price, currency, and billing interval for this invoice.
    """

    billing_period: Optional[int]
    """The interval in days at which the plan charges (renewal plans)."""

    custom_fields: Optional[Iterable[CreateInvoiceInputWithProductAndEmailAddressPlanCustomField]]
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


class CreateInvoiceInputWithProductAndEmailAddressProduct(TypedDict, total=False):
    """The properties of the product to create for this invoice.

    Provide this to create a new product inline.
    """

    title: Required[str]
    """The title of the product."""

    product_tax_code_id: Optional[str]
    """The ID of the product tax code to apply to this product."""


class CreateInvoiceInputWithProductIDAndMemberID(TypedDict, total=False):
    collection_method: Required[CollectionMethod]
    """How the invoice should be collected.

    Use charge_automatically to charge a stored payment method, or send_invoice to
    email the customer.
    """

    company_id: Required[str]
    """The unique identifier of the company to create this invoice for."""

    due_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The date by which the invoice must be paid."""

    member_id: Required[str]
    """The unique identifier of an existing member to create this invoice for.

    If not provided, you must supply an email_address and customer_name.
    """

    plan: Required[CreateInvoiceInputWithProductIDAndMemberIDPlan]
    """
    The plan attributes defining the price, currency, and billing interval for this
    invoice.
    """

    product_id: Required[str]
    """The unique identifier of an existing product to create this invoice for."""

    automatically_finalizes_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date and time when the invoice will be automatically finalized and charged.

    Only valid when collection_method is charge_automatically. If not provided, the
    charge will be processed immediately.
    """

    charge_buyer_fee: Optional[bool]
    """Whether to charge the customer a buyer fee on this invoice."""

    customer_name: Optional[str]
    """The name of the customer.

    Required when creating an invoice for a customer who is not yet a member of the
    company.
    """

    payment_method_id: Optional[str]
    """The unique identifier of the payment method to charge.

    Required when collection_method is charge_automatically.
    """

    payment_token_id: Optional[str]
    """The payment token ID to use for this invoice.

    If using charge_automatically, you must provide a payment_token.
    """


class CreateInvoiceInputWithProductIDAndMemberIDPlanCustomField(TypedDict, total=False):
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


class CreateInvoiceInputWithProductIDAndMemberIDPlan(TypedDict, total=False):
    """
    The plan attributes defining the price, currency, and billing interval for this invoice.
    """

    billing_period: Optional[int]
    """The interval in days at which the plan charges (renewal plans)."""

    custom_fields: Optional[Iterable[CreateInvoiceInputWithProductIDAndMemberIDPlanCustomField]]
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


class CreateInvoiceInputWithProductIDAndEmailAddress(TypedDict, total=False):
    collection_method: Required[CollectionMethod]
    """How the invoice should be collected.

    Use charge_automatically to charge a stored payment method, or send_invoice to
    email the customer.
    """

    company_id: Required[str]
    """The unique identifier of the company to create this invoice for."""

    due_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The date by which the invoice must be paid."""

    email_address: Required[str]
    """The email address of the customer.

    Required when creating an invoice for a customer who is not yet a member of the
    company.
    """

    plan: Required[CreateInvoiceInputWithProductIDAndEmailAddressPlan]
    """
    The plan attributes defining the price, currency, and billing interval for this
    invoice.
    """

    product_id: Required[str]
    """The unique identifier of an existing product to create this invoice for."""

    automatically_finalizes_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date and time when the invoice will be automatically finalized and charged.

    Only valid when collection_method is charge_automatically. If not provided, the
    charge will be processed immediately.
    """

    charge_buyer_fee: Optional[bool]
    """Whether to charge the customer a buyer fee on this invoice."""

    customer_name: Optional[str]
    """The name of the customer.

    Required when creating an invoice for a customer who is not yet a member of the
    company.
    """

    payment_method_id: Optional[str]
    """The unique identifier of the payment method to charge.

    Required when collection_method is charge_automatically.
    """

    payment_token_id: Optional[str]
    """The payment token ID to use for this invoice.

    If using charge_automatically, you must provide a payment_token.
    """


class CreateInvoiceInputWithProductIDAndEmailAddressPlanCustomField(TypedDict, total=False):
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


class CreateInvoiceInputWithProductIDAndEmailAddressPlan(TypedDict, total=False):
    """
    The plan attributes defining the price, currency, and billing interval for this invoice.
    """

    billing_period: Optional[int]
    """The interval in days at which the plan charges (renewal plans)."""

    custom_fields: Optional[Iterable[CreateInvoiceInputWithProductIDAndEmailAddressPlanCustomField]]
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


InvoiceCreateParams: TypeAlias = Union[
    CreateInvoiceInputWithProductAndMemberID,
    CreateInvoiceInputWithProductAndEmailAddress,
    CreateInvoiceInputWithProductIDAndMemberID,
    CreateInvoiceInputWithProductIDAndEmailAddress,
]
