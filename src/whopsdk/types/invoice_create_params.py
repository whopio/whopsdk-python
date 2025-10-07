# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .shared.currency import Currency
from .shared.plan_type import PlanType
from .shared.visibility import Visibility
from .shared.release_method import ReleaseMethod
from .shared.collection_method import CollectionMethod

__all__ = ["InvoiceCreateParams", "Plan", "PlanCustomField", "Product"]


class InvoiceCreateParams(TypedDict, total=False):
    collection_method: Required[Optional[CollectionMethod]]
    """The method of collection for an invoice."""

    company_id: Required[str]
    """The company ID to create this invoice for."""

    due_date: Required[int]
    """The date the invoice is due, if applicable."""

    plan: Required[Plan]
    """The properties of the plan to create for this invoice."""

    charge_buyer_fee: Optional[bool]
    """Whether or not to charge the customer a buyer fee."""

    customer_name: Optional[str]
    """The name of the customer to create this invoice for.

    This is required if you want to create an invoice for a customer who does not
    have a member of your company yet.
    """

    email_address: Optional[str]
    """The email address to create this invoice for.

    This is required if you want to create an invoice for a user who does not have a
    member of your company yet.
    """

    member_id: Optional[str]
    """The member ID to create this invoice for.

    Include this if you want to create an invoice for an existing member. If you do
    not have a member ID, you must provide an email_address and customer_name.
    """

    payment_token_id: Optional[str]
    """The payment token ID to use for this invoice.

    If using charge_automatically, you must provide a payment_token.
    """

    product: Optional[Product]
    """The properties of the access pass to create for this invoice.

    Include this if you want to create an invoice for a new product.
    """

    product_id: Optional[str]
    """The access pass ID to create this invoice for.

    Include this if you want to create an invoice for an existing product.
    """


class PlanCustomField(TypedDict, total=False):
    field_type: Required[Optional[Literal["text"]]]
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


class Plan(TypedDict, total=False):
    ach_payments: Optional[bool]
    """Whether or not ACH payments are accepted"""

    base_currency: Optional[Currency]
    """The available currencies on the platform"""

    billing_period: Optional[int]
    """The interval at which the plan charges (renewal plans)."""

    card_payments: Optional[bool]
    """Whether or not card payments are accepted"""

    coinbase_commerce_accepted: Optional[bool]
    """Marks whether coinbase commerce payments are/aren't accepted."""

    custom_fields: Optional[Iterable[PlanCustomField]]
    """An array of custom field objects."""

    description: Optional[str]
    """The description of the plan."""

    expiration_days: Optional[int]
    """The interval at which the plan charges (expiration plans)."""

    initial_price: Optional[float]
    """An additional amount charged upon first purchase."""

    internal_notes: Optional[str]
    """A personal description or notes section for the business."""

    offer_cancel_discount: Optional[bool]
    """Whether or not to offer a discount to cancel a subscription."""

    paypal_accepted: Optional[bool]
    """Marks whether paypal payments are/aren't accepted."""

    plan_type: Optional[PlanType]
    """The type of plan that can be attached to an access pass"""

    platform_balance_accepted: Optional[bool]
    """Marks whether platform balance payments are/aren't accepted."""

    redirect_url: Optional[str]
    """The URL to redirect the customer to after purchase."""

    release_method: Optional[ReleaseMethod]
    """The methods of how a plan can be released."""

    renewal_price: Optional[float]
    """The amount the customer is charged every billing period."""

    split_pay_required_payments: Optional[int]
    """The number of payments required before pausing the subscription."""

    splitit_accepted: Optional[bool]
    """
    Marks whether payments using splitit, a payment processor, are/aren't accepted
    for the plan.
    """

    stock: Optional[int]
    """The number of units available for purchase."""

    trial_period_days: Optional[int]
    """The number of free trial days added before a renewal plan."""

    unlimited_stock: Optional[bool]
    """Limits/doesn't limit the number of units available for purchase."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class Product(TypedDict, total=False):
    title: Required[str]
    """The title of the access pass."""

    product_tax_code_id: Optional[str]
    """The ID of the product tax code to apply to this access pass."""
