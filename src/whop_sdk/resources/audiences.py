# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ..types import audience_list_params, audience_create_params, audience_update_params, audience_add_people_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
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
        auto_refresh: bool | Omit = omit,
        column_mapping: audience_create_params.ColumnMapping | Omit = omit,
        count: int | Omit = omit,
        file_id: str | Omit = omit,
        filters: object | Omit = omit,
        name: str | Omit = omit,
        percentage: int | Omit = omit,
        source_audience_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
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
        object. With `filters`: creates an audience from saved People filters (`name`
        required) — membership is built from the account's People data, and
        `auto_refresh` decides whether it keeps tracking the filters or keeps whoever
        matched at creation. With `audience_type: lookalike`: creates a ladder of Meta
        lookalike audiences from an existing ready custom audience
        (`source_audience_id`, `count`, and `percentage` required) — `count` equal
        similarity bands slicing the top `percentage`% (3 audiences at 6% = 0–2%, 2–4%,
        4–6%), each returned as its own audience in a `{ data: [...] }` envelope.

        Args:
          account_id: Account ID, prefixed `biz_`.

          audience_type: What to create. Defaults to `custom` (CSV upload).

          auto_refresh: Filter audiences only, and set only at creation. `true` (the default) rebuilds
              membership from the filters twice a day. `false` keeps whoever matched at
              creation and never rebuilds.

          column_mapping: Custom audiences only. Maps supported identity fields to CSV column headers. Map
              at least one of `email` or `phone`.

          count: Lookalikes only. Number of lookalike audiences to create (1–6).

          file_id: Custom audiences only. The uploaded customer CSV — a file id (`file_...`)
              returned by `POST /files`.

          filters: Filter audiences only. The People filters that define membership, keyed exactly
              as `GET /people` accepts them — for example `{"os": "iOS", "country": "US"}`.
              Date filters must be rolling windows — `first_seen_within_days` or
              `last_seen_within_days` — so the audience re-anchors on every refresh; fixed
              dates such as `first_seen_after` are rejected. Source values are canonical
              source paths (`whop:<campaign>:<group>:<ad>`, `ext:<platform>:...`,
              `referrer:<domain>`, `direct`), exact or with a trailing `:*` wildcard.

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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return cast(
            AudienceCreateResponse,
            self._post(
                "/audiences",
                body=maybe_transform(
                    {
                        "account_id": account_id,
                        "audience_type": audience_type,
                        "auto_refresh": auto_refresh,
                        "column_mapping": column_mapping,
                        "count": count,
                        "file_id": file_id,
                        "filters": filters,
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

    def update(
        self,
        audience_id: str,
        *,
        filters: object | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Audience:
        """Renames an audience.

        For an audience built from People filters that keeps itself
        up to date, pass `filters` to replace them, which rebuilds membership
        immediately. Whether an audience auto refreshes is set when it is created.

        Args:
          filters: Replaces the People filters that define membership. The whole definition is
              replaced rather than merged, so send every filter you want to keep — a filter
              you leave out stops applying. Keys and values are the ones `GET /people`
              accepts, such as an `os` of `iOS` or a `country` of `US`, and at least one
              filter is required. Date filters must be rolling windows —
              `first_seen_within_days` or `last_seen_within_days` — so the audience re-anchors
              every time it rebuilds; fixed dates such as `first_seen_after` are rejected, as
              is `audience_id`. An array value holds at most 500 items, and each value at most
              10 KB. Only an audience with a `source_type` of `people_filter` and
              `auto_refresh` of `true` accepts filters: an uploaded list has no filters to
              replace, and with auto refresh off the audience keeps the people it matched when
              it was built, so create a new audience instead.

          name: New audience display name. A blank value is ignored rather than clearing the
              name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        return self._patch(
            path_template("/audiences/{audience_id}", audience_id=audience_id),
            body=maybe_transform(
                {
                    "filters": filters,
                    "name": name,
                },
                audience_update_params.AudienceUpdateParams,
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
        audience_type: Literal["custom", "lookalike"] | Omit = omit,
        first: int | Omit = omit,
        source_type: Literal["csv_upload", "people_filter"] | Omit = omit,
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

          source_type: Filter by member source: `csv_upload` (uploaded lists) or `people_filter`
              (automatic audiences built from saved People filters).

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
                        "source_type": source_type,
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

    def add_people(
        self,
        audience_id: str,
        *,
        file_id: str,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Audience:
        """Adds users from a new CSV file to an existing uploaded custom audience.

        The file
        uses the audience's saved column mapping, processing happens in the background,
        and existing audience members remain unchanged.

        Args:
          file_id: The new customer CSV — a file id (`file_...`) returned by `POST /files`. Its
              headers must match the audience's saved column mapping.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/audiences/{audience_id}/add_people", audience_id=audience_id),
            body=maybe_transform({"file_id": file_id}, audience_add_people_params.AudienceAddPeopleParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Audience,
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
        auto_refresh: bool | Omit = omit,
        column_mapping: audience_create_params.ColumnMapping | Omit = omit,
        count: int | Omit = omit,
        file_id: str | Omit = omit,
        filters: object | Omit = omit,
        name: str | Omit = omit,
        percentage: int | Omit = omit,
        source_audience_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
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
        object. With `filters`: creates an audience from saved People filters (`name`
        required) — membership is built from the account's People data, and
        `auto_refresh` decides whether it keeps tracking the filters or keeps whoever
        matched at creation. With `audience_type: lookalike`: creates a ladder of Meta
        lookalike audiences from an existing ready custom audience
        (`source_audience_id`, `count`, and `percentage` required) — `count` equal
        similarity bands slicing the top `percentage`% (3 audiences at 6% = 0–2%, 2–4%,
        4–6%), each returned as its own audience in a `{ data: [...] }` envelope.

        Args:
          account_id: Account ID, prefixed `biz_`.

          audience_type: What to create. Defaults to `custom` (CSV upload).

          auto_refresh: Filter audiences only, and set only at creation. `true` (the default) rebuilds
              membership from the filters twice a day. `false` keeps whoever matched at
              creation and never rebuilds.

          column_mapping: Custom audiences only. Maps supported identity fields to CSV column headers. Map
              at least one of `email` or `phone`.

          count: Lookalikes only. Number of lookalike audiences to create (1–6).

          file_id: Custom audiences only. The uploaded customer CSV — a file id (`file_...`)
              returned by `POST /files`.

          filters: Filter audiences only. The People filters that define membership, keyed exactly
              as `GET /people` accepts them — for example `{"os": "iOS", "country": "US"}`.
              Date filters must be rolling windows — `first_seen_within_days` or
              `last_seen_within_days` — so the audience re-anchors on every refresh; fixed
              dates such as `first_seen_after` are rejected. Source values are canonical
              source paths (`whop:<campaign>:<group>:<ad>`, `ext:<platform>:...`,
              `referrer:<domain>`, `direct`), exact or with a trailing `:*` wildcard.

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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return cast(
            AudienceCreateResponse,
            await self._post(
                "/audiences",
                body=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "audience_type": audience_type,
                        "auto_refresh": auto_refresh,
                        "column_mapping": column_mapping,
                        "count": count,
                        "file_id": file_id,
                        "filters": filters,
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

    async def update(
        self,
        audience_id: str,
        *,
        filters: object | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Audience:
        """Renames an audience.

        For an audience built from People filters that keeps itself
        up to date, pass `filters` to replace them, which rebuilds membership
        immediately. Whether an audience auto refreshes is set when it is created.

        Args:
          filters: Replaces the People filters that define membership. The whole definition is
              replaced rather than merged, so send every filter you want to keep — a filter
              you leave out stops applying. Keys and values are the ones `GET /people`
              accepts, such as an `os` of `iOS` or a `country` of `US`, and at least one
              filter is required. Date filters must be rolling windows —
              `first_seen_within_days` or `last_seen_within_days` — so the audience re-anchors
              every time it rebuilds; fixed dates such as `first_seen_after` are rejected, as
              is `audience_id`. An array value holds at most 500 items, and each value at most
              10 KB. Only an audience with a `source_type` of `people_filter` and
              `auto_refresh` of `true` accepts filters: an uploaded list has no filters to
              replace, and with auto refresh off the audience keeps the people it matched when
              it was built, so create a new audience instead.

          name: New audience display name. A blank value is ignored rather than clearing the
              name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        return await self._patch(
            path_template("/audiences/{audience_id}", audience_id=audience_id),
            body=await async_maybe_transform(
                {
                    "filters": filters,
                    "name": name,
                },
                audience_update_params.AudienceUpdateParams,
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
        audience_type: Literal["custom", "lookalike"] | Omit = omit,
        first: int | Omit = omit,
        source_type: Literal["csv_upload", "people_filter"] | Omit = omit,
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

          source_type: Filter by member source: `csv_upload` (uploaded lists) or `people_filter`
              (automatic audiences built from saved People filters).

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
                        "source_type": source_type,
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

    async def add_people(
        self,
        audience_id: str,
        *,
        file_id: str,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Audience:
        """Adds users from a new CSV file to an existing uploaded custom audience.

        The file
        uses the audience's saved column mapping, processing happens in the background,
        and existing audience members remain unchanged.

        Args:
          file_id: The new customer CSV — a file id (`file_...`) returned by `POST /files`. Its
              headers must match the audience's saved column mapping.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/audiences/{audience_id}/add_people", audience_id=audience_id),
            body=await async_maybe_transform({"file_id": file_id}, audience_add_people_params.AudienceAddPeopleParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Audience,
        )


class AudiencesResourceWithRawResponse:
    def __init__(self, audiences: AudiencesResource) -> None:
        self._audiences = audiences

        self.create = to_raw_response_wrapper(
            audiences.create,
        )
        self.update = to_raw_response_wrapper(
            audiences.update,
        )
        self.list = to_raw_response_wrapper(
            audiences.list,
        )
        self.delete = to_raw_response_wrapper(
            audiences.delete,
        )
        self.add_people = to_raw_response_wrapper(
            audiences.add_people,
        )


class AsyncAudiencesResourceWithRawResponse:
    def __init__(self, audiences: AsyncAudiencesResource) -> None:
        self._audiences = audiences

        self.create = async_to_raw_response_wrapper(
            audiences.create,
        )
        self.update = async_to_raw_response_wrapper(
            audiences.update,
        )
        self.list = async_to_raw_response_wrapper(
            audiences.list,
        )
        self.delete = async_to_raw_response_wrapper(
            audiences.delete,
        )
        self.add_people = async_to_raw_response_wrapper(
            audiences.add_people,
        )


class AudiencesResourceWithStreamingResponse:
    def __init__(self, audiences: AudiencesResource) -> None:
        self._audiences = audiences

        self.create = to_streamed_response_wrapper(
            audiences.create,
        )
        self.update = to_streamed_response_wrapper(
            audiences.update,
        )
        self.list = to_streamed_response_wrapper(
            audiences.list,
        )
        self.delete = to_streamed_response_wrapper(
            audiences.delete,
        )
        self.add_people = to_streamed_response_wrapper(
            audiences.add_people,
        )


class AsyncAudiencesResourceWithStreamingResponse:
    def __init__(self, audiences: AsyncAudiencesResource) -> None:
        self._audiences = audiences

        self.create = async_to_streamed_response_wrapper(
            audiences.create,
        )
        self.update = async_to_streamed_response_wrapper(
            audiences.update,
        )
        self.list = async_to_streamed_response_wrapper(
            audiences.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            audiences.delete,
        )
        self.add_people = async_to_streamed_response_wrapper(
            audiences.add_people,
        )
