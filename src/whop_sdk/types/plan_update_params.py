# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared.currency import Currency
from .shared.tax_type import TaxType
from .shared.visibility import Visibility
from .payment_method_types import PaymentMethodTypes

__all__ = [
    "PlanUpdateParams",
    "CustomField",
    "Image",
    "ImageAttachmentInputWithDirectUploadID",
    "ImageAttachmentInputWithID",
    "PaymentMethodConfiguration",
]


class PlanUpdateParams(TypedDict, total=False):
    billing_period: Optional[int]
    """The interval at which the plan charges (renewal plans)."""

    currency: Optional[Currency]
    """The available currencies on the platform"""

    custom_fields: Optional[Iterable[CustomField]]
    """An array of custom field objects."""

    description: Optional[str]
    """The description of the plan."""

    expiration_days: Optional[int]
    """The interval at which the plan charges (expiration plans)."""

    image: Optional[Image]
    """An image for the plan. This will be visible on the product page to customers."""

    initial_price: Optional[float]
    """An additional amount charged upon first purchase."""

    internal_notes: Optional[str]
    """A personal description or notes section for the business."""

    offer_cancel_discount: Optional[bool]
    """Whether or not to offer a discount to cancel a subscription."""

    override_tax_type: Optional[TaxType]
    """
    Whether or not the tax is included in a plan's price (or if it hasn't been set
    up)
    """

    payment_method_configuration: Optional[PaymentMethodConfiguration]
    """The explicit payment method configuration for the plan.

    If sent as null, the custom configuration will be removed.
    """

    renewal_price: Optional[float]
    """The amount the customer is charged every billing period."""

    stock: Optional[int]
    """The number of units available for purchase."""

    strike_through_initial_price: Optional[float]
    """The price to display with a strikethrough for the initial price.

    Provided as a number in dollars. Eg: 19.99 for $19.99
    """

    strike_through_renewal_price: Optional[float]
    """The price to display with a strikethrough for the renewal price.

    Provided as a number in dollars. Eg: 19.99 for $19.99
    """

    title: Optional[str]
    """The title of the plan. This will be visible on the product page to customers."""

    trial_period_days: Optional[int]
    """The number of free trial days added before a renewal plan."""

    unlimited_stock: Optional[bool]
    """Limits/doesn't limit the number of units available for purchase."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class CustomField(TypedDict, total=False):
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


class ImageAttachmentInputWithDirectUploadID(TypedDict, total=False):
    """Input for an attachment"""

    direct_upload_id: Required[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """


class ImageAttachmentInputWithID(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """


Image: TypeAlias = Union[ImageAttachmentInputWithDirectUploadID, ImageAttachmentInputWithID]


class PaymentMethodConfiguration(TypedDict, total=False):
    """The explicit payment method configuration for the plan.

    If sent as null, the custom configuration will be removed.
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
