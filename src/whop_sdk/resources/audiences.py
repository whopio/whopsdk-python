# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

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
from ..types.audience_delete_response import AudienceDeleteResponse

__all__ = ["AudiencesResource", "AsyncAudiencesResource"]


class AudiencesResource(SyncAPIResource):
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
        column_mapping: Dict[str, str],
        file_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Audience:
        """
        Creates a custom audience from an uploaded CSV file and starts processing it.

        Args:
          account_id: The ID of the account that will own the audience.

          column_mapping: Map of identity field (email, phone, first_name, last_name, country) to the CSV
              column header that holds it. Map at least an email or phone column.

          file_id: A direct upload ID returned by the standard media upload endpoint.

          name: A display name for the audience.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/audiences",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "column_mapping": column_mapping,
                    "file_id": file_id,
                    "name": name,
                },
                audience_create_params.AudienceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Audience,
        )

    def list(
        self,
        *,
        account_id: str,
        after: str | Omit = omit,
        audience_id: str | Omit = omit,
        first: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Audience]:
        """
        Lists the custom audiences (uploaded CSV customer lists) for an account.

        Args:
          account_id: The ID of the account that owns the audiences, which will look like
              biz\\__******\\********.

          after: A cursor; returns audiences after this position.

          audience_id: Optional audience ID to filter the response to one audience, which will look
              like adaud\\__******\\********.

          first: The number of audiences to return (default 20, max 100).

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
        Deletes (soft-discards) a custom audience.

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
        column_mapping: Dict[str, str],
        file_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Audience:
        """
        Creates a custom audience from an uploaded CSV file and starts processing it.

        Args:
          account_id: The ID of the account that will own the audience.

          column_mapping: Map of identity field (email, phone, first_name, last_name, country) to the CSV
              column header that holds it. Map at least an email or phone column.

          file_id: A direct upload ID returned by the standard media upload endpoint.

          name: A display name for the audience.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/audiences",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "column_mapping": column_mapping,
                    "file_id": file_id,
                    "name": name,
                },
                audience_create_params.AudienceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Audience,
        )

    def list(
        self,
        *,
        account_id: str,
        after: str | Omit = omit,
        audience_id: str | Omit = omit,
        first: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Audience, AsyncCursorPage[Audience]]:
        """
        Lists the custom audiences (uploaded CSV customer lists) for an account.

        Args:
          account_id: The ID of the account that owns the audiences, which will look like
              biz\\__******\\********.

          after: A cursor; returns audiences after this position.

          audience_id: Optional audience ID to filter the response to one audience, which will look
              like adaud\\__******\\********.

          first: The number of audiences to return (default 20, max 100).

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
        Deletes (soft-discards) a custom audience.

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
