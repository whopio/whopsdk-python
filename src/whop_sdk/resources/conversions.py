# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import conversion_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shared.currency import Currency
from ..types.conversion_create_response import ConversionCreateResponse

__all__ = ["ConversionsResource", "AsyncConversionsResource"]


class ConversionsResource(SyncAPIResource):
    """Conversions"""

    @cached_property
    def with_raw_response(self) -> ConversionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return ConversionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return ConversionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_id: str,
        event_name: Literal[
            "lead",
            "submit_application",
            "contact",
            "complete_registration",
            "schedule",
            "view_content",
            "add_to_cart",
            "custom",
            "page",
        ],
        action_source: Optional[
            Literal[
                "email",
                "website",
                "app",
                "phone_call",
                "chat",
                "physical_store",
                "system_generated",
                "business_messaging",
                "other",
            ]
        ]
        | Omit = omit,
        context: Optional[conversion_create_params.Context] | Omit = omit,
        currency: Optional[Currency] | Omit = omit,
        custom_name: Optional[str] | Omit = omit,
        duration: Optional[int] | Omit = omit,
        event_id: Optional[str] | Omit = omit,
        event_time: Union[str, datetime, None] | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        referrer_url: Optional[str] | Omit = omit,
        resumed: Optional[bool] | Omit = omit,
        source: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        url: Optional[str] | Omit = omit,
        user: Optional[conversion_create_params.User] | Omit = omit,
        value: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversionCreateResponse:
        """
        Track a conversion or engagement event for a company.

        Required permissions:

        - `event:create`

        Args:
          company_id: The company to associate with this event.

          event_name: The type of event.

          action_source: The channel where an event originated

          context: Tracking and attribution context.

          currency: The available currencies on the platform

          custom_name: Custom event name when event_name is 'custom'. Maximum 35 chars for this value.

          duration: For 'leave' events: milliseconds the visitor spent on the page.

          event_id: Client-provided identifier for deduplication. Generated if omitted.

          event_time: When the event occurred. Defaults to now.

          plan_id: The plan associated with the event.

          product_id: The product associated with the event.

          referrer_url: The referring URL.

          resumed: For 'page' events: true when the page was restored from the back/forward cache.

          source: For 'identify' events: where the identity was captured (url, form, manual,
              iframe).

          title: For 'page' events: the document title.

          url: The URL where the event occurred.

          user: User identity and profile data.

          value: Monetary value associated with the event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/conversions",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "event_name": event_name,
                    "action_source": action_source,
                    "context": context,
                    "currency": currency,
                    "custom_name": custom_name,
                    "duration": duration,
                    "event_id": event_id,
                    "event_time": event_time,
                    "plan_id": plan_id,
                    "product_id": product_id,
                    "referrer_url": referrer_url,
                    "resumed": resumed,
                    "source": source,
                    "title": title,
                    "url": url,
                    "user": user,
                    "value": value,
                },
                conversion_create_params.ConversionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversionCreateResponse,
        )


class AsyncConversionsResource(AsyncAPIResource):
    """Conversions"""

    @cached_property
    def with_raw_response(self) -> AsyncConversionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncConversionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_id: str,
        event_name: Literal[
            "lead",
            "submit_application",
            "contact",
            "complete_registration",
            "schedule",
            "view_content",
            "add_to_cart",
            "custom",
            "page",
        ],
        action_source: Optional[
            Literal[
                "email",
                "website",
                "app",
                "phone_call",
                "chat",
                "physical_store",
                "system_generated",
                "business_messaging",
                "other",
            ]
        ]
        | Omit = omit,
        context: Optional[conversion_create_params.Context] | Omit = omit,
        currency: Optional[Currency] | Omit = omit,
        custom_name: Optional[str] | Omit = omit,
        duration: Optional[int] | Omit = omit,
        event_id: Optional[str] | Omit = omit,
        event_time: Union[str, datetime, None] | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        referrer_url: Optional[str] | Omit = omit,
        resumed: Optional[bool] | Omit = omit,
        source: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        url: Optional[str] | Omit = omit,
        user: Optional[conversion_create_params.User] | Omit = omit,
        value: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversionCreateResponse:
        """
        Track a conversion or engagement event for a company.

        Required permissions:

        - `event:create`

        Args:
          company_id: The company to associate with this event.

          event_name: The type of event.

          action_source: The channel where an event originated

          context: Tracking and attribution context.

          currency: The available currencies on the platform

          custom_name: Custom event name when event_name is 'custom'. Maximum 35 chars for this value.

          duration: For 'leave' events: milliseconds the visitor spent on the page.

          event_id: Client-provided identifier for deduplication. Generated if omitted.

          event_time: When the event occurred. Defaults to now.

          plan_id: The plan associated with the event.

          product_id: The product associated with the event.

          referrer_url: The referring URL.

          resumed: For 'page' events: true when the page was restored from the back/forward cache.

          source: For 'identify' events: where the identity was captured (url, form, manual,
              iframe).

          title: For 'page' events: the document title.

          url: The URL where the event occurred.

          user: User identity and profile data.

          value: Monetary value associated with the event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/conversions",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "event_name": event_name,
                    "action_source": action_source,
                    "context": context,
                    "currency": currency,
                    "custom_name": custom_name,
                    "duration": duration,
                    "event_id": event_id,
                    "event_time": event_time,
                    "plan_id": plan_id,
                    "product_id": product_id,
                    "referrer_url": referrer_url,
                    "resumed": resumed,
                    "source": source,
                    "title": title,
                    "url": url,
                    "user": user,
                    "value": value,
                },
                conversion_create_params.ConversionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversionCreateResponse,
        )


class ConversionsResourceWithRawResponse:
    def __init__(self, conversions: ConversionsResource) -> None:
        self._conversions = conversions

        self.create = to_raw_response_wrapper(
            conversions.create,
        )


class AsyncConversionsResourceWithRawResponse:
    def __init__(self, conversions: AsyncConversionsResource) -> None:
        self._conversions = conversions

        self.create = async_to_raw_response_wrapper(
            conversions.create,
        )


class ConversionsResourceWithStreamingResponse:
    def __init__(self, conversions: ConversionsResource) -> None:
        self._conversions = conversions

        self.create = to_streamed_response_wrapper(
            conversions.create,
        )


class AsyncConversionsResourceWithStreamingResponse:
    def __init__(self, conversions: AsyncConversionsResource) -> None:
        self._conversions = conversions

        self.create = async_to_streamed_response_wrapper(
            conversions.create,
        )
