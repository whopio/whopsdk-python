# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import person_list_params, person_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.person_list_response import PersonListResponse
from ..types.person_retrieve_response import PersonRetrieveResponse

__all__ = ["PeopleResource", "AsyncPeopleResource"]


class PeopleResource(SyncAPIResource):
    """
    A Person is an identity-linked profile of a visitor or customer of an account, assembled from every [event](/api-reference/beta/events/event) the person generated — pixel page views, ad clicks, leads, identifies, and payments. Each profile carries the person's known identities (names, emails, phones, user IDs), purchase history and LTV, geo/device profile, traffic sources, and the first and last marketing touches that reached them.

    Use the People API to list and segment the people of an account — filter by activity, purchases, traffic source, location, or marketing touch, and sort by value — or retrieve one person by person ID, user ID, email address, or phone number.
    """

    @cached_property
    def with_raw_response(self) -> PeopleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return PeopleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PeopleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return PeopleResourceWithStreamingResponse(self)

    def retrieve(
        self,
        person_id: str,
        *,
        account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonRetrieveResponse:
        """Retrieves one person for an account.

        The identifier can be a person ID (prefixed
        `prsn_`), a user ID (prefixed `user_`), an email address, or a phone number —
        merged people resolve to the surviving profile.

        Args:
          account_id: Account ID, prefixed `biz_`. Optional for account API keys; required for
              credentials that can access multiple accounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not person_id:
            raise ValueError(f"Expected a non-empty value for `person_id` but received {person_id!r}")
        return self._get(
            path_template("/people/{person_id}", person_id=person_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_id": account_id}, person_retrieve_params.PersonRetrieveParams),
            ),
            cast_to=PersonRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        attribution_model: Literal["last_touch", "first_touch"] | Omit = omit,
        audience_id: str | Omit = omit,
        before: str | Omit = omit,
        contactable: bool | Omit = omit,
        country: str | Omit = omit,
        custom_event: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        email: str | Omit = omit,
        event_from: Union[str, datetime] | Omit = omit,
        event_name: SequenceNotStr[str] | Omit = omit,
        event_to: Union[str, datetime] | Omit = omit,
        first: int | Omit = omit,
        first_seen_after: Union[str, datetime] | Omit = omit,
        first_seen_before: Union[str, datetime] | Omit = omit,
        first_seen_within_days: int | Omit = omit,
        has_purchased: bool | Omit = omit,
        last_seen_after: Union[str, datetime] | Omit = omit,
        last_seen_before: Union[str, datetime] | Omit = omit,
        last_seen_within_days: int | Omit = omit,
        order: Literal[
            "first_seen_at",
            "last_seen_at",
            "first_purchase_at",
            "last_purchase_at",
            "purchase_count",
            "event_count",
            "ltv",
            "aov",
            "name",
            "email",
        ]
        | Omit = omit,
        phone: str | Omit = omit,
        query: str | Omit = omit,
        source: SequenceNotStr[str] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PersonListResponse]:
        """
        Lists the people (visitors and customers) of an account: the identity-linked
        person profiles aggregated from every pixel, payment, and platform event —
        identities, purchases and LTV, geo/device profile, traffic sources, and
        first/last marketing touches.

        Args:
          account_id: Account ID, prefixed `biz_`. Optional for account API keys; required for
              credentials that can access multiple accounts.

          after: A cursor for fetching people after a previous page.

          attribution_model: Attribution model the source filter matches against (defaults to last_touch).

          audience_id: Only include people in this audience. An audience that keeps itself up to date
              resolves to the People filters that define it, so this always reflects who
              matches now; uploaded lists and point-in-time snapshots match their recorded
              members.

          before: A cursor for fetching people before a later page.

          contactable: true for people who have an email address or phone number — the ones an ad
              platform can match.

          country: Only include people whose most recent visit came from this ISO 3166-1 alpha-2
              country code.

          custom_event: Only include people who fired this custom pixel event.

          direction: Sort direction. Defaults to desc.

          email: Only include the person linked to this email address.

          event_from:
              With event_to plus an event or source filter, switches to exact-population mode:
              person ids are resolved and paginated on the events side within this window (the
              same query the people metric counts), then hydrated per page.

          event_name: Only include people who fired any of these events, e.g. payment.completed or
              page.checkout.view.

          event_to: The inclusive end of the event window for exact-population mode.

          first: The number of people to return (default 100, max 100).

          first_seen_after: Only include people first seen at or after this ISO 8601 timestamp.

          first_seen_before: Only include people first seen before this ISO 8601 timestamp.

          first_seen_within_days: Only include people first seen within this many days, as a rolling window.

          has_purchased: true for customers only, false for people who have never purchased.

          last_seen_after: Only include people last seen at or after this ISO 8601 timestamp.

          last_seen_before: Only include people last seen before this ISO 8601 timestamp.

          last_seen_within_days: Only include people last seen within this many days, as a rolling window.

          order: Column to sort by. Defaults to last_seen_at.

          phone: Only include the person linked to this phone number.

          query: Search people by name, email, phone, or whop user ID (case-insensitive substring
              match).

          source: Only include people acquired from any of these sources — canonical paths
              (whop:<campaign>:<group>:<ad>, ext:<platform>:..., referrer:<domain>, direct,
              other), exact or with a trailing :\\** prefix. The same vocabulary the events /
              people metrics use.

          user_id: Only include the person linked to this whop user ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/people",
            page=SyncCursorPage[PersonListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "attribution_model": attribution_model,
                        "audience_id": audience_id,
                        "before": before,
                        "contactable": contactable,
                        "country": country,
                        "custom_event": custom_event,
                        "direction": direction,
                        "email": email,
                        "event_from": event_from,
                        "event_name": event_name,
                        "event_to": event_to,
                        "first": first,
                        "first_seen_after": first_seen_after,
                        "first_seen_before": first_seen_before,
                        "first_seen_within_days": first_seen_within_days,
                        "has_purchased": has_purchased,
                        "last_seen_after": last_seen_after,
                        "last_seen_before": last_seen_before,
                        "last_seen_within_days": last_seen_within_days,
                        "order": order,
                        "phone": phone,
                        "query": query,
                        "source": source,
                        "user_id": user_id,
                    },
                    person_list_params.PersonListParams,
                ),
            ),
            model=PersonListResponse,
        )


class AsyncPeopleResource(AsyncAPIResource):
    """
    A Person is an identity-linked profile of a visitor or customer of an account, assembled from every [event](/api-reference/beta/events/event) the person generated — pixel page views, ad clicks, leads, identifies, and payments. Each profile carries the person's known identities (names, emails, phones, user IDs), purchase history and LTV, geo/device profile, traffic sources, and the first and last marketing touches that reached them.

    Use the People API to list and segment the people of an account — filter by activity, purchases, traffic source, location, or marketing touch, and sort by value — or retrieve one person by person ID, user ID, email address, or phone number.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPeopleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPeopleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPeopleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncPeopleResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        person_id: str,
        *,
        account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonRetrieveResponse:
        """Retrieves one person for an account.

        The identifier can be a person ID (prefixed
        `prsn_`), a user ID (prefixed `user_`), an email address, or a phone number —
        merged people resolve to the surviving profile.

        Args:
          account_id: Account ID, prefixed `biz_`. Optional for account API keys; required for
              credentials that can access multiple accounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not person_id:
            raise ValueError(f"Expected a non-empty value for `person_id` but received {person_id!r}")
        return await self._get(
            path_template("/people/{person_id}", person_id=person_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, person_retrieve_params.PersonRetrieveParams
                ),
            ),
            cast_to=PersonRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        attribution_model: Literal["last_touch", "first_touch"] | Omit = omit,
        audience_id: str | Omit = omit,
        before: str | Omit = omit,
        contactable: bool | Omit = omit,
        country: str | Omit = omit,
        custom_event: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        email: str | Omit = omit,
        event_from: Union[str, datetime] | Omit = omit,
        event_name: SequenceNotStr[str] | Omit = omit,
        event_to: Union[str, datetime] | Omit = omit,
        first: int | Omit = omit,
        first_seen_after: Union[str, datetime] | Omit = omit,
        first_seen_before: Union[str, datetime] | Omit = omit,
        first_seen_within_days: int | Omit = omit,
        has_purchased: bool | Omit = omit,
        last_seen_after: Union[str, datetime] | Omit = omit,
        last_seen_before: Union[str, datetime] | Omit = omit,
        last_seen_within_days: int | Omit = omit,
        order: Literal[
            "first_seen_at",
            "last_seen_at",
            "first_purchase_at",
            "last_purchase_at",
            "purchase_count",
            "event_count",
            "ltv",
            "aov",
            "name",
            "email",
        ]
        | Omit = omit,
        phone: str | Omit = omit,
        query: str | Omit = omit,
        source: SequenceNotStr[str] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PersonListResponse, AsyncCursorPage[PersonListResponse]]:
        """
        Lists the people (visitors and customers) of an account: the identity-linked
        person profiles aggregated from every pixel, payment, and platform event —
        identities, purchases and LTV, geo/device profile, traffic sources, and
        first/last marketing touches.

        Args:
          account_id: Account ID, prefixed `biz_`. Optional for account API keys; required for
              credentials that can access multiple accounts.

          after: A cursor for fetching people after a previous page.

          attribution_model: Attribution model the source filter matches against (defaults to last_touch).

          audience_id: Only include people in this audience. An audience that keeps itself up to date
              resolves to the People filters that define it, so this always reflects who
              matches now; uploaded lists and point-in-time snapshots match their recorded
              members.

          before: A cursor for fetching people before a later page.

          contactable: true for people who have an email address or phone number — the ones an ad
              platform can match.

          country: Only include people whose most recent visit came from this ISO 3166-1 alpha-2
              country code.

          custom_event: Only include people who fired this custom pixel event.

          direction: Sort direction. Defaults to desc.

          email: Only include the person linked to this email address.

          event_from:
              With event_to plus an event or source filter, switches to exact-population mode:
              person ids are resolved and paginated on the events side within this window (the
              same query the people metric counts), then hydrated per page.

          event_name: Only include people who fired any of these events, e.g. payment.completed or
              page.checkout.view.

          event_to: The inclusive end of the event window for exact-population mode.

          first: The number of people to return (default 100, max 100).

          first_seen_after: Only include people first seen at or after this ISO 8601 timestamp.

          first_seen_before: Only include people first seen before this ISO 8601 timestamp.

          first_seen_within_days: Only include people first seen within this many days, as a rolling window.

          has_purchased: true for customers only, false for people who have never purchased.

          last_seen_after: Only include people last seen at or after this ISO 8601 timestamp.

          last_seen_before: Only include people last seen before this ISO 8601 timestamp.

          last_seen_within_days: Only include people last seen within this many days, as a rolling window.

          order: Column to sort by. Defaults to last_seen_at.

          phone: Only include the person linked to this phone number.

          query: Search people by name, email, phone, or whop user ID (case-insensitive substring
              match).

          source: Only include people acquired from any of these sources — canonical paths
              (whop:<campaign>:<group>:<ad>, ext:<platform>:..., referrer:<domain>, direct,
              other), exact or with a trailing :\\** prefix. The same vocabulary the events /
              people metrics use.

          user_id: Only include the person linked to this whop user ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/people",
            page=AsyncCursorPage[PersonListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "attribution_model": attribution_model,
                        "audience_id": audience_id,
                        "before": before,
                        "contactable": contactable,
                        "country": country,
                        "custom_event": custom_event,
                        "direction": direction,
                        "email": email,
                        "event_from": event_from,
                        "event_name": event_name,
                        "event_to": event_to,
                        "first": first,
                        "first_seen_after": first_seen_after,
                        "first_seen_before": first_seen_before,
                        "first_seen_within_days": first_seen_within_days,
                        "has_purchased": has_purchased,
                        "last_seen_after": last_seen_after,
                        "last_seen_before": last_seen_before,
                        "last_seen_within_days": last_seen_within_days,
                        "order": order,
                        "phone": phone,
                        "query": query,
                        "source": source,
                        "user_id": user_id,
                    },
                    person_list_params.PersonListParams,
                ),
            ),
            model=PersonListResponse,
        )


class PeopleResourceWithRawResponse:
    def __init__(self, people: PeopleResource) -> None:
        self._people = people

        self.retrieve = to_raw_response_wrapper(
            people.retrieve,
        )
        self.list = to_raw_response_wrapper(
            people.list,
        )


class AsyncPeopleResourceWithRawResponse:
    def __init__(self, people: AsyncPeopleResource) -> None:
        self._people = people

        self.retrieve = async_to_raw_response_wrapper(
            people.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            people.list,
        )


class PeopleResourceWithStreamingResponse:
    def __init__(self, people: PeopleResource) -> None:
        self._people = people

        self.retrieve = to_streamed_response_wrapper(
            people.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            people.list,
        )


class AsyncPeopleResourceWithStreamingResponse:
    def __init__(self, people: AsyncPeopleResource) -> None:
        self._people = people

        self.retrieve = async_to_streamed_response_wrapper(
            people.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            people.list,
        )
