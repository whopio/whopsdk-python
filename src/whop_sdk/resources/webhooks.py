# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import json
from typing import List, Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import (
    webhook_list_params,
    webhook_test_params,
    webhook_create_params,
    webhook_replay_params,
    webhook_update_params,
    webhook_list_deliveries_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._models import construct_type
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._exceptions import WhopError
from .._base_client import AsyncPaginator, make_request_options
from ..types.webhook import Webhook
from ..types.unwrap_webhook_event import UnwrapWebhookEvent
from ..types.webhook_list_response import WebhookListResponse
from ..types.webhook_test_response import WebhookTestResponse
from ..types.webhook_delete_response import WebhookDeleteResponse
from ..types.webhook_replay_response import WebhookReplayResponse
from ..types.webhook_list_deliveries_response import WebhookListDeliveriesResponse
from ..types.webhook_replay_delivery_response import WebhookReplayDeliveryResponse

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return WebhooksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        url: str,
        api_version_date: Optional[str] | Omit = omit,
        child_resource_events: bool | Omit = omit,
        enabled: bool | Omit = omit,
        events: List[
            Literal[
                "invoice.created",
                "invoice.marked_uncollectible",
                "invoice.paid",
                "invoice.past_due",
                "invoice.voided",
                "membership.activated",
                "membership.deactivated",
                "membership.trial_ending_soon",
                "entry.created",
                "entry.approved",
                "entry.denied",
                "entry.deleted",
                "export.completed",
                "export.failed",
                "setup_intent.requires_action",
                "setup_intent.succeeded",
                "setup_intent.canceled",
                "ledger_account.funds_available",
                "swap.completed",
                "deposit.succeeded",
                "transfer.created",
                "transfer.completed",
                "withdrawal.created",
                "withdrawal.updated",
                "card_transaction.created",
                "card_transaction.updated",
                "card_transaction.completed",
                "card_transaction.declined",
                "card_transaction.reversed",
                "card.created",
                "card.updated",
                "card.frozen",
                "card.canceled",
                "card_application.created",
                "card_application.updated",
                "card_application.approved",
                "card_application.denied",
                "course_lesson_interaction.completed",
                "payout_method.created",
                "verification.succeeded",
                "identity_profile.approved",
                "identity_profile.rejected",
                "identity_profile.needs_action",
                "identity_profile.updated",
                "payout_account.status_updated",
                "resolution_center_case.created",
                "resolution_center_case.updated",
                "resolution_center_case.decided",
                "product.created",
                "product.updated",
                "product.deleted",
                "product.published",
                "product.unpublished",
                "plan.created",
                "plan.updated",
                "plan.deleted",
                "shipment.created",
                "shipment.updated",
                "member.created",
                "ad_campaign.payment_failed",
                "chat.message.created",
                "chat.reaction.created",
                "payment.created",
                "payment.succeeded",
                "payment.failed",
                "payment.pending",
                "dispute.created",
                "dispute.updated",
                "refund.created",
                "refund.updated",
                "dispute_alert.created",
                "membership.cancel_at_period_end_changed",
                "membership_went_valid",
                "membership_went_invalid",
                "membership_metadata_updated",
                "resolution_created",
                "resolution_updated",
                "resolution_decided",
                "payment_affiliate_reward_created",
                "membership_experience_claimed",
                "app_membership_went_valid",
                "app_membership_went_invalid",
                "app_payment_created",
                "app_payment_succeeded",
                "app_payment_failed",
                "app_payment_pending",
                "app_membership_cancel_at_period_end_changed",
                "payment_created",
                "payment_succeeded",
                "payment_failed",
                "payment_pending",
                "dispute_created",
                "dispute_updated",
                "refund_created",
                "refund_updated",
                "dispute_alert_created",
                "membership_cancel_at_period_end_changed",
                "membership.went_valid",
                "membership.went_invalid",
                "membership.metadata_updated",
                "resolution.created",
                "resolution.updated",
                "resolution.decided",
                "payment.affiliate_reward_created",
                "membership.experience_claimed",
                "app_membership.went_valid",
                "app_membership.went_invalid",
                "app_payment.created",
                "app_payment.succeeded",
                "app_payment.failed",
                "app_payment.pending",
                "app_membership.cancel_at_period_end_changed",
            ]
        ]
        | Omit = omit,
        resource_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Webhook:
        """
        Creates a webhook endpoint that receives event notifications via HTTP POST.

        Args:
          url: The URL to send the webhook to.

          api_version_date: The dated API version (Api-Version-Date) to pin this webhook's payloads to. Omit
              to leave the webhook unpinned, tracking the current payload shape.

          child_resource_events: Whether to send events for child resources. For example, if the webhook is
              created for an account, enabling this sends events only from its connected
              accounts.

          enabled: Whether or not the webhook is enabled. Defaults to `true`.

          events: The events to send the webhook for, in dot form (for example
              `payment.succeeded`).

          resource_id: The account or app to create the webhook for. Defaults to the current account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/webhooks",
            body=maybe_transform(
                {
                    "url": url,
                    "api_version_date": api_version_date,
                    "child_resource_events": child_resource_events,
                    "enabled": enabled,
                    "events": events,
                    "resource_id": resource_id,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Webhook,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Retrieves the details of an existing webhook.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )

    def update(
        self,
        id: str,
        *,
        api_version_date: Optional[str] | Omit = omit,
        child_resource_events: bool | Omit = omit,
        enabled: bool | Omit = omit,
        events: List[
            Literal[
                "invoice.created",
                "invoice.marked_uncollectible",
                "invoice.paid",
                "invoice.past_due",
                "invoice.voided",
                "membership.activated",
                "membership.deactivated",
                "membership.trial_ending_soon",
                "entry.created",
                "entry.approved",
                "entry.denied",
                "entry.deleted",
                "export.completed",
                "export.failed",
                "setup_intent.requires_action",
                "setup_intent.succeeded",
                "setup_intent.canceled",
                "ledger_account.funds_available",
                "swap.completed",
                "deposit.succeeded",
                "transfer.created",
                "transfer.completed",
                "withdrawal.created",
                "withdrawal.updated",
                "card_transaction.created",
                "card_transaction.updated",
                "card_transaction.completed",
                "card_transaction.declined",
                "card_transaction.reversed",
                "card.created",
                "card.updated",
                "card.frozen",
                "card.canceled",
                "card_application.created",
                "card_application.updated",
                "card_application.approved",
                "card_application.denied",
                "course_lesson_interaction.completed",
                "payout_method.created",
                "verification.succeeded",
                "identity_profile.approved",
                "identity_profile.rejected",
                "identity_profile.needs_action",
                "identity_profile.updated",
                "payout_account.status_updated",
                "resolution_center_case.created",
                "resolution_center_case.updated",
                "resolution_center_case.decided",
                "product.created",
                "product.updated",
                "product.deleted",
                "product.published",
                "product.unpublished",
                "plan.created",
                "plan.updated",
                "plan.deleted",
                "shipment.created",
                "shipment.updated",
                "member.created",
                "ad_campaign.payment_failed",
                "chat.message.created",
                "chat.reaction.created",
                "payment.created",
                "payment.succeeded",
                "payment.failed",
                "payment.pending",
                "dispute.created",
                "dispute.updated",
                "refund.created",
                "refund.updated",
                "dispute_alert.created",
                "membership.cancel_at_period_end_changed",
                "membership_went_valid",
                "membership_went_invalid",
                "membership_metadata_updated",
                "resolution_created",
                "resolution_updated",
                "resolution_decided",
                "payment_affiliate_reward_created",
                "membership_experience_claimed",
                "app_membership_went_valid",
                "app_membership_went_invalid",
                "app_payment_created",
                "app_payment_succeeded",
                "app_payment_failed",
                "app_payment_pending",
                "app_membership_cancel_at_period_end_changed",
                "payment_created",
                "payment_succeeded",
                "payment_failed",
                "payment_pending",
                "dispute_created",
                "dispute_updated",
                "refund_created",
                "refund_updated",
                "dispute_alert_created",
                "membership_cancel_at_period_end_changed",
                "membership.went_valid",
                "membership.went_invalid",
                "membership.metadata_updated",
                "resolution.created",
                "resolution.updated",
                "resolution.decided",
                "payment.affiliate_reward_created",
                "membership.experience_claimed",
                "app_membership.went_valid",
                "app_membership.went_invalid",
                "app_payment.created",
                "app_payment.succeeded",
                "app_payment.failed",
                "app_payment.pending",
                "app_membership.cancel_at_period_end_changed",
            ]
        ]
        | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Webhook:
        """
        Updates a webhook endpoint's URL, subscribed events, pinned payload version, or
        enabled state.

        Args:
          api_version_date: The dated API version (Api-Version-Date) to pin this webhook's payloads to. Only
              valid for `v1` webhooks. Omit to leave the current pin unchanged, or pass `null`
              to unpin and track the current payload shape.

          child_resource_events: Whether or not to send events for child resources.

          enabled: Whether or not the webhook is enabled.

          events: The events to send the webhook for, in dot form (for example
              `payment.succeeded`).

          url: The URL to send the webhook to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/webhooks/{id}", id=id),
            body=maybe_transform(
                {
                    "api_version_date": api_version_date,
                    "child_resource_events": child_resource_events,
                    "enabled": enabled,
                    "events": events,
                    "url": url,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Webhook,
        )

    def list(
        self,
        *,
        account_id: str,
        after: str | Omit = omit,
        app_id: str | Omit = omit,
        before: str | Omit = omit,
        first: int | Omit = omit,
        has_failures: bool | Omit = omit,
        include_app_webhooks: bool | Omit = omit,
        last: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[WebhookListResponse]:
        """
        Returns a paginated list of webhook endpoints configured for an account, ordered
        by most recently created.

        Args:
          account_id: The unique identifier of the account to list webhooks for.

          after: A cursor; returns webhooks after this position.

          app_id: Only return webhooks attached to this app. Omit to list the account's own
              webhooks.

          before: A cursor; returns webhooks before this position.

          first: The number of webhooks to return (default 20, max 100).

          has_failures: Only return webhooks whose endpoint is currently failing — every delivery since
              the current failure streak began has been rejected. Clears as soon as a delivery
              succeeds.

          include_app_webhooks: Also return webhooks attached to the account's apps, not just the account's own.
              Cannot be combined with `app_id`.

          last: The number of webhooks to return from the end of the range.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/webhooks",
            page=SyncCursorPage[WebhookListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "app_id": app_id,
                        "before": before,
                        "first": first,
                        "has_failures": has_failures,
                        "include_app_webhooks": include_app_webhooks,
                        "last": last,
                    },
                    webhook_list_params.WebhookListParams,
                ),
            ),
            model=WebhookListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookDeleteResponse:
        """Permanently deletes a webhook endpoint.

        Returns `true` on success, matching the
        legacy proxy response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookDeleteResponse,
        )

    def list_deliveries(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        first: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[WebhookListDeliveriesResponse]:
        """
        Returns a paginated list of delivery attempts for a webhook, ordered by most
        recent first. Includes the request payload, response body, response code, and
        timing for each attempt.

        Args:
          after: A cursor; returns deliveries after this position.

          first: The number of deliveries to return (default 50, max 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/webhooks/{id}/deliveries", id=id),
            page=SyncCursorPage[WebhookListDeliveriesResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "first": first,
                    },
                    webhook_list_deliveries_params.WebhookListDeliveriesParams,
                ),
            ),
            model=WebhookListDeliveriesResponse,
        )

    def replay(
        self,
        id: str,
        *,
        sent_after: str,
        events: SequenceNotStr[str] | Omit = omit,
        failed_only: bool | Omit = omit,
        sent_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookReplayResponse:
        """
        Re-sends the webhook's past deliveries within a time window, optionally limited
        to specific events or to messages whose most recent delivery attempt failed.
        Fire and forget: nothing about the replay is stored, and each re-send appears as
        a new entry in the webhook's delivery log. Each matching message is re-sent once
        with its original `webhook-id`, so consumers that deduplicate are unaffected.
        Only available for enabled webhooks on API version v1; deliveries are retained
        for 30 days.

        Args:
          sent_after: Start of the delivery window to replay, as an ISO 8601 timestamp. Clamped to the
              30-day delivery retention.

          events: Only replay these event types, in dot form (for example `payment.succeeded`).
              Omit to include every event.

          failed_only: Only replay messages whose most recent delivery attempt in the window failed.
              Defaults to false. Best-effort: a message whose attempts span processing batches
              can still be re-sent — replays keep the original `webhook-id`, so consumers that
              deduplicate are unaffected.

          sent_before: End of the delivery window to replay, as an ISO 8601 timestamp. Defaults to now.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/webhooks/{id}/replay", id=id),
            body=maybe_transform(
                {
                    "sent_after": sent_after,
                    "events": events,
                    "failed_only": failed_only,
                    "sent_before": sent_before,
                },
                webhook_replay_params.WebhookReplayParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookReplayResponse,
        )

    def replay_delivery(
        self,
        delivery_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookReplayDeliveryResponse:
        """
        Re-sends the exact payload of a past delivery to the webhook's current URL and
        returns the delivery result. The replay keeps the original `webhook-id`, so
        consumers that deduplicate on it can drop events they already processed. Only
        available for enabled webhooks on API version v1; deliveries are retained for 30
        days.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return self._post(
            path_template("/webhooks/{id}/deliveries/{delivery_id}/replay", id=id, delivery_id=delivery_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookReplayDeliveryResponse,
        )

    def test(
        self,
        id: str,
        *,
        event: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookTestResponse:
        """
        Sends a sample payload for the given event to the webhook's URL and returns the
        delivery result.

        Args:
          event: The event to test the webhook for, in dot form (for example
              `payment.succeeded`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/webhooks/{id}/test", id=id),
            body=maybe_transform({"event": event}, webhook_test_params.WebhookTestParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookTestResponse,
        )

    def unwrap(self, payload: str, *, headers: Mapping[str, str], key: str | bytes | None = None) -> UnwrapWebhookEvent:
        try:
            from standardwebhooks import Webhook
        except ImportError as exc:
            raise WhopError("You need to install `whop-sdk[webhooks]` to use this method") from exc

        if key is None:
            key = self._client.webhook_key
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's webhook_key or passed in as an argument"
                )

        if not isinstance(headers, dict):
            headers = dict(headers)

        Webhook(key).verify(payload, headers)

        return cast(
            UnwrapWebhookEvent,
            construct_type(
                type_=UnwrapWebhookEvent,
                value=json.loads(payload),
            ),
        )


class AsyncWebhooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncWebhooksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        url: str,
        api_version_date: Optional[str] | Omit = omit,
        child_resource_events: bool | Omit = omit,
        enabled: bool | Omit = omit,
        events: List[
            Literal[
                "invoice.created",
                "invoice.marked_uncollectible",
                "invoice.paid",
                "invoice.past_due",
                "invoice.voided",
                "membership.activated",
                "membership.deactivated",
                "membership.trial_ending_soon",
                "entry.created",
                "entry.approved",
                "entry.denied",
                "entry.deleted",
                "export.completed",
                "export.failed",
                "setup_intent.requires_action",
                "setup_intent.succeeded",
                "setup_intent.canceled",
                "ledger_account.funds_available",
                "swap.completed",
                "deposit.succeeded",
                "transfer.created",
                "transfer.completed",
                "withdrawal.created",
                "withdrawal.updated",
                "card_transaction.created",
                "card_transaction.updated",
                "card_transaction.completed",
                "card_transaction.declined",
                "card_transaction.reversed",
                "card.created",
                "card.updated",
                "card.frozen",
                "card.canceled",
                "card_application.created",
                "card_application.updated",
                "card_application.approved",
                "card_application.denied",
                "course_lesson_interaction.completed",
                "payout_method.created",
                "verification.succeeded",
                "identity_profile.approved",
                "identity_profile.rejected",
                "identity_profile.needs_action",
                "identity_profile.updated",
                "payout_account.status_updated",
                "resolution_center_case.created",
                "resolution_center_case.updated",
                "resolution_center_case.decided",
                "product.created",
                "product.updated",
                "product.deleted",
                "product.published",
                "product.unpublished",
                "plan.created",
                "plan.updated",
                "plan.deleted",
                "shipment.created",
                "shipment.updated",
                "member.created",
                "ad_campaign.payment_failed",
                "chat.message.created",
                "chat.reaction.created",
                "payment.created",
                "payment.succeeded",
                "payment.failed",
                "payment.pending",
                "dispute.created",
                "dispute.updated",
                "refund.created",
                "refund.updated",
                "dispute_alert.created",
                "membership.cancel_at_period_end_changed",
                "membership_went_valid",
                "membership_went_invalid",
                "membership_metadata_updated",
                "resolution_created",
                "resolution_updated",
                "resolution_decided",
                "payment_affiliate_reward_created",
                "membership_experience_claimed",
                "app_membership_went_valid",
                "app_membership_went_invalid",
                "app_payment_created",
                "app_payment_succeeded",
                "app_payment_failed",
                "app_payment_pending",
                "app_membership_cancel_at_period_end_changed",
                "payment_created",
                "payment_succeeded",
                "payment_failed",
                "payment_pending",
                "dispute_created",
                "dispute_updated",
                "refund_created",
                "refund_updated",
                "dispute_alert_created",
                "membership_cancel_at_period_end_changed",
                "membership.went_valid",
                "membership.went_invalid",
                "membership.metadata_updated",
                "resolution.created",
                "resolution.updated",
                "resolution.decided",
                "payment.affiliate_reward_created",
                "membership.experience_claimed",
                "app_membership.went_valid",
                "app_membership.went_invalid",
                "app_payment.created",
                "app_payment.succeeded",
                "app_payment.failed",
                "app_payment.pending",
                "app_membership.cancel_at_period_end_changed",
            ]
        ]
        | Omit = omit,
        resource_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Webhook:
        """
        Creates a webhook endpoint that receives event notifications via HTTP POST.

        Args:
          url: The URL to send the webhook to.

          api_version_date: The dated API version (Api-Version-Date) to pin this webhook's payloads to. Omit
              to leave the webhook unpinned, tracking the current payload shape.

          child_resource_events: Whether to send events for child resources. For example, if the webhook is
              created for an account, enabling this sends events only from its connected
              accounts.

          enabled: Whether or not the webhook is enabled. Defaults to `true`.

          events: The events to send the webhook for, in dot form (for example
              `payment.succeeded`).

          resource_id: The account or app to create the webhook for. Defaults to the current account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/webhooks",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "api_version_date": api_version_date,
                    "child_resource_events": child_resource_events,
                    "enabled": enabled,
                    "events": events,
                    "resource_id": resource_id,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Webhook,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Retrieves the details of an existing webhook.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )

    async def update(
        self,
        id: str,
        *,
        api_version_date: Optional[str] | Omit = omit,
        child_resource_events: bool | Omit = omit,
        enabled: bool | Omit = omit,
        events: List[
            Literal[
                "invoice.created",
                "invoice.marked_uncollectible",
                "invoice.paid",
                "invoice.past_due",
                "invoice.voided",
                "membership.activated",
                "membership.deactivated",
                "membership.trial_ending_soon",
                "entry.created",
                "entry.approved",
                "entry.denied",
                "entry.deleted",
                "export.completed",
                "export.failed",
                "setup_intent.requires_action",
                "setup_intent.succeeded",
                "setup_intent.canceled",
                "ledger_account.funds_available",
                "swap.completed",
                "deposit.succeeded",
                "transfer.created",
                "transfer.completed",
                "withdrawal.created",
                "withdrawal.updated",
                "card_transaction.created",
                "card_transaction.updated",
                "card_transaction.completed",
                "card_transaction.declined",
                "card_transaction.reversed",
                "card.created",
                "card.updated",
                "card.frozen",
                "card.canceled",
                "card_application.created",
                "card_application.updated",
                "card_application.approved",
                "card_application.denied",
                "course_lesson_interaction.completed",
                "payout_method.created",
                "verification.succeeded",
                "identity_profile.approved",
                "identity_profile.rejected",
                "identity_profile.needs_action",
                "identity_profile.updated",
                "payout_account.status_updated",
                "resolution_center_case.created",
                "resolution_center_case.updated",
                "resolution_center_case.decided",
                "product.created",
                "product.updated",
                "product.deleted",
                "product.published",
                "product.unpublished",
                "plan.created",
                "plan.updated",
                "plan.deleted",
                "shipment.created",
                "shipment.updated",
                "member.created",
                "ad_campaign.payment_failed",
                "chat.message.created",
                "chat.reaction.created",
                "payment.created",
                "payment.succeeded",
                "payment.failed",
                "payment.pending",
                "dispute.created",
                "dispute.updated",
                "refund.created",
                "refund.updated",
                "dispute_alert.created",
                "membership.cancel_at_period_end_changed",
                "membership_went_valid",
                "membership_went_invalid",
                "membership_metadata_updated",
                "resolution_created",
                "resolution_updated",
                "resolution_decided",
                "payment_affiliate_reward_created",
                "membership_experience_claimed",
                "app_membership_went_valid",
                "app_membership_went_invalid",
                "app_payment_created",
                "app_payment_succeeded",
                "app_payment_failed",
                "app_payment_pending",
                "app_membership_cancel_at_period_end_changed",
                "payment_created",
                "payment_succeeded",
                "payment_failed",
                "payment_pending",
                "dispute_created",
                "dispute_updated",
                "refund_created",
                "refund_updated",
                "dispute_alert_created",
                "membership_cancel_at_period_end_changed",
                "membership.went_valid",
                "membership.went_invalid",
                "membership.metadata_updated",
                "resolution.created",
                "resolution.updated",
                "resolution.decided",
                "payment.affiliate_reward_created",
                "membership.experience_claimed",
                "app_membership.went_valid",
                "app_membership.went_invalid",
                "app_payment.created",
                "app_payment.succeeded",
                "app_payment.failed",
                "app_payment.pending",
                "app_membership.cancel_at_period_end_changed",
            ]
        ]
        | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Webhook:
        """
        Updates a webhook endpoint's URL, subscribed events, pinned payload version, or
        enabled state.

        Args:
          api_version_date: The dated API version (Api-Version-Date) to pin this webhook's payloads to. Only
              valid for `v1` webhooks. Omit to leave the current pin unchanged, or pass `null`
              to unpin and track the current payload shape.

          child_resource_events: Whether or not to send events for child resources.

          enabled: Whether or not the webhook is enabled.

          events: The events to send the webhook for, in dot form (for example
              `payment.succeeded`).

          url: The URL to send the webhook to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/webhooks/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "api_version_date": api_version_date,
                    "child_resource_events": child_resource_events,
                    "enabled": enabled,
                    "events": events,
                    "url": url,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Webhook,
        )

    def list(
        self,
        *,
        account_id: str,
        after: str | Omit = omit,
        app_id: str | Omit = omit,
        before: str | Omit = omit,
        first: int | Omit = omit,
        has_failures: bool | Omit = omit,
        include_app_webhooks: bool | Omit = omit,
        last: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WebhookListResponse, AsyncCursorPage[WebhookListResponse]]:
        """
        Returns a paginated list of webhook endpoints configured for an account, ordered
        by most recently created.

        Args:
          account_id: The unique identifier of the account to list webhooks for.

          after: A cursor; returns webhooks after this position.

          app_id: Only return webhooks attached to this app. Omit to list the account's own
              webhooks.

          before: A cursor; returns webhooks before this position.

          first: The number of webhooks to return (default 20, max 100).

          has_failures: Only return webhooks whose endpoint is currently failing — every delivery since
              the current failure streak began has been rejected. Clears as soon as a delivery
              succeeds.

          include_app_webhooks: Also return webhooks attached to the account's apps, not just the account's own.
              Cannot be combined with `app_id`.

          last: The number of webhooks to return from the end of the range.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/webhooks",
            page=AsyncCursorPage[WebhookListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "app_id": app_id,
                        "before": before,
                        "first": first,
                        "has_failures": has_failures,
                        "include_app_webhooks": include_app_webhooks,
                        "last": last,
                    },
                    webhook_list_params.WebhookListParams,
                ),
            ),
            model=WebhookListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookDeleteResponse:
        """Permanently deletes a webhook endpoint.

        Returns `true` on success, matching the
        legacy proxy response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookDeleteResponse,
        )

    def list_deliveries(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        first: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WebhookListDeliveriesResponse, AsyncCursorPage[WebhookListDeliveriesResponse]]:
        """
        Returns a paginated list of delivery attempts for a webhook, ordered by most
        recent first. Includes the request payload, response body, response code, and
        timing for each attempt.

        Args:
          after: A cursor; returns deliveries after this position.

          first: The number of deliveries to return (default 50, max 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/webhooks/{id}/deliveries", id=id),
            page=AsyncCursorPage[WebhookListDeliveriesResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "first": first,
                    },
                    webhook_list_deliveries_params.WebhookListDeliveriesParams,
                ),
            ),
            model=WebhookListDeliveriesResponse,
        )

    async def replay(
        self,
        id: str,
        *,
        sent_after: str,
        events: SequenceNotStr[str] | Omit = omit,
        failed_only: bool | Omit = omit,
        sent_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookReplayResponse:
        """
        Re-sends the webhook's past deliveries within a time window, optionally limited
        to specific events or to messages whose most recent delivery attempt failed.
        Fire and forget: nothing about the replay is stored, and each re-send appears as
        a new entry in the webhook's delivery log. Each matching message is re-sent once
        with its original `webhook-id`, so consumers that deduplicate are unaffected.
        Only available for enabled webhooks on API version v1; deliveries are retained
        for 30 days.

        Args:
          sent_after: Start of the delivery window to replay, as an ISO 8601 timestamp. Clamped to the
              30-day delivery retention.

          events: Only replay these event types, in dot form (for example `payment.succeeded`).
              Omit to include every event.

          failed_only: Only replay messages whose most recent delivery attempt in the window failed.
              Defaults to false. Best-effort: a message whose attempts span processing batches
              can still be re-sent — replays keep the original `webhook-id`, so consumers that
              deduplicate are unaffected.

          sent_before: End of the delivery window to replay, as an ISO 8601 timestamp. Defaults to now.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/webhooks/{id}/replay", id=id),
            body=await async_maybe_transform(
                {
                    "sent_after": sent_after,
                    "events": events,
                    "failed_only": failed_only,
                    "sent_before": sent_before,
                },
                webhook_replay_params.WebhookReplayParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookReplayResponse,
        )

    async def replay_delivery(
        self,
        delivery_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookReplayDeliveryResponse:
        """
        Re-sends the exact payload of a past delivery to the webhook's current URL and
        returns the delivery result. The replay keeps the original `webhook-id`, so
        consumers that deduplicate on it can drop events they already processed. Only
        available for enabled webhooks on API version v1; deliveries are retained for 30
        days.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return await self._post(
            path_template("/webhooks/{id}/deliveries/{delivery_id}/replay", id=id, delivery_id=delivery_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookReplayDeliveryResponse,
        )

    async def test(
        self,
        id: str,
        *,
        event: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookTestResponse:
        """
        Sends a sample payload for the given event to the webhook's URL and returns the
        delivery result.

        Args:
          event: The event to test the webhook for, in dot form (for example
              `payment.succeeded`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/webhooks/{id}/test", id=id),
            body=await async_maybe_transform({"event": event}, webhook_test_params.WebhookTestParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookTestResponse,
        )

    def unwrap(self, payload: str, *, headers: Mapping[str, str], key: str | bytes | None = None) -> UnwrapWebhookEvent:
        try:
            from standardwebhooks import Webhook
        except ImportError as exc:
            raise WhopError("You need to install `whop-sdk[webhooks]` to use this method") from exc

        if key is None:
            key = self._client.webhook_key
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's webhook_key or passed in as an argument"
                )

        if not isinstance(headers, dict):
            headers = dict(headers)

        Webhook(key).verify(payload, headers)

        return cast(
            UnwrapWebhookEvent,
            construct_type(
                type_=UnwrapWebhookEvent,
                value=json.loads(payload),
            ),
        )


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_raw_response_wrapper(
            webhooks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            webhooks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = to_raw_response_wrapper(
            webhooks.delete,
        )
        self.list_deliveries = to_raw_response_wrapper(
            webhooks.list_deliveries,
        )
        self.replay = to_raw_response_wrapper(
            webhooks.replay,
        )
        self.replay_delivery = to_raw_response_wrapper(
            webhooks.replay_delivery,
        )
        self.test = to_raw_response_wrapper(
            webhooks.test,
        )


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_raw_response_wrapper(
            webhooks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            webhooks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            webhooks.delete,
        )
        self.list_deliveries = async_to_raw_response_wrapper(
            webhooks.list_deliveries,
        )
        self.replay = async_to_raw_response_wrapper(
            webhooks.replay,
        )
        self.replay_delivery = async_to_raw_response_wrapper(
            webhooks.replay_delivery,
        )
        self.test = async_to_raw_response_wrapper(
            webhooks.test,
        )


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_streamed_response_wrapper(
            webhooks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            webhooks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.list_deliveries = to_streamed_response_wrapper(
            webhooks.list_deliveries,
        )
        self.replay = to_streamed_response_wrapper(
            webhooks.replay,
        )
        self.replay_delivery = to_streamed_response_wrapper(
            webhooks.replay_delivery,
        )
        self.test = to_streamed_response_wrapper(
            webhooks.test,
        )


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_streamed_response_wrapper(
            webhooks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            webhooks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.list_deliveries = async_to_streamed_response_wrapper(
            webhooks.list_deliveries,
        )
        self.replay = async_to_streamed_response_wrapper(
            webhooks.replay,
        )
        self.replay_delivery = async_to_streamed_response_wrapper(
            webhooks.replay_delivery,
        )
        self.test = async_to_streamed_response_wrapper(
            webhooks.test,
        )
