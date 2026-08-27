# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .shared.currency import Currency
from .shared.plan_type import PlanType
from .shared.visibility import Visibility
from .shared.global_affiliate_status import GlobalAffiliateStatus

__all__ = [
    "PaymentCreateParams",
    "CreatePaymentInputWithPlanAndConfirmationToken",
    "CreatePaymentInputWithPlanAndConfirmationTokenPlan",
    "CreatePaymentInputWithPlanAndConfirmationTokenPlanProduct",
    "CreatePaymentInputWithPlanAndMemberID",
    "CreatePaymentInputWithPlanAndMemberIDPlan",
    "CreatePaymentInputWithPlanAndMemberIDPlanProduct",
    "CreatePaymentInputWithPlanIDAndConfirmationToken",
    "CreatePaymentInputWithPlanIDAndMemberID",
]


class CreatePaymentInputWithPlanAndConfirmationToken(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to create the payment for."""

    confirmation_token: Required[str]
    """
    A confirmation token ID (ctok\\__) describing a payment method the buyer just
    supplied. Provide this INSTEAD of member_id and payment_method_id to charge a
    method that is not yet on file — the buyer is resolved from the token's billing
    email, or from `email`. The buyer may still have a step to complete (3DS, a
    redirect, linking a bank); poll the payment's status endpoint for what to do
    next.
    """

    plan: Required[CreatePaymentInputWithPlanAndConfirmationTokenPlan]
    """Pass this object to create a new plan for this payment"""

    capture: Optional[bool]
    """Whether to capture the card payment immediately.

    Pass false to place an authorization hold that must be captured in full within
    five days.
    """

    email: Optional[str]
    """
    Overrides the buyer email carried on the confirmation token, resolving or
    creating the Whop user the payment belongs to. Ignored when the confirmation
    token was created by a signed-in buyer, and unless confirmation_token is
    provided.
    """

    metadata: Optional[Dict[str, object]]
    """Custom metadata to attach to the payment."""

    payment_method_id: Optional[str]
    """The ID of the payment method to use for the payment.

    It must be connected to the Member being charged. Required unless
    confirmation_token is provided.
    """

    promo_code_id: Optional[str]
    """The ID of an active promo code to apply to this payment.

    The promo code must belong to the company and be valid for the plan being
    purchased. The plan must be attached to a product — promo codes are not eligible
    for one-off purchases.
    """

    return_url: Optional[str]
    """Where the buyer continues after completing an off-site step.

    Must be an absolute https URL without credentials (http is allowed for
    localhost), at most 2,048 characters. Editable until they return — see the
    payment's update endpoint. Ignored unless confirmation_token is provided.
    """


class CreatePaymentInputWithPlanAndConfirmationTokenPlanProduct(TypedDict, total=False):
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

    product_tax_code_id: Optional[str]
    """The ID of the product tax code to apply to this product."""

    redirect_purchase_url: Optional[str]
    """The URL to redirect the customer to after a purchase."""

    route: Optional[str]
    """The route of the product."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class CreatePaymentInputWithPlanAndConfirmationTokenPlan(TypedDict, total=False):
    """Pass this object to create a new plan for this payment"""

    currency: Required[Currency]
    """The respective currency identifier for the plan."""

    application_fee_amount: Optional[float]
    """The application fee amount collected by the platform from this connected
    account.

    Provided as a number in dollars (e.g., 5.00 for $5.00). Must be less than the
    total payment amount. Only valid for connected accounts with a parent company.
    """

    billing_period: Optional[int]
    """The interval in days at which the plan charges (renewal plans).

    For example, 30 for monthly billing.
    """

    description: Optional[str]
    """The description of the plan."""

    expiration_days: Optional[int]
    """
    The number of days until the membership expires and revokes access (expiration
    plans). For example, 365 for one year.
    """

    force_create_new_plan: Optional[bool]
    """
    Whether to force the creation of a new plan even if one with the same attributes
    already exists.
    """

    initial_price: Optional[float]
    """An additional amount charged upon first purchase.

    Provided as a number in the specified currency. Eg: 10.43 for $10.43 USD.
    """

    internal_notes: Optional[str]
    """A personal description or notes section for the business."""

    plan_type: Optional[PlanType]
    """The type of plan that can be attached to a product"""

    product: Optional[CreatePaymentInputWithPlanAndConfirmationTokenPlanProduct]
    """Pass this object to create a new product for this plan.

    We will use the product external identifier to find or create an existing
    product.
    """

    product_id: Optional[str]
    """The product the plan is related to. Either this or product is required."""

    renewal_price: Optional[float]
    """The amount the customer is charged every billing period.

    Provided as a number in the specified currency. Eg: 10.43 for $10.43 USD.
    """

    title: Optional[str]
    """The title of the plan. This will be visible on the product page to customers."""

    trial_period_days: Optional[int]
    """The number of free trial days added before a renewal plan."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class CreatePaymentInputWithPlanAndMemberID(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to create the payment for."""

    member_id: Required[str]
    """The ID of the member to create the payment for.

    Required unless confirmation_token is provided.
    """

    plan: Required[CreatePaymentInputWithPlanAndMemberIDPlan]
    """Pass this object to create a new plan for this payment"""

    capture: Optional[bool]
    """Whether to capture the card payment immediately.

    Pass false to place an authorization hold that must be captured in full within
    five days.
    """

    email: Optional[str]
    """
    Overrides the buyer email carried on the confirmation token, resolving or
    creating the Whop user the payment belongs to. Ignored when the confirmation
    token was created by a signed-in buyer, and unless confirmation_token is
    provided.
    """

    metadata: Optional[Dict[str, object]]
    """Custom metadata to attach to the payment."""

    payment_method_id: Optional[str]
    """The ID of the payment method to use for the payment.

    It must be connected to the Member being charged. Required unless
    confirmation_token is provided.
    """

    promo_code_id: Optional[str]
    """The ID of an active promo code to apply to this payment.

    The promo code must belong to the company and be valid for the plan being
    purchased. The plan must be attached to a product — promo codes are not eligible
    for one-off purchases.
    """

    return_url: Optional[str]
    """Where the buyer continues after completing an off-site step.

    Must be an absolute https URL without credentials (http is allowed for
    localhost), at most 2,048 characters. Editable until they return — see the
    payment's update endpoint. Ignored unless confirmation_token is provided.
    """


class CreatePaymentInputWithPlanAndMemberIDPlanProduct(TypedDict, total=False):
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

    product_tax_code_id: Optional[str]
    """The ID of the product tax code to apply to this product."""

    redirect_purchase_url: Optional[str]
    """The URL to redirect the customer to after a purchase."""

    route: Optional[str]
    """The route of the product."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class CreatePaymentInputWithPlanAndMemberIDPlan(TypedDict, total=False):
    """Pass this object to create a new plan for this payment"""

    currency: Required[Currency]
    """The respective currency identifier for the plan."""

    application_fee_amount: Optional[float]
    """The application fee amount collected by the platform from this connected
    account.

    Provided as a number in dollars (e.g., 5.00 for $5.00). Must be less than the
    total payment amount. Only valid for connected accounts with a parent company.
    """

    billing_period: Optional[int]
    """The interval in days at which the plan charges (renewal plans).

    For example, 30 for monthly billing.
    """

    description: Optional[str]
    """The description of the plan."""

    expiration_days: Optional[int]
    """
    The number of days until the membership expires and revokes access (expiration
    plans). For example, 365 for one year.
    """

    force_create_new_plan: Optional[bool]
    """
    Whether to force the creation of a new plan even if one with the same attributes
    already exists.
    """

    initial_price: Optional[float]
    """An additional amount charged upon first purchase.

    Provided as a number in the specified currency. Eg: 10.43 for $10.43 USD.
    """

    internal_notes: Optional[str]
    """A personal description or notes section for the business."""

    plan_type: Optional[PlanType]
    """The type of plan that can be attached to a product"""

    product: Optional[CreatePaymentInputWithPlanAndMemberIDPlanProduct]
    """Pass this object to create a new product for this plan.

    We will use the product external identifier to find or create an existing
    product.
    """

    product_id: Optional[str]
    """The product the plan is related to. Either this or product is required."""

    renewal_price: Optional[float]
    """The amount the customer is charged every billing period.

    Provided as a number in the specified currency. Eg: 10.43 for $10.43 USD.
    """

    title: Optional[str]
    """The title of the plan. This will be visible on the product page to customers."""

    trial_period_days: Optional[int]
    """The number of free trial days added before a renewal plan."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class CreatePaymentInputWithPlanIDAndConfirmationToken(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to create the payment for."""

    confirmation_token: Required[str]
    """
    A confirmation token ID (ctok\\__) describing a payment method the buyer just
    supplied. Provide this INSTEAD of member_id and payment_method_id to charge a
    method that is not yet on file — the buyer is resolved from the token's billing
    email, or from `email`. The buyer may still have a step to complete (3DS, a
    redirect, linking a bank); poll the payment's status endpoint for what to do
    next.
    """

    plan_id: Required[str]
    """An ID of an existing plan to use for the payment."""

    capture: Optional[bool]
    """Whether to capture the card payment immediately.

    Pass false to place an authorization hold that must be captured in full within
    five days.
    """

    email: Optional[str]
    """
    Overrides the buyer email carried on the confirmation token, resolving or
    creating the Whop user the payment belongs to. Ignored when the confirmation
    token was created by a signed-in buyer, and unless confirmation_token is
    provided.
    """

    metadata: Optional[Dict[str, object]]
    """Custom metadata to attach to the payment."""

    payment_method_id: Optional[str]
    """The ID of the payment method to use for the payment.

    It must be connected to the Member being charged. Required unless
    confirmation_token is provided.
    """

    promo_code_id: Optional[str]
    """The ID of an active promo code to apply to this payment.

    The promo code must belong to the company and be valid for the plan being
    purchased. The plan must be attached to a product — promo codes are not eligible
    for one-off purchases.
    """

    return_url: Optional[str]
    """Where the buyer continues after completing an off-site step.

    Must be an absolute https URL without credentials (http is allowed for
    localhost), at most 2,048 characters. Editable until they return — see the
    payment's update endpoint. Ignored unless confirmation_token is provided.
    """


class CreatePaymentInputWithPlanIDAndMemberID(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to create the payment for."""

    member_id: Required[str]
    """The ID of the member to create the payment for.

    Required unless confirmation_token is provided.
    """

    plan_id: Required[str]
    """An ID of an existing plan to use for the payment."""

    capture: Optional[bool]
    """Whether to capture the card payment immediately.

    Pass false to place an authorization hold that must be captured in full within
    five days.
    """

    email: Optional[str]
    """
    Overrides the buyer email carried on the confirmation token, resolving or
    creating the Whop user the payment belongs to. Ignored when the confirmation
    token was created by a signed-in buyer, and unless confirmation_token is
    provided.
    """

    metadata: Optional[Dict[str, object]]
    """Custom metadata to attach to the payment."""

    payment_method_id: Optional[str]
    """The ID of the payment method to use for the payment.

    It must be connected to the Member being charged. Required unless
    confirmation_token is provided.
    """

    promo_code_id: Optional[str]
    """The ID of an active promo code to apply to this payment.

    The promo code must belong to the company and be valid for the plan being
    purchased. The plan must be attached to a product — promo codes are not eligible
    for one-off purchases.
    """

    return_url: Optional[str]
    """Where the buyer continues after completing an off-site step.

    Must be an absolute https URL without credentials (http is allowed for
    localhost), at most 2,048 characters. Editable until they return — see the
    payment's update endpoint. Ignored unless confirmation_token is provided.
    """


PaymentCreateParams: TypeAlias = Union[
    CreatePaymentInputWithPlanAndConfirmationToken,
    CreatePaymentInputWithPlanAndMemberID,
    CreatePaymentInputWithPlanIDAndConfirmationToken,
    CreatePaymentInputWithPlanIDAndMemberID,
]
