# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import ad_campaign_list_params, ad_campaign_create_params, ad_campaign_update_params
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
from ..types.ad_campaign_list_response import AdCampaignListResponse
from ..types.ad_campaign_pause_response import AdCampaignPauseResponse
from ..types.ad_campaign_create_response import AdCampaignCreateResponse
from ..types.ad_campaign_update_response import AdCampaignUpdateResponse
from ..types.ad_campaign_unpause_response import AdCampaignUnpauseResponse
from ..types.ad_campaign_retrieve_response import AdCampaignRetrieveResponse

__all__ = ["AdCampaignsResource", "AsyncAdCampaignsResource"]


class AdCampaignsResource(SyncAPIResource):
    """Ad campaigns"""

    @cached_property
    def with_raw_response(self) -> AdCampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AdCampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdCampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AdCampaignsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_id: str,
        config: ad_campaign_create_params.Config,
        platform: Literal["meta", "tiktok"],
        title: str,
        ad_creative_set_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        budget: Optional[float] | Omit = omit,
        budget_type: Optional[Literal["daily", "lifetime"]] | Omit = omit,
        daily_budget: Optional[float] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        target_country_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaignCreateResponse:
        """
        Creates a new ad campaign for a product.

        Required permissions:

        - `ad_campaign:create`
        - `access_pass:basic:read`
        - `company:balance:read`

        Args:
          company_id: The company ID to create this ad campaign for.

          config: Unified campaign configuration (conversion goal, budget, bidding, etc.).

          platform: The ad platform to run on (e.g., meta, tiktok).

          title: The title of the ad campaign. Must be max 100 characters.

          ad_creative_set_ids: Array of creative set IDs to link to this campaign.

          budget: Budget amount in dollars.

          budget_type: The budget type for an ad campaign or ad group.

          daily_budget: Daily budget in dollars (minimum $5). Required unless lifetime_budget is set in
              config.

          product_id: The unique identifier of the product to promote.

          target_country_codes: Array of ISO3166 country codes for territory targeting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ad_campaigns",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "config": config,
                    "platform": platform,
                    "title": title,
                    "ad_creative_set_ids": ad_creative_set_ids,
                    "budget": budget,
                    "budget_type": budget_type,
                    "daily_budget": daily_budget,
                    "product_id": product_id,
                    "target_country_codes": target_country_codes,
                },
                ad_campaign_create_params.AdCampaignCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaignCreateResponse,
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
    ) -> AdCampaignRetrieveResponse:
        """
        Retrieves a single ad campaign by its unique identifier.

        Required permissions:

        - `ad_campaign:basic:read`
        - `access_pass:basic:read`
        - `company:balance:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/ad_campaigns/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaignRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        ad_creative_set_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        budget: Optional[float] | Omit = omit,
        budget_type: Optional[Literal["daily", "lifetime"]] | Omit = omit,
        config: Optional[ad_campaign_update_params.Config] | Omit = omit,
        daily_budget: Optional[float] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        target_country_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaignUpdateResponse:
        """
        Updates an existing ad campaign.

        Required permissions:

        - `ad_campaign:update`
        - `access_pass:basic:read`
        - `company:balance:read`

        Args:
          ad_creative_set_ids: Array of creative set IDs to link to this campaign.

          budget: Budget amount in dollars.

          budget_type: The budget type for an ad campaign or ad group.

          config: Unified campaign configuration (conversion goal, budget, bidding, etc.).

          daily_budget: Daily budget in dollars (minimum $5).

          product_id: The unique identifier of the product (access pass) to promote.

          target_country_codes: Array of ISO3166 country codes for territory targeting.

          title: The title of the ad campaign. Must be max 100 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/ad_campaigns/{id}", id=id),
            body=maybe_transform(
                {
                    "ad_creative_set_ids": ad_creative_set_ids,
                    "budget": budget,
                    "budget_type": budget_type,
                    "config": config,
                    "daily_budget": daily_budget,
                    "product_id": product_id,
                    "target_country_codes": target_country_codes,
                    "title": title,
                },
                ad_campaign_update_params.AdCampaignUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaignUpdateResponse,
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
        query: Optional[str] | Omit = omit,
        status: Optional[
            Literal[
                "active",
                "paused",
                "inactive",
                "stale",
                "pending_refund",
                "payment_failed",
                "draft",
                "in_review",
                "flagged",
                "importing",
                "imported",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AdCampaignListResponse]:
        """
        Returns a paginated list of ad campaigns for a company, with optional filtering
        by status, and creation date.

        Required permissions:

        - `ad_campaign:basic:read`
        - `access_pass:basic:read`

        Args:
          company_id: The unique identifier of the company to list ad campaigns for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return ad campaigns created after this timestamp.

          created_before: Only return ad campaigns created before this timestamp.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          query: Case-insensitive substring match against the campaign title.

          status: The status of an ad campaign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ad_campaigns",
            page=SyncCursorPage[AdCampaignListResponse],
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
                        "query": query,
                        "status": status,
                    },
                    ad_campaign_list_params.AdCampaignListParams,
                ),
            ),
            model=AdCampaignListResponse,
        )

    def pause(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaignPauseResponse:
        """
        Pauses an ad campaign, optionally until a specific date.

        Required permissions:

        - `ad_campaign:update`
        - `access_pass:basic:read`
        - `company:balance:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/ad_campaigns/{id}/pause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaignPauseResponse,
        )

    def unpause(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaignUnpauseResponse:
        """
        Resumes a paused ad campaign.

        Required permissions:

        - `ad_campaign:update`
        - `access_pass:basic:read`
        - `company:balance:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/ad_campaigns/{id}/unpause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaignUnpauseResponse,
        )


class AsyncAdCampaignsResource(AsyncAPIResource):
    """Ad campaigns"""

    @cached_property
    def with_raw_response(self) -> AsyncAdCampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdCampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdCampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncAdCampaignsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_id: str,
        config: ad_campaign_create_params.Config,
        platform: Literal["meta", "tiktok"],
        title: str,
        ad_creative_set_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        budget: Optional[float] | Omit = omit,
        budget_type: Optional[Literal["daily", "lifetime"]] | Omit = omit,
        daily_budget: Optional[float] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        target_country_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaignCreateResponse:
        """
        Creates a new ad campaign for a product.

        Required permissions:

        - `ad_campaign:create`
        - `access_pass:basic:read`
        - `company:balance:read`

        Args:
          company_id: The company ID to create this ad campaign for.

          config: Unified campaign configuration (conversion goal, budget, bidding, etc.).

          platform: The ad platform to run on (e.g., meta, tiktok).

          title: The title of the ad campaign. Must be max 100 characters.

          ad_creative_set_ids: Array of creative set IDs to link to this campaign.

          budget: Budget amount in dollars.

          budget_type: The budget type for an ad campaign or ad group.

          daily_budget: Daily budget in dollars (minimum $5). Required unless lifetime_budget is set in
              config.

          product_id: The unique identifier of the product to promote.

          target_country_codes: Array of ISO3166 country codes for territory targeting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ad_campaigns",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "config": config,
                    "platform": platform,
                    "title": title,
                    "ad_creative_set_ids": ad_creative_set_ids,
                    "budget": budget,
                    "budget_type": budget_type,
                    "daily_budget": daily_budget,
                    "product_id": product_id,
                    "target_country_codes": target_country_codes,
                },
                ad_campaign_create_params.AdCampaignCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaignCreateResponse,
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
    ) -> AdCampaignRetrieveResponse:
        """
        Retrieves a single ad campaign by its unique identifier.

        Required permissions:

        - `ad_campaign:basic:read`
        - `access_pass:basic:read`
        - `company:balance:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/ad_campaigns/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaignRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        ad_creative_set_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        budget: Optional[float] | Omit = omit,
        budget_type: Optional[Literal["daily", "lifetime"]] | Omit = omit,
        config: Optional[ad_campaign_update_params.Config] | Omit = omit,
        daily_budget: Optional[float] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        target_country_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaignUpdateResponse:
        """
        Updates an existing ad campaign.

        Required permissions:

        - `ad_campaign:update`
        - `access_pass:basic:read`
        - `company:balance:read`

        Args:
          ad_creative_set_ids: Array of creative set IDs to link to this campaign.

          budget: Budget amount in dollars.

          budget_type: The budget type for an ad campaign or ad group.

          config: Unified campaign configuration (conversion goal, budget, bidding, etc.).

          daily_budget: Daily budget in dollars (minimum $5).

          product_id: The unique identifier of the product (access pass) to promote.

          target_country_codes: Array of ISO3166 country codes for territory targeting.

          title: The title of the ad campaign. Must be max 100 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/ad_campaigns/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "ad_creative_set_ids": ad_creative_set_ids,
                    "budget": budget,
                    "budget_type": budget_type,
                    "config": config,
                    "daily_budget": daily_budget,
                    "product_id": product_id,
                    "target_country_codes": target_country_codes,
                    "title": title,
                },
                ad_campaign_update_params.AdCampaignUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaignUpdateResponse,
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
        query: Optional[str] | Omit = omit,
        status: Optional[
            Literal[
                "active",
                "paused",
                "inactive",
                "stale",
                "pending_refund",
                "payment_failed",
                "draft",
                "in_review",
                "flagged",
                "importing",
                "imported",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AdCampaignListResponse, AsyncCursorPage[AdCampaignListResponse]]:
        """
        Returns a paginated list of ad campaigns for a company, with optional filtering
        by status, and creation date.

        Required permissions:

        - `ad_campaign:basic:read`
        - `access_pass:basic:read`

        Args:
          company_id: The unique identifier of the company to list ad campaigns for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return ad campaigns created after this timestamp.

          created_before: Only return ad campaigns created before this timestamp.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          query: Case-insensitive substring match against the campaign title.

          status: The status of an ad campaign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ad_campaigns",
            page=AsyncCursorPage[AdCampaignListResponse],
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
                        "query": query,
                        "status": status,
                    },
                    ad_campaign_list_params.AdCampaignListParams,
                ),
            ),
            model=AdCampaignListResponse,
        )

    async def pause(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaignPauseResponse:
        """
        Pauses an ad campaign, optionally until a specific date.

        Required permissions:

        - `ad_campaign:update`
        - `access_pass:basic:read`
        - `company:balance:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/ad_campaigns/{id}/pause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaignPauseResponse,
        )

    async def unpause(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaignUnpauseResponse:
        """
        Resumes a paused ad campaign.

        Required permissions:

        - `ad_campaign:update`
        - `access_pass:basic:read`
        - `company:balance:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/ad_campaigns/{id}/unpause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaignUnpauseResponse,
        )


class AdCampaignsResourceWithRawResponse:
    def __init__(self, ad_campaigns: AdCampaignsResource) -> None:
        self._ad_campaigns = ad_campaigns

        self.create = to_raw_response_wrapper(
            ad_campaigns.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ad_campaigns.retrieve,
        )
        self.update = to_raw_response_wrapper(
            ad_campaigns.update,
        )
        self.list = to_raw_response_wrapper(
            ad_campaigns.list,
        )
        self.pause = to_raw_response_wrapper(
            ad_campaigns.pause,
        )
        self.unpause = to_raw_response_wrapper(
            ad_campaigns.unpause,
        )


class AsyncAdCampaignsResourceWithRawResponse:
    def __init__(self, ad_campaigns: AsyncAdCampaignsResource) -> None:
        self._ad_campaigns = ad_campaigns

        self.create = async_to_raw_response_wrapper(
            ad_campaigns.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ad_campaigns.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            ad_campaigns.update,
        )
        self.list = async_to_raw_response_wrapper(
            ad_campaigns.list,
        )
        self.pause = async_to_raw_response_wrapper(
            ad_campaigns.pause,
        )
        self.unpause = async_to_raw_response_wrapper(
            ad_campaigns.unpause,
        )


class AdCampaignsResourceWithStreamingResponse:
    def __init__(self, ad_campaigns: AdCampaignsResource) -> None:
        self._ad_campaigns = ad_campaigns

        self.create = to_streamed_response_wrapper(
            ad_campaigns.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ad_campaigns.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ad_campaigns.update,
        )
        self.list = to_streamed_response_wrapper(
            ad_campaigns.list,
        )
        self.pause = to_streamed_response_wrapper(
            ad_campaigns.pause,
        )
        self.unpause = to_streamed_response_wrapper(
            ad_campaigns.unpause,
        )


class AsyncAdCampaignsResourceWithStreamingResponse:
    def __init__(self, ad_campaigns: AsyncAdCampaignsResource) -> None:
        self._ad_campaigns = ad_campaigns

        self.create = async_to_streamed_response_wrapper(
            ad_campaigns.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ad_campaigns.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ad_campaigns.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ad_campaigns.list,
        )
        self.pause = async_to_streamed_response_wrapper(
            ad_campaigns.pause,
        )
        self.unpause = async_to_streamed_response_wrapper(
            ad_campaigns.unpause,
        )
