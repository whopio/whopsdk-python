# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import team_member_list_params, team_member_create_params, team_member_update_params
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
from ..types.team_member import TeamMember
from ..types.team_member_delete_response import TeamMemberDeleteResponse

__all__ = ["TeamMembersResource", "AsyncTeamMembersResource"]


class TeamMembersResource(SyncAPIResource):
    """
    A Team Member is a member of an account's team: the link between a user and an account, carrying the role that controls what they can do. Roles are either system roles (like `admin` or `moderator`) or `custom` roles managed from the dashboard.

    Use the Team Members API to list an account's team, add a user to the team with a system role, change a member's role, and remove members. Adding a user who has not yet accepted sends an invitation instead.
    """

    @cached_property
    def with_raw_response(self) -> TeamMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return TeamMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TeamMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return TeamMembersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        role: Literal["owner", "admin", "sales_manager", "moderator", "advertiser"],
        email: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> TeamMember:
        """Adds a member to an account's team with a system role.

        Identify them by exactly
        one of `user_id` or `email`. If the person has not yet accepted — or the email
        does not belong to a Whop account yet — an invitation is sent instead and the
        response is `202` with
        `{ "object": "team_member_invite", "invitation_sent": true }`. If they already
        have a pending invite, the request fails with a `400`. Custom roles cannot be
        granted via the API.

        Args:
          account_id: Account ID, prefixed `biz_`.

          role: The system role to grant.

          email: Email address to invite. Mutually exclusive with `user_id`. If the email already
              belongs to a Whop account it is treated the same as passing that account's
              `user_id`; otherwise a pending invite is created for the email.

          user_id: The user to add to the team, prefixed `user_`. Mutually exclusive with `email`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/team_members",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "role": role,
                    "email": email,
                    "user_id": user_id,
                },
                team_member_create_params.TeamMemberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TeamMember,
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
    ) -> TeamMember:
        """Retrieves a team member by ID.

        `email` requires the
        `company:authorized_user:email:read` scope and is `null` otherwise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/team_members/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TeamMember,
        )

    def update(
        self,
        id: str,
        *,
        role: Literal["owner", "admin", "sales_manager", "moderator", "advertiser"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> TeamMember:
        """Changes a team member's system role.

        Requires a user session — account API keys
        cannot change member roles. The account owner's role cannot be changed, and you
        cannot change your own role.

        Args:
          role: The system role to grant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/team_members/{id}", id=id),
            body=maybe_transform({"role": role}, team_member_update_params.TeamMemberUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TeamMember,
        )

    def list(
        self,
        *,
        account_id: str,
        after: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        role: Literal[
            "owner",
            "admin",
            "sales_manager",
            "moderator",
            "advertiser",
            "app_manager",
            "support",
            "manager",
            "workforce",
            "custom",
        ]
        | Omit = omit,
        status: Literal["joined", "pending"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[TeamMember]:
        """
        Lists an account's team members, including pending invites (`status: "pending"`,
        `ausri_` ids; `user` is `null` for invites sent to an email with no Whop account
        yet). For accepted members, `email` requires the
        `company:authorized_user:email:read` scope and is `null` otherwise.

        Args:
          account_id: Account ID, prefixed `biz_`.

          after: Cursor for the next page of members.

          created_after: Only return members added after this ISO 8601 timestamp.

          created_before: Only return members added before this ISO 8601 timestamp.

          direction: Sort direction. Defaults to `desc`.

          first: Number of members to return. Defaults to 20; maximum 100.

          order: Field used to sort members.

          role: Only return members with this role. `custom` matches members on a
              dashboard-managed custom role.

          status: Only return members with this status: `joined` (accepted members) or `pending`
              (pending invites). Both are returned by default.

          user_id: Only return the membership for this user ID, prefixed `user_`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/team_members",
            page=SyncCursorPage[TeamMember],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "order": order,
                        "role": role,
                        "status": status,
                        "user_id": user_id,
                    },
                    team_member_list_params.TeamMemberListParams,
                ),
            ),
            model=TeamMember,
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
    ) -> TeamMemberDeleteResponse:
        """
        Removes a team member from the account, or revokes a pending invite when given
        an `ausri_` ID. A user session may delete its own membership to leave the team
        without the delete scope. The account owner cannot be removed.

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
            path_template("/team_members/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TeamMemberDeleteResponse,
        )


class AsyncTeamMembersResource(AsyncAPIResource):
    """
    A Team Member is a member of an account's team: the link between a user and an account, carrying the role that controls what they can do. Roles are either system roles (like `admin` or `moderator`) or `custom` roles managed from the dashboard.

    Use the Team Members API to list an account's team, add a user to the team with a system role, change a member's role, and remove members. Adding a user who has not yet accepted sends an invitation instead.
    """

    @cached_property
    def with_raw_response(self) -> AsyncTeamMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTeamMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTeamMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncTeamMembersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        role: Literal["owner", "admin", "sales_manager", "moderator", "advertiser"],
        email: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> TeamMember:
        """Adds a member to an account's team with a system role.

        Identify them by exactly
        one of `user_id` or `email`. If the person has not yet accepted — or the email
        does not belong to a Whop account yet — an invitation is sent instead and the
        response is `202` with
        `{ "object": "team_member_invite", "invitation_sent": true }`. If they already
        have a pending invite, the request fails with a `400`. Custom roles cannot be
        granted via the API.

        Args:
          account_id: Account ID, prefixed `biz_`.

          role: The system role to grant.

          email: Email address to invite. Mutually exclusive with `user_id`. If the email already
              belongs to a Whop account it is treated the same as passing that account's
              `user_id`; otherwise a pending invite is created for the email.

          user_id: The user to add to the team, prefixed `user_`. Mutually exclusive with `email`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/team_members",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "role": role,
                    "email": email,
                    "user_id": user_id,
                },
                team_member_create_params.TeamMemberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TeamMember,
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
    ) -> TeamMember:
        """Retrieves a team member by ID.

        `email` requires the
        `company:authorized_user:email:read` scope and is `null` otherwise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/team_members/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TeamMember,
        )

    async def update(
        self,
        id: str,
        *,
        role: Literal["owner", "admin", "sales_manager", "moderator", "advertiser"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> TeamMember:
        """Changes a team member's system role.

        Requires a user session — account API keys
        cannot change member roles. The account owner's role cannot be changed, and you
        cannot change your own role.

        Args:
          role: The system role to grant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/team_members/{id}", id=id),
            body=await async_maybe_transform({"role": role}, team_member_update_params.TeamMemberUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TeamMember,
        )

    def list(
        self,
        *,
        account_id: str,
        after: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        role: Literal[
            "owner",
            "admin",
            "sales_manager",
            "moderator",
            "advertiser",
            "app_manager",
            "support",
            "manager",
            "workforce",
            "custom",
        ]
        | Omit = omit,
        status: Literal["joined", "pending"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TeamMember, AsyncCursorPage[TeamMember]]:
        """
        Lists an account's team members, including pending invites (`status: "pending"`,
        `ausri_` ids; `user` is `null` for invites sent to an email with no Whop account
        yet). For accepted members, `email` requires the
        `company:authorized_user:email:read` scope and is `null` otherwise.

        Args:
          account_id: Account ID, prefixed `biz_`.

          after: Cursor for the next page of members.

          created_after: Only return members added after this ISO 8601 timestamp.

          created_before: Only return members added before this ISO 8601 timestamp.

          direction: Sort direction. Defaults to `desc`.

          first: Number of members to return. Defaults to 20; maximum 100.

          order: Field used to sort members.

          role: Only return members with this role. `custom` matches members on a
              dashboard-managed custom role.

          status: Only return members with this status: `joined` (accepted members) or `pending`
              (pending invites). Both are returned by default.

          user_id: Only return the membership for this user ID, prefixed `user_`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/team_members",
            page=AsyncCursorPage[TeamMember],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "order": order,
                        "role": role,
                        "status": status,
                        "user_id": user_id,
                    },
                    team_member_list_params.TeamMemberListParams,
                ),
            ),
            model=TeamMember,
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
    ) -> TeamMemberDeleteResponse:
        """
        Removes a team member from the account, or revokes a pending invite when given
        an `ausri_` ID. A user session may delete its own membership to leave the team
        without the delete scope. The account owner cannot be removed.

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
            path_template("/team_members/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TeamMemberDeleteResponse,
        )


class TeamMembersResourceWithRawResponse:
    def __init__(self, team_members: TeamMembersResource) -> None:
        self._team_members = team_members

        self.create = to_raw_response_wrapper(
            team_members.create,
        )
        self.retrieve = to_raw_response_wrapper(
            team_members.retrieve,
        )
        self.update = to_raw_response_wrapper(
            team_members.update,
        )
        self.list = to_raw_response_wrapper(
            team_members.list,
        )
        self.delete = to_raw_response_wrapper(
            team_members.delete,
        )


class AsyncTeamMembersResourceWithRawResponse:
    def __init__(self, team_members: AsyncTeamMembersResource) -> None:
        self._team_members = team_members

        self.create = async_to_raw_response_wrapper(
            team_members.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            team_members.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            team_members.update,
        )
        self.list = async_to_raw_response_wrapper(
            team_members.list,
        )
        self.delete = async_to_raw_response_wrapper(
            team_members.delete,
        )


class TeamMembersResourceWithStreamingResponse:
    def __init__(self, team_members: TeamMembersResource) -> None:
        self._team_members = team_members

        self.create = to_streamed_response_wrapper(
            team_members.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            team_members.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            team_members.update,
        )
        self.list = to_streamed_response_wrapper(
            team_members.list,
        )
        self.delete = to_streamed_response_wrapper(
            team_members.delete,
        )


class AsyncTeamMembersResourceWithStreamingResponse:
    def __init__(self, team_members: AsyncTeamMembersResource) -> None:
        self._team_members = team_members

        self.create = async_to_streamed_response_wrapper(
            team_members.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            team_members.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            team_members.update,
        )
        self.list = async_to_streamed_response_wrapper(
            team_members.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            team_members.delete,
        )
