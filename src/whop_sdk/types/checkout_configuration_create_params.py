# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .shared.currency import Currency
from .shared.tax_type import TaxType
from .shared.plan_type import PlanType
from .shared.visibility import Visibility
from .shared.release_method import ReleaseMethod

__all__ = ["CheckoutConfigurationCreateParams", "Plan", "PlanCustomField", "PlanImage"]


class CheckoutConfigurationCreateParams(TypedDict, total=False):
    affiliate_code: Optional[str]
    """The affiliate code to use for the checkout configuration"""

    metadata: Optional[Dict[str, object]]
    """The metadata to use for the checkout configuration"""

    plan: Optional[Plan]
    """Pass this object to create a new plan for this checkout configuration"""

    plan_id: Optional[str]
    """The ID of the plan to use for the checkout configuration"""

    redirect_url: Optional[str]
    """The URL to redirect the user to after the checkout configuration is created"""


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


class PlanImage(TypedDict, total=False):
    id: Optional[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """

    direct_upload_id: Optional[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """


class Plan(TypedDict, total=False):
    company_id: Required[str]
    """The company the plan should be created for."""

    billing_period: Optional[int]
    """The interval at which the plan charges (renewal plans)."""

    currency: Optional[Currency]
    """The available currencies on the platform"""

    custom_fields: Optional[Iterable[PlanCustomField]]
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

    image: Optional[PlanImage]
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

    plan_type: Optional[PlanType]
    """The type of plan that can be attached to an access pass"""

    product_id: Optional[str]
    """The product the plan is related to."""

    release_method: Optional[ReleaseMethod]
    """The methods of how a plan can be released."""

    renewal_price: Optional[float]
    """The amount the customer is charged every billing period."""

    title: Optional[str]
    """The title of the plan. This will be visible on the product page to customers."""

    trial_period_days: Optional[int]
    """The number of free trial days added before a renewal plan."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""
