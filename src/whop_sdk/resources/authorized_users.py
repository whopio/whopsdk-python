# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import authorized_user_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
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
from ..types.shared.authorized_user_roles import AuthorizedUserRoles
from ..types.authorized_user_list_response import AuthorizedUserListResponse
from ..types.authorized_user_retrieve_response import AuthorizedUserRetrieveResponse

__all__ = ["AuthorizedUsersResource", "AsyncAuthorizedUsersResource"]


class AuthorizedUsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthorizedUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AuthorizedUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthorizedUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AuthorizedUsersResourceWithStreamingResponse(self)

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
    ) -> AuthorizedUserRetrieveResponse:
        """
        Retrieves a authorized user by ID

        Required permissions:

        - `company:authorized_user:read`
        - `member:email:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/authorized_users/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedUserRetrieveResponse,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        role: Optional[AuthorizedUserRoles] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AuthorizedUserListResponse]:
        """
        Lists authorized users

        Required permissions:

        - `company:authorized_user:read`
        - `member:email:read`

        Args:
          company_id: The ID of the company to list authorized users for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          role: Possible roles an authorized user can have

          user_id: Filter by the user ID to check if the user is an authorized user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/authorized_users",
            page=SyncCursorPage[AuthorizedUserListResponse],
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
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "last": last,
                        "role": role,
                        "user_id": user_id,
                    },
                    authorized_user_list_params.AuthorizedUserListParams,
                ),
            ),
            model=AuthorizedUserListResponse,
        )


class AsyncAuthorizedUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthorizedUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthorizedUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthorizedUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncAuthorizedUsersResourceWithStreamingResponse(self)

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
    ) -> AuthorizedUserRetrieveResponse:
        """
        Retrieves a authorized user by ID

        Required permissions:

        - `company:authorized_user:read`
        - `member:email:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/authorized_users/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedUserRetrieveResponse,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        role: Optional[AuthorizedUserRoles] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AuthorizedUserListResponse, AsyncCursorPage[AuthorizedUserListResponse]]:
        """
        Lists authorized users

        Required permissions:

        - `company:authorized_user:read`
        - `member:email:read`

        Args:
          company_id: The ID of the company to list authorized users for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          role: Possible roles an authorized user can have

          user_id: Filter by the user ID to check if the user is an authorized user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/authorized_users",
            page=AsyncCursorPage[AuthorizedUserListResponse],
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
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "last": last,
                        "role": role,
                        "user_id": user_id,
                    },
                    authorized_user_list_params.AuthorizedUserListParams,
                ),
            ),
            model=AuthorizedUserListResponse,
        )


class AuthorizedUsersResourceWithRawResponse:
    def __init__(self, authorized_users: AuthorizedUsersResource) -> None:
        self._authorized_users = authorized_users

        self.retrieve = to_raw_response_wrapper(
            authorized_users.retrieve,
        )
        self.list = to_raw_response_wrapper(
            authorized_users.list,
        )


class AsyncAuthorizedUsersResourceWithRawResponse:
    def __init__(self, authorized_users: AsyncAuthorizedUsersResource) -> None:
        self._authorized_users = authorized_users

        self.retrieve = async_to_raw_response_wrapper(
            authorized_users.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            authorized_users.list,
        )


class AuthorizedUsersResourceWithStreamingResponse:
    def __init__(self, authorized_users: AuthorizedUsersResource) -> None:
        self._authorized_users = authorized_users

        self.retrieve = to_streamed_response_wrapper(
            authorized_users.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            authorized_users.list,
        )


class AsyncAuthorizedUsersResourceWithStreamingResponse:
    def __init__(self, authorized_users: AsyncAuthorizedUsersResource) -> None:
        self._authorized_users = authorized_users

        self.retrieve = async_to_streamed_response_wrapper(
            authorized_users.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            authorized_users.list,
        )
