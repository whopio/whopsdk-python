# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.plan_type import PlanType
from .shared.visibility import Visibility
from .tax_identifier_type import TaxIdentifierType
from .payment_method_types import PaymentMethodTypes
from .shared.release_method import ReleaseMethod
from .shared.collection_method import CollectionMethod

__all__ = [
    "InvoiceUpdateParams",
    "BillingAddress",
    "LineItem",
    "Plan",
    "PlanCustomField",
    "PlanPaymentMethodConfiguration",
]


class InvoiceUpdateParams(TypedDict, total=False):
    automatically_finalizes_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date and time when the invoice will be automatically finalized and charged."""

    billing_address: Optional[BillingAddress]
    """Inline billing address to create or update a mailing address for this invoice."""

    charge_buyer_fee: Optional[bool]
    """Whether to charge the customer a buyer fee on this invoice."""

    collection_method: Optional[CollectionMethod]
    """The method of collection for an invoice."""

    customer_name: Optional[str]
    """The name of the customer."""

    due_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date by which the invoice must be paid."""

    email_address: Optional[str]
    """The email address of the customer."""

    line_items: Optional[Iterable[LineItem]]
    """Line items that break down the invoice total."""

    mailing_address_id: Optional[str]
    """The unique identifier of an existing mailing address to attach."""

    member_id: Optional[str]
    """The unique identifier of a member to assign as the customer."""

    payment_method_id: Optional[str]
    """The unique identifier of the payment method to charge."""

    plan: Optional[Plan]
    """Updated plan attributes."""


class BillingAddress(TypedDict, total=False):
    """Inline billing address to create or update a mailing address for this invoice."""

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


class LineItem(TypedDict, total=False):
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


class PlanCustomField(TypedDict, total=False):
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


class PlanPaymentMethodConfiguration(TypedDict, total=False):
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


class Plan(TypedDict, total=False):
    """Updated plan attributes."""

    billing_period: Optional[int]
    """The interval in days at which the plan charges (renewal plans)."""

    custom_fields: Optional[Iterable[PlanCustomField]]
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

    payment_method_configuration: Optional[PlanPaymentMethodConfiguration]
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
