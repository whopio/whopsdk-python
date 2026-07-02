# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import person_list_params, person_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.person_list_response import PersonListResponse
from ..types.person_retrieve_response import PersonRetrieveResponse

__all__ = ["PeopleResource", "AsyncPeopleResource"]


class PeopleResource(SyncAPIResource):
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
        from_: int | Omit = omit,
        to: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonRetrieveResponse:
        """
        Retrieves one person for an account, aggregated from pixel events.

        Args:
          account_id: The ID of the account, which will look like biz\\__******\\********. Optional for
              account API keys; required for credentials that can access multiple accounts.

          from_: Start of the time range as a Unix timestamp.

          to: End of the time range as a Unix timestamp. Defaults to now.

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
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "from_": from_,
                        "to": to,
                    },
                    person_retrieve_params.PersonRetrieveParams,
                ),
            ),
            cast_to=PersonRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        filters: str | Omit = omit,
        first: int | Omit = omit,
        from_: int | Omit = omit,
        offset: int | Omit = omit,
        sort: str | Omit = omit,
        to: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonListResponse:
        """
        Lists the people (visitors and customers) of an account, aggregated from pixel
        events. The account is inferred from an account API key; other credentials must
        pass account_id.

        Args:
          account_id: The ID of the account, which will look like biz\\__******\\********. Optional for
              account API keys; required for credentials that can access multiple accounts.

          direction: Sort direction. Defaults to desc.

          filters: A JSON-encoded array of filters, each with field, operator, and value keys.

          first: The number of people to return (default 100, max 101).

          from_: Start of the time range as a Unix timestamp. Defaults to 366 days before `to`.

          offset: The number of people to skip, for offset pagination.

          sort: Column to sort by (e.g. last_seen_at, ltv, purchase_count). Defaults to
              last_seen_at.

          to: End of the time range as a Unix timestamp. Defaults to now.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/people",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "direction": direction,
                        "filters": filters,
                        "first": first,
                        "from_": from_,
                        "offset": offset,
                        "sort": sort,
                        "to": to,
                    },
                    person_list_params.PersonListParams,
                ),
            ),
            cast_to=PersonListResponse,
        )


class AsyncPeopleResource(AsyncAPIResource):
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
        from_: int | Omit = omit,
        to: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonRetrieveResponse:
        """
        Retrieves one person for an account, aggregated from pixel events.

        Args:
          account_id: The ID of the account, which will look like biz\\__******\\********. Optional for
              account API keys; required for credentials that can access multiple accounts.

          from_: Start of the time range as a Unix timestamp.

          to: End of the time range as a Unix timestamp. Defaults to now.

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
                    {
                        "account_id": account_id,
                        "from_": from_,
                        "to": to,
                    },
                    person_retrieve_params.PersonRetrieveParams,
                ),
            ),
            cast_to=PersonRetrieveResponse,
        )

    async def list(
        self,
        *,
        account_id: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        filters: str | Omit = omit,
        first: int | Omit = omit,
        from_: int | Omit = omit,
        offset: int | Omit = omit,
        sort: str | Omit = omit,
        to: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonListResponse:
        """
        Lists the people (visitors and customers) of an account, aggregated from pixel
        events. The account is inferred from an account API key; other credentials must
        pass account_id.

        Args:
          account_id: The ID of the account, which will look like biz\\__******\\********. Optional for
              account API keys; required for credentials that can access multiple accounts.

          direction: Sort direction. Defaults to desc.

          filters: A JSON-encoded array of filters, each with field, operator, and value keys.

          first: The number of people to return (default 100, max 101).

          from_: Start of the time range as a Unix timestamp. Defaults to 366 days before `to`.

          offset: The number of people to skip, for offset pagination.

          sort: Column to sort by (e.g. last_seen_at, ltv, purchase_count). Defaults to
              last_seen_at.

          to: End of the time range as a Unix timestamp. Defaults to now.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/people",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "direction": direction,
                        "filters": filters,
                        "first": first,
                        "from_": from_,
                        "offset": offset,
                        "sort": sort,
                        "to": to,
                    },
                    person_list_params.PersonListParams,
                ),
            ),
            cast_to=PersonListResponse,
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
