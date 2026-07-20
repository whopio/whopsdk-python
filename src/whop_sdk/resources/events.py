# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import event_list_params, event_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.event_list_response import EventListResponse
from ..types.event_create_response import EventCreateResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    """
    An Event records conversion or engagement activity for an account, such as page views, purchases, or leads. Each event ties the action to the [person](/api-reference/beta/people/person) who took it, so activity can be attributed to the ads and links that drove it.

    Use the Events API to send new tracking events, list recent identity-linked events for an account, and inspect the events recorded for a person.
    """

    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        event_name: str,
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
        context: Optional[event_create_params.Context] | Omit = omit,
        currency: Optional[
            Literal[
                "usd",
                "sgd",
                "inr",
                "aud",
                "brl",
                "cad",
                "dkk",
                "eur",
                "nok",
                "gbp",
                "sek",
                "chf",
                "hkd",
                "huf",
                "jpy",
                "mxn",
                "myr",
                "pln",
                "czk",
                "nzd",
                "aed",
                "eth",
                "ape",
                "cop",
                "ron",
                "thb",
                "bgn",
                "idr",
                "dop",
                "php",
                "try",
                "krw",
                "twd",
                "vnd",
                "pkr",
                "clp",
                "uyu",
                "ars",
                "zar",
                "dzd",
                "tnd",
                "mad",
                "kes",
                "kwd",
                "jod",
                "all",
                "xcd",
                "amd",
                "bsd",
                "bhd",
                "bob",
                "bam",
                "khr",
                "crc",
                "xof",
                "egp",
                "etb",
                "gmd",
                "ghs",
                "gtq",
                "gyd",
                "ils",
                "jmd",
                "mop",
                "mga",
                "mur",
                "mdl",
                "mnt",
                "nad",
                "ngn",
                "mkd",
                "omr",
                "pyg",
                "pen",
                "qar",
                "rwf",
                "sar",
                "rsd",
                "lkr",
                "tzs",
                "ttd",
                "uzs",
                "rub",
                "btc",
                "cny",
                "usdt",
                "kzt",
                "awg",
                "whop_usd",
                "xau",
            ]
        ]
        | Omit = omit,
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
        user: Optional[event_create_params.User] | Omit = omit,
        value: Optional[float] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventCreateResponse:
        """
        Tracks a conversion or engagement event for an account.

        Args:
          account_id: The account to associate with this event.

          event_name: The type of event.

              Use a standard event (lead, submit_application, contact, complete_registration,
              schedule, view_content, add_to_cart) or pass your own name directly for a custom
              event.

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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/events",
            body=maybe_transform(
                {
                    "account_id": account_id,
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
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventCreateResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        first: int | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        person_id: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[EventListResponse]:
        """Lists pixel events, most recent first.

        Pass person_id for one person's journey,
        or omit it to list identity-linked events for an account within an explicit time
        range. Events are shaped like the POST /events intake: attribution in context,
        identity in user.

        Args:
          account_id: The ID of the account, which will look like biz\\__******\\********. Optional for
              account API keys; required for credentials that can access multiple accounts.

          after: A cursor for fetching events after a previous page.

          before: A cursor for fetching events before a later page.

          first: The number of events to return.

          from_: Start of the time range as an ISO 8601 timestamp. Required when person_id is
              omitted.

          person_id: The ID of the person. Omit to list recent identity-linked events for the
              account.

          to: End of the time range as an ISO 8601 timestamp. Required when person_id is
              omitted; otherwise defaults to now.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events",
            page=SyncCursorPage[EventListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "before": before,
                        "first": first,
                        "from_": from_,
                        "person_id": person_id,
                        "to": to,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=EventListResponse,
        )


class AsyncEventsResource(AsyncAPIResource):
    """
    An Event records conversion or engagement activity for an account, such as page views, purchases, or leads. Each event ties the action to the [person](/api-reference/beta/people/person) who took it, so activity can be attributed to the ads and links that drove it.

    Use the Events API to send new tracking events, list recent identity-linked events for an account, and inspect the events recorded for a person.
    """

    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        event_name: str,
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
        context: Optional[event_create_params.Context] | Omit = omit,
        currency: Optional[
            Literal[
                "usd",
                "sgd",
                "inr",
                "aud",
                "brl",
                "cad",
                "dkk",
                "eur",
                "nok",
                "gbp",
                "sek",
                "chf",
                "hkd",
                "huf",
                "jpy",
                "mxn",
                "myr",
                "pln",
                "czk",
                "nzd",
                "aed",
                "eth",
                "ape",
                "cop",
                "ron",
                "thb",
                "bgn",
                "idr",
                "dop",
                "php",
                "try",
                "krw",
                "twd",
                "vnd",
                "pkr",
                "clp",
                "uyu",
                "ars",
                "zar",
                "dzd",
                "tnd",
                "mad",
                "kes",
                "kwd",
                "jod",
                "all",
                "xcd",
                "amd",
                "bsd",
                "bhd",
                "bob",
                "bam",
                "khr",
                "crc",
                "xof",
                "egp",
                "etb",
                "gmd",
                "ghs",
                "gtq",
                "gyd",
                "ils",
                "jmd",
                "mop",
                "mga",
                "mur",
                "mdl",
                "mnt",
                "nad",
                "ngn",
                "mkd",
                "omr",
                "pyg",
                "pen",
                "qar",
                "rwf",
                "sar",
                "rsd",
                "lkr",
                "tzs",
                "ttd",
                "uzs",
                "rub",
                "btc",
                "cny",
                "usdt",
                "kzt",
                "awg",
                "whop_usd",
                "xau",
            ]
        ]
        | Omit = omit,
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
        user: Optional[event_create_params.User] | Omit = omit,
        value: Optional[float] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventCreateResponse:
        """
        Tracks a conversion or engagement event for an account.

        Args:
          account_id: The account to associate with this event.

          event_name: The type of event.

              Use a standard event (lead, submit_application, contact, complete_registration,
              schedule, view_content, add_to_cart) or pass your own name directly for a custom
              event.

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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/events",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
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
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventCreateResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        first: int | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        person_id: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EventListResponse, AsyncCursorPage[EventListResponse]]:
        """Lists pixel events, most recent first.

        Pass person_id for one person's journey,
        or omit it to list identity-linked events for an account within an explicit time
        range. Events are shaped like the POST /events intake: attribution in context,
        identity in user.

        Args:
          account_id: The ID of the account, which will look like biz\\__******\\********. Optional for
              account API keys; required for credentials that can access multiple accounts.

          after: A cursor for fetching events after a previous page.

          before: A cursor for fetching events before a later page.

          first: The number of events to return.

          from_: Start of the time range as an ISO 8601 timestamp. Required when person_id is
              omitted.

          person_id: The ID of the person. Omit to list recent identity-linked events for the
              account.

          to: End of the time range as an ISO 8601 timestamp. Required when person_id is
              omitted; otherwise defaults to now.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events",
            page=AsyncCursorPage[EventListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "before": before,
                        "first": first,
                        "from_": from_,
                        "person_id": person_id,
                        "to": to,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=EventListResponse,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create = to_raw_response_wrapper(
            events.create,
        )
        self.list = to_raw_response_wrapper(
            events.list,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create = async_to_raw_response_wrapper(
            events.create,
        )
        self.list = async_to_raw_response_wrapper(
            events.list,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create = to_streamed_response_wrapper(
            events.create,
        )
        self.list = to_streamed_response_wrapper(
            events.list,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create = async_to_streamed_response_wrapper(
            events.create,
        )
        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
