# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.plan_type import PlanType
from .shared.visibility import Visibility
from .shared.release_method import ReleaseMethod
from .shared.collection_method import CollectionMethod

__all__ = ["InvoiceCreateParams", "Plan", "PlanCustomField", "Product"]


class InvoiceCreateParams(TypedDict, total=False):
    collection_method: Required[CollectionMethod]
    """The method of collection for this invoice.

    If using charge_automatically, you must provide a payment_token.
    """

    company_id: Required[str]
    """The company ID to create this invoice for."""

    due_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
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
    """The properties of the product to create for this invoice.

    Include this if you want to create an invoice for a new product.
    """

    product_id: Optional[str]
    """The product ID to create this invoice for.

    Include this if you want to create an invoice for an existing product.
    """


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


class Plan(TypedDict, total=False):
    billing_period: Optional[int]
    """The interval at which the plan charges (renewal plans)."""

    custom_fields: Optional[Iterable[PlanCustomField]]
    """An array of custom field objects."""

    description: Optional[str]
    """The description of the plan."""

    expiration_days: Optional[int]
    """The interval at which the plan charges (expiration plans)."""

    initial_price: Optional[float]
    """An additional amount charged upon first purchase.

    Use only if a one time payment OR you want to charge an additional amount on top
    of the renewal price. Provided as a number in dollars. Eg: 10.43 for $10.43
    """

    internal_notes: Optional[str]
    """A personal description or notes section for the business."""

    plan_type: Optional[PlanType]
    """The type of plan that can be attached to an access pass"""

    release_method: Optional[ReleaseMethod]
    """The methods of how a plan can be released."""

    renewal_price: Optional[float]
    """The amount the customer is charged every billing period.

    Use only if a recurring payment. Provided as a number in dollars. Eg: 10.43 for
    $10.43
    """

    trial_period_days: Optional[int]
    """The number of free trial days added before a renewal plan."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class Product(TypedDict, total=False):
    title: Required[str]
    """The title of the product."""

    product_tax_code_id: Optional[str]
    """The ID of the product tax code to apply to this product."""
