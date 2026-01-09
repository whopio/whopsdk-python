# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import json
from typing import List, Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import webhook_list_params, webhook_create_params, webhook_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
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
from ..types.unwrap_webhook_event import UnwrapWebhookEvent
from ..types.webhook_list_response import WebhookListResponse
from ..types.webhook_create_response import WebhookCreateResponse
from ..types.webhook_delete_response import WebhookDeleteResponse
from ..types.webhook_update_response import WebhookUpdateResponse
from ..types.webhook_retrieve_response import WebhookRetrieveResponse

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
        api_version: Optional[Literal["v1", "v2", "v5"]] | Omit = omit,
        child_resource_events: Optional[bool] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        events: Optional[
            List[
                Literal[
                    "invoice.created",
                    "invoice.paid",
                    "invoice.past_due",
                    "invoice.voided",
                    "membership.activated",
                    "membership.deactivated",
                    "entry.created",
                    "entry.approved",
                    "entry.denied",
                    "entry.deleted",
                    "setup_intent.requires_action",
                    "setup_intent.succeeded",
                    "setup_intent.canceled",
                    "withdrawal.created",
                    "withdrawal.updated",
                    "course_lesson_interaction.completed",
                    "payout_method.created",
                    "verification.succeeded",
                    "payment.created",
                    "payment.succeeded",
                    "payment.failed",
                    "payment.pending",
                    "dispute.created",
                    "dispute.updated",
                    "refund.created",
                    "refund.updated",
                    "membership.cancel_at_period_end_changed",
                ]
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
    ) -> WebhookCreateResponse:
        """
        Creates a new webhook

        Required permissions:

        - `developer:manage_webhook`

        Args:
          url: The URL to send the webhook to.

          api_version: The different API versions

          child_resource_events: Whether or not to send events for child resources. For example, if the webhook
              is created for a Company, enabling this will only send events from the Company's
              sub-merchants (child companies).

          enabled: Whether or not the webhook is enabled.

          events: The events to send the webhook for.

          resource_id: The resource to create the webhook for. By default this will use current company

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/webhooks",
            body=maybe_transform(
                {
                    "url": url,
                    "api_version": api_version,
                    "child_resource_events": child_resource_events,
                    "enabled": enabled,
                    "events": events,
                    "resource_id": resource_id,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookCreateResponse,
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
    ) -> WebhookRetrieveResponse:
        """
        Retrieves a webhook by ID

        Required permissions:

        - `developer:manage_webhook`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/webhooks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        api_version: Optional[Literal["v1", "v2", "v5"]] | Omit = omit,
        child_resource_events: Optional[bool] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        events: Optional[
            List[
                Literal[
                    "invoice.created",
                    "invoice.paid",
                    "invoice.past_due",
                    "invoice.voided",
                    "membership.activated",
                    "membership.deactivated",
                    "entry.created",
                    "entry.approved",
                    "entry.denied",
                    "entry.deleted",
                    "setup_intent.requires_action",
                    "setup_intent.succeeded",
                    "setup_intent.canceled",
                    "withdrawal.created",
                    "withdrawal.updated",
                    "course_lesson_interaction.completed",
                    "payout_method.created",
                    "verification.succeeded",
                    "payment.created",
                    "payment.succeeded",
                    "payment.failed",
                    "payment.pending",
                    "dispute.created",
                    "dispute.updated",
                    "refund.created",
                    "refund.updated",
                    "membership.cancel_at_period_end_changed",
                ]
            ]
        ]
        | Omit = omit,
        url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookUpdateResponse:
        """
        Updates a webhook

        Required permissions:

        - `developer:manage_webhook`

        Args:
          api_version: The different API versions

          child_resource_events: Whether or not to send events for child resources.

          enabled: Whether or not the webhook is enabled.

          events: The events to send the webhook for.

          url: The URL to send the webhook to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/webhooks/{id}",
            body=maybe_transform(
                {
                    "api_version": api_version,
                    "child_resource_events": child_resource_events,
                    "enabled": enabled,
                    "events": events,
                    "url": url,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookUpdateResponse,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[WebhookListResponse]:
        """
        Lists webhooks for a company

        Required permissions:

        - `developer:manage_webhook`

        Args:
          company_id: The ID of the company to list webhooks for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

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
                        "company_id": company_id,
                        "after": after,
                        "before": before,
                        "first": first,
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
    ) -> WebhookDeleteResponse:
        """
        Deletes a webhook

        Required permissions:

        - `developer:manage_webhook`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/webhooks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeleteResponse,
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
        api_version: Optional[Literal["v1", "v2", "v5"]] | Omit = omit,
        child_resource_events: Optional[bool] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        events: Optional[
            List[
                Literal[
                    "invoice.created",
                    "invoice.paid",
                    "invoice.past_due",
                    "invoice.voided",
                    "membership.activated",
                    "membership.deactivated",
                    "entry.created",
                    "entry.approved",
                    "entry.denied",
                    "entry.deleted",
                    "setup_intent.requires_action",
                    "setup_intent.succeeded",
                    "setup_intent.canceled",
                    "withdrawal.created",
                    "withdrawal.updated",
                    "course_lesson_interaction.completed",
                    "payout_method.created",
                    "verification.succeeded",
                    "payment.created",
                    "payment.succeeded",
                    "payment.failed",
                    "payment.pending",
                    "dispute.created",
                    "dispute.updated",
                    "refund.created",
                    "refund.updated",
                    "membership.cancel_at_period_end_changed",
                ]
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
    ) -> WebhookCreateResponse:
        """
        Creates a new webhook

        Required permissions:

        - `developer:manage_webhook`

        Args:
          url: The URL to send the webhook to.

          api_version: The different API versions

          child_resource_events: Whether or not to send events for child resources. For example, if the webhook
              is created for a Company, enabling this will only send events from the Company's
              sub-merchants (child companies).

          enabled: Whether or not the webhook is enabled.

          events: The events to send the webhook for.

          resource_id: The resource to create the webhook for. By default this will use current company

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/webhooks",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "api_version": api_version,
                    "child_resource_events": child_resource_events,
                    "enabled": enabled,
                    "events": events,
                    "resource_id": resource_id,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookCreateResponse,
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
    ) -> WebhookRetrieveResponse:
        """
        Retrieves a webhook by ID

        Required permissions:

        - `developer:manage_webhook`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/webhooks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        api_version: Optional[Literal["v1", "v2", "v5"]] | Omit = omit,
        child_resource_events: Optional[bool] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        events: Optional[
            List[
                Literal[
                    "invoice.created",
                    "invoice.paid",
                    "invoice.past_due",
                    "invoice.voided",
                    "membership.activated",
                    "membership.deactivated",
                    "entry.created",
                    "entry.approved",
                    "entry.denied",
                    "entry.deleted",
                    "setup_intent.requires_action",
                    "setup_intent.succeeded",
                    "setup_intent.canceled",
                    "withdrawal.created",
                    "withdrawal.updated",
                    "course_lesson_interaction.completed",
                    "payout_method.created",
                    "verification.succeeded",
                    "payment.created",
                    "payment.succeeded",
                    "payment.failed",
                    "payment.pending",
                    "dispute.created",
                    "dispute.updated",
                    "refund.created",
                    "refund.updated",
                    "membership.cancel_at_period_end_changed",
                ]
            ]
        ]
        | Omit = omit,
        url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookUpdateResponse:
        """
        Updates a webhook

        Required permissions:

        - `developer:manage_webhook`

        Args:
          api_version: The different API versions

          child_resource_events: Whether or not to send events for child resources.

          enabled: Whether or not the webhook is enabled.

          events: The events to send the webhook for.

          url: The URL to send the webhook to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/webhooks/{id}",
            body=await async_maybe_transform(
                {
                    "api_version": api_version,
                    "child_resource_events": child_resource_events,
                    "enabled": enabled,
                    "events": events,
                    "url": url,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookUpdateResponse,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WebhookListResponse, AsyncCursorPage[WebhookListResponse]]:
        """
        Lists webhooks for a company

        Required permissions:

        - `developer:manage_webhook`

        Args:
          company_id: The ID of the company to list webhooks for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

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
                        "company_id": company_id,
                        "after": after,
                        "before": before,
                        "first": first,
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
    ) -> WebhookDeleteResponse:
        """
        Deletes a webhook

        Required permissions:

        - `developer:manage_webhook`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/webhooks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeleteResponse,
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
