# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .entry_denied_webhook_event import EntryDeniedWebhookEvent
from .invoice_paid_webhook_event import InvoicePaidWebhookEvent
from .plan_created_webhook_event import PlanCreatedWebhookEvent
from .plan_deleted_webhook_event import PlanDeletedWebhookEvent
from .plan_updated_webhook_event import PlanUpdatedWebhookEvent
from .entry_created_webhook_event import EntryCreatedWebhookEvent
from .entry_deleted_webhook_event import EntryDeletedWebhookEvent
from .export_failed_webhook_event import ExportFailedWebhookEvent
from .entry_approved_webhook_event import EntryApprovedWebhookEvent
from .invoice_voided_webhook_event import InvoiceVoidedWebhookEvent
from .member_created_webhook_event import MemberCreatedWebhookEvent
from .payment_failed_webhook_event import PaymentFailedWebhookEvent
from .refund_created_webhook_event import RefundCreatedWebhookEvent
from .refund_updated_webhook_event import RefundUpdatedWebhookEvent
from .dispute_created_webhook_event import DisputeCreatedWebhookEvent
from .dispute_updated_webhook_event import DisputeUpdatedWebhookEvent
from .invoice_created_webhook_event import InvoiceCreatedWebhookEvent
from .payment_created_webhook_event import PaymentCreatedWebhookEvent
from .payment_pending_webhook_event import PaymentPendingWebhookEvent
from .product_created_webhook_event import ProductCreatedWebhookEvent
from .product_deleted_webhook_event import ProductDeletedWebhookEvent
from .product_updated_webhook_event import ProductUpdatedWebhookEvent
from .export_completed_webhook_event import ExportCompletedWebhookEvent
from .invoice_past_due_webhook_event import InvoicePastDueWebhookEvent
from .shipment_created_webhook_event import ShipmentCreatedWebhookEvent
from .shipment_updated_webhook_event import ShipmentUpdatedWebhookEvent
from .deposit_succeeded_webhook_event import DepositSucceededWebhookEvent
from .payment_succeeded_webhook_event import PaymentSucceededWebhookEvent
from .product_published_webhook_event import ProductPublishedWebhookEvent
from .withdrawal_created_webhook_event import WithdrawalCreatedWebhookEvent
from .withdrawal_updated_webhook_event import WithdrawalUpdatedWebhookEvent
from .product_unpublished_webhook_event import ProductUnpublishedWebhookEvent
from .chat_message_created_webhook_event import ChatMessageCreatedWebhookEvent
from .membership_activated_webhook_event import MembershipActivatedWebhookEvent
from .chat_reaction_created_webhook_event import ChatReactionCreatedWebhookEvent
from .dispute_alert_created_webhook_event import DisputeAlertCreatedWebhookEvent
from .payout_method_created_webhook_event import PayoutMethodCreatedWebhookEvent
from .setup_intent_canceled_webhook_event import SetupIntentCanceledWebhookEvent
from .membership_deactivated_webhook_event import MembershipDeactivatedWebhookEvent
from .setup_intent_succeeded_webhook_event import SetupIntentSucceededWebhookEvent
from .verification_succeeded_webhook_event import VerificationSucceededWebhookEvent
from .card_transaction_created_webhook_event import CardTransactionCreatedWebhookEvent
from .card_transaction_updated_webhook_event import CardTransactionUpdatedWebhookEvent
from .identity_profile_updated_webhook_event import IdentityProfileUpdatedWebhookEvent
from .card_transaction_declined_webhook_event import CardTransactionDeclinedWebhookEvent
from .card_transaction_reversed_webhook_event import CardTransactionReversedWebhookEvent
from .card_transaction_completed_webhook_event import CardTransactionCompletedWebhookEvent
from .invoice_marked_uncollectible_webhook_event import InvoiceMarkedUncollectibleWebhookEvent
from .membership_trial_ending_soon_webhook_event import MembershipTrialEndingSoonWebhookEvent
from .setup_intent_requires_action_webhook_event import SetupIntentRequiresActionWebhookEvent
from .payout_account_status_updated_webhook_event import PayoutAccountStatusUpdatedWebhookEvent
from .ledger_account_funds_available_webhook_event import LedgerAccountFundsAvailableWebhookEvent
from .resolution_center_case_created_webhook_event import ResolutionCenterCaseCreatedWebhookEvent
from .resolution_center_case_decided_webhook_event import ResolutionCenterCaseDecidedWebhookEvent
from .resolution_center_case_updated_webhook_event import ResolutionCenterCaseUpdatedWebhookEvent
from .course_lesson_interaction_completed_webhook_event import CourseLessonInteractionCompletedWebhookEvent
from .membership_cancel_at_period_end_changed_webhook_event import MembershipCancelAtPeriodEndChangedWebhookEvent

__all__ = ["UnwrapWebhookEvent"]

UnwrapWebhookEvent: TypeAlias = Annotated[
    Union[
        CardTransactionCompletedWebhookEvent,
        CardTransactionCreatedWebhookEvent,
        CardTransactionDeclinedWebhookEvent,
        CardTransactionReversedWebhookEvent,
        CardTransactionUpdatedWebhookEvent,
        ChatMessageCreatedWebhookEvent,
        ChatReactionCreatedWebhookEvent,
        CourseLessonInteractionCompletedWebhookEvent,
        DepositSucceededWebhookEvent,
        DisputeCreatedWebhookEvent,
        DisputeUpdatedWebhookEvent,
        DisputeAlertCreatedWebhookEvent,
        EntryApprovedWebhookEvent,
        EntryCreatedWebhookEvent,
        EntryDeletedWebhookEvent,
        EntryDeniedWebhookEvent,
        ExportCompletedWebhookEvent,
        ExportFailedWebhookEvent,
        IdentityProfileUpdatedWebhookEvent,
        InvoiceCreatedWebhookEvent,
        InvoiceMarkedUncollectibleWebhookEvent,
        InvoicePaidWebhookEvent,
        InvoicePastDueWebhookEvent,
        InvoiceVoidedWebhookEvent,
        LedgerAccountFundsAvailableWebhookEvent,
        MemberCreatedWebhookEvent,
        MembershipActivatedWebhookEvent,
        MembershipCancelAtPeriodEndChangedWebhookEvent,
        MembershipDeactivatedWebhookEvent,
        MembershipTrialEndingSoonWebhookEvent,
        PaymentCreatedWebhookEvent,
        PaymentFailedWebhookEvent,
        PaymentPendingWebhookEvent,
        PaymentSucceededWebhookEvent,
        PayoutAccountStatusUpdatedWebhookEvent,
        PayoutMethodCreatedWebhookEvent,
        PlanCreatedWebhookEvent,
        PlanDeletedWebhookEvent,
        PlanUpdatedWebhookEvent,
        ProductCreatedWebhookEvent,
        ProductDeletedWebhookEvent,
        ProductPublishedWebhookEvent,
        ProductUnpublishedWebhookEvent,
        ProductUpdatedWebhookEvent,
        RefundCreatedWebhookEvent,
        RefundUpdatedWebhookEvent,
        ResolutionCenterCaseCreatedWebhookEvent,
        ResolutionCenterCaseDecidedWebhookEvent,
        ResolutionCenterCaseUpdatedWebhookEvent,
        SetupIntentCanceledWebhookEvent,
        SetupIntentRequiresActionWebhookEvent,
        SetupIntentSucceededWebhookEvent,
        ShipmentCreatedWebhookEvent,
        ShipmentUpdatedWebhookEvent,
        VerificationSucceededWebhookEvent,
        WithdrawalCreatedWebhookEvent,
        WithdrawalUpdatedWebhookEvent,
    ],
    PropertyInfo(discriminator="type"),
]
