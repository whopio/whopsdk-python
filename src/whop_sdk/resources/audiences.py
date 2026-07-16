# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ..types import audience_list_params, audience_create_params
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
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.audience import Audience
from ..types.audience_create_response import AudienceCreateResponse
from ..types.audience_delete_response import AudienceDeleteResponse

__all__ = ["AudiencesResource", "AsyncAudiencesResource"]


class AudiencesResource(SyncAPIResource):
    """An Audience represents a customer list uploaded to Whop for ad targeting.

    Audiences belong to an account and sync to supported ad platforms as custom audiences.

    Use the Audiences API to create audiences from CSV uploads, monitor processing status, and list or delete audiences for an account. Created audiences are usable for targeting after processing reaches `ready` or `partial`.
    """

    @cached_property
    def with_raw_response(self) -> AudiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AudiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AudiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AudiencesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        audience_type: Literal["custom", "lookalike"] | Omit = omit,
        column_mapping: audience_create_params.ColumnMapping | Omit = omit,
        count: int | Omit = omit,
        file_id: str | Omit = omit,
        name: str | Omit = omit,
        percentage: int | Omit = omit,
        source_audience_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceCreateResponse:
        """Creates an audience.

        Default (`audience_type` omitted or `custom`): creates one
        audience from an uploaded customer identity CSV file (`name`, `column_mapping`,
        and `file_id` required) and starts processing it; responds with the audience
        object. With `audience_type: lookalike`: creates a ladder of Meta lookalike
        audiences from an existing ready custom audience (`source_audience_id`, `count`,
        and `percentage` required) — `count` equal similarity bands slicing the top
        `percentage`% (3 audiences at 6% = 0–2%, 2–4%, 4–6%), each returned as its own
        audience in a `{ data: [...] }` envelope.

        Args:
          account_id: Account ID, prefixed `biz_`.

          audience_type: What to create. Defaults to `custom` (CSV upload).

          column_mapping: Custom audiences only. Maps supported identity fields to CSV column headers. Map
              at least one of `email` or `phone`.

          count: Lookalikes only. Number of lookalike audiences to create (1–6).

          file_id: Custom audiences only. Direct upload ID from the standard media upload endpoint.

          name: Audience display name. Required for custom audiences; lookalike names are
              generated from the source audience.

          percentage: Lookalikes only. Total similarity reach as a whole percent (1–20), sliced evenly
              across `count` — must be divisible by `count`.

          source_audience_id: Lookalikes only. The ready custom audience (`adaud_`) to build from; it needs at
              least 100 matched people.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AudienceCreateResponse,
            self._post(
                "/audiences",
                body=maybe_transform(
                    {
                        "account_id": account_id,
                        "audience_type": audience_type,
                        "column_mapping": column_mapping,
                        "count": count,
                        "file_id": file_id,
                        "name": name,
                        "percentage": percentage,
                        "source_audience_id": source_audience_id,
                    },
                    audience_create_params.AudienceCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AudienceCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        after: str | Omit = omit,
        audience_id: str | Omit = omit,
        audience_type: Literal["custom", "lookalike"] | Omit = omit,
        first: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Audience]:
        """Lists uploaded customer-list audiences for an account.

        Pass `audience_id` to
        return a specific audience.

        Args:
          account_id: Account ID, prefixed `biz_`.

          after: Cursor for the next page of audiences.

          audience_id: Audience ID, prefixed `adaud_`, used to filter the response to one audience.

          audience_type: Filter by audience type: `custom` (uploaded lists) or `lookalike`.

          first: Number of audiences to return. Defaults to 20; maximum 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/audiences",
            page=SyncCursorPage[Audience],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "audience_id": audience_id,
                        "audience_type": audience_type,
                        "first": first,
                    },
                    audience_list_params.AudienceListParams,
                ),
            ),
            model=Audience,
        )

    def delete(
        self,
        audience_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceDeleteResponse:
        """
        Deletes an audience so it is no longer available for targeting.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        return self._delete(
            path_template("/audiences/{audience_id}", audience_id=audience_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AudienceDeleteResponse,
        )


class AsyncAudiencesResource(AsyncAPIResource):
    """An Audience represents a customer list uploaded to Whop for ad targeting.

    Audiences belong to an account and sync to supported ad platforms as custom audiences.

    Use the Audiences API to create audiences from CSV uploads, monitor processing status, and list or delete audiences for an account. Created audiences are usable for targeting after processing reaches `ready` or `partial`.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAudiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAudiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAudiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncAudiencesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        audience_type: Literal["custom", "lookalike"] | Omit = omit,
        column_mapping: audience_create_params.ColumnMapping | Omit = omit,
        count: int | Omit = omit,
        file_id: str | Omit = omit,
        name: str | Omit = omit,
        percentage: int | Omit = omit,
        source_audience_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceCreateResponse:
        """Creates an audience.

        Default (`audience_type` omitted or `custom`): creates one
        audience from an uploaded customer identity CSV file (`name`, `column_mapping`,
        and `file_id` required) and starts processing it; responds with the audience
        object. With `audience_type: lookalike`: creates a ladder of Meta lookalike
        audiences from an existing ready custom audience (`source_audience_id`, `count`,
        and `percentage` required) — `count` equal similarity bands slicing the top
        `percentage`% (3 audiences at 6% = 0–2%, 2–4%, 4–6%), each returned as its own
        audience in a `{ data: [...] }` envelope.

        Args:
          account_id: Account ID, prefixed `biz_`.

          audience_type: What to create. Defaults to `custom` (CSV upload).

          column_mapping: Custom audiences only. Maps supported identity fields to CSV column headers. Map
              at least one of `email` or `phone`.

          count: Lookalikes only. Number of lookalike audiences to create (1–6).

          file_id: Custom audiences only. Direct upload ID from the standard media upload endpoint.

          name: Audience display name. Required for custom audiences; lookalike names are
              generated from the source audience.

          percentage: Lookalikes only. Total similarity reach as a whole percent (1–20), sliced evenly
              across `count` — must be divisible by `count`.

          source_audience_id: Lookalikes only. The ready custom audience (`adaud_`) to build from; it needs at
              least 100 matched people.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AudienceCreateResponse,
            await self._post(
                "/audiences",
                body=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "audience_type": audience_type,
                        "column_mapping": column_mapping,
                        "count": count,
                        "file_id": file_id,
                        "name": name,
                        "percentage": percentage,
                        "source_audience_id": source_audience_id,
                    },
                    audience_create_params.AudienceCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AudienceCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        after: str | Omit = omit,
        audience_id: str | Omit = omit,
        audience_type: Literal["custom", "lookalike"] | Omit = omit,
        first: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Audience, AsyncCursorPage[Audience]]:
        """Lists uploaded customer-list audiences for an account.

        Pass `audience_id` to
        return a specific audience.

        Args:
          account_id: Account ID, prefixed `biz_`.

          after: Cursor for the next page of audiences.

          audience_id: Audience ID, prefixed `adaud_`, used to filter the response to one audience.

          audience_type: Filter by audience type: `custom` (uploaded lists) or `lookalike`.

          first: Number of audiences to return. Defaults to 20; maximum 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/audiences",
            page=AsyncCursorPage[Audience],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "audience_id": audience_id,
                        "audience_type": audience_type,
                        "first": first,
                    },
                    audience_list_params.AudienceListParams,
                ),
            ),
            model=Audience,
        )

    async def delete(
        self,
        audience_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceDeleteResponse:
        """
        Deletes an audience so it is no longer available for targeting.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        return await self._delete(
            path_template("/audiences/{audience_id}", audience_id=audience_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AudienceDeleteResponse,
        )


class AudiencesResourceWithRawResponse:
    def __init__(self, audiences: AudiencesResource) -> None:
        self._audiences = audiences

        self.create = to_raw_response_wrapper(
            audiences.create,
        )
        self.list = to_raw_response_wrapper(
            audiences.list,
        )
        self.delete = to_raw_response_wrapper(
            audiences.delete,
        )


class AsyncAudiencesResourceWithRawResponse:
    def __init__(self, audiences: AsyncAudiencesResource) -> None:
        self._audiences = audiences

        self.create = async_to_raw_response_wrapper(
            audiences.create,
        )
        self.list = async_to_raw_response_wrapper(
            audiences.list,
        )
        self.delete = async_to_raw_response_wrapper(
            audiences.delete,
        )


class AudiencesResourceWithStreamingResponse:
    def __init__(self, audiences: AudiencesResource) -> None:
        self._audiences = audiences

        self.create = to_streamed_response_wrapper(
            audiences.create,
        )
        self.list = to_streamed_response_wrapper(
            audiences.list,
        )
        self.delete = to_streamed_response_wrapper(
            audiences.delete,
        )


class AsyncAudiencesResourceWithStreamingResponse:
    def __init__(self, audiences: AsyncAudiencesResource) -> None:
        self._audiences = audiences

        self.create = async_to_streamed_response_wrapper(
            audiences.create,
        )
        self.list = async_to_streamed_response_wrapper(
            audiences.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            audiences.delete,
        )
