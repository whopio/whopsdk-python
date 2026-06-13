# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import Granularities, ad_report_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.granularities import Granularities
from ..types.ad_report_retrieve_response import AdReportRetrieveResponse

__all__ = ["AdReportsResource", "AsyncAdReportsResource"]


class AdReportsResource(SyncAPIResource):
    """Ad reports"""

    @cached_property
    def with_raw_response(self) -> AdReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AdReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AdReportsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        from_: Union[str, datetime],
        to: Union[str, datetime],
        ad_campaign_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        ad_group_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        ad_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        breakdown: Optional[Literal["campaign", "ad_group", "ad"]] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        granularity: Optional[Granularities] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdReportRetrieveResponse:
        """Performance report for a company, ad campaigns, ad groups, or ads.

        Always
        returns aggregate `summary` totals summed across the scope. Set `granularity` to
        additionally get a time series, or set `breakdown` (`campaign`/`ad_group`/`ad`)
        to additionally get per-entity rows inside the requested scope. Exactly one of
        `companyId`, `adCampaignIds`, `adGroupIds`, or `adIds` must be provided.

        Required permissions:

        - `ad_campaign:stats:read`

        Args:
          from_: Inclusive start of the reporting window.

          to: Inclusive end of the reporting window.

          ad_campaign_ids: Scope the report to these ad campaigns (max 100); stats are summed across them.
              Mutually exclusive with `companyId`, `adGroupIds`, and `adIds`.

          ad_group_ids: Scope the report to these ad groups (max 100); stats are summed across them.
              Mutually exclusive with `companyId`, `adCampaignIds`, and `adIds`.

          ad_ids: Scope the report to these ads (max 100); stats are summed across them. Mutually
              exclusive with `companyId`, `adCampaignIds`, and `adGroupIds`.

          breakdown: Entity level to group an ad report by.

          company_id: The unique identifier of a company. Mutually exclusive with `adCampaignIds`,
              `adGroupIds`, and `adIds`. Use with `breakdown` to fan out across every
              campaign, ad group, or ad in the company without paging.

          currency: ISO 4217 currency code to report `spend` in. Defaults to the company's ads
              reporting currency.

          granularity: Bucket size for external ad stat rows.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ad_reports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "ad_campaign_ids": ad_campaign_ids,
                        "ad_group_ids": ad_group_ids,
                        "ad_ids": ad_ids,
                        "breakdown": breakdown,
                        "company_id": company_id,
                        "currency": currency,
                        "granularity": granularity,
                    },
                    ad_report_retrieve_params.AdReportRetrieveParams,
                ),
            ),
            cast_to=AdReportRetrieveResponse,
        )


class AsyncAdReportsResource(AsyncAPIResource):
    """Ad reports"""

    @cached_property
    def with_raw_response(self) -> AsyncAdReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncAdReportsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        from_: Union[str, datetime],
        to: Union[str, datetime],
        ad_campaign_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        ad_group_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        ad_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        breakdown: Optional[Literal["campaign", "ad_group", "ad"]] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        granularity: Optional[Granularities] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdReportRetrieveResponse:
        """Performance report for a company, ad campaigns, ad groups, or ads.

        Always
        returns aggregate `summary` totals summed across the scope. Set `granularity` to
        additionally get a time series, or set `breakdown` (`campaign`/`ad_group`/`ad`)
        to additionally get per-entity rows inside the requested scope. Exactly one of
        `companyId`, `adCampaignIds`, `adGroupIds`, or `adIds` must be provided.

        Required permissions:

        - `ad_campaign:stats:read`

        Args:
          from_: Inclusive start of the reporting window.

          to: Inclusive end of the reporting window.

          ad_campaign_ids: Scope the report to these ad campaigns (max 100); stats are summed across them.
              Mutually exclusive with `companyId`, `adGroupIds`, and `adIds`.

          ad_group_ids: Scope the report to these ad groups (max 100); stats are summed across them.
              Mutually exclusive with `companyId`, `adCampaignIds`, and `adIds`.

          ad_ids: Scope the report to these ads (max 100); stats are summed across them. Mutually
              exclusive with `companyId`, `adCampaignIds`, and `adGroupIds`.

          breakdown: Entity level to group an ad report by.

          company_id: The unique identifier of a company. Mutually exclusive with `adCampaignIds`,
              `adGroupIds`, and `adIds`. Use with `breakdown` to fan out across every
              campaign, ad group, or ad in the company without paging.

          currency: ISO 4217 currency code to report `spend` in. Defaults to the company's ads
              reporting currency.

          granularity: Bucket size for external ad stat rows.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ad_reports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "ad_campaign_ids": ad_campaign_ids,
                        "ad_group_ids": ad_group_ids,
                        "ad_ids": ad_ids,
                        "breakdown": breakdown,
                        "company_id": company_id,
                        "currency": currency,
                        "granularity": granularity,
                    },
                    ad_report_retrieve_params.AdReportRetrieveParams,
                ),
            ),
            cast_to=AdReportRetrieveResponse,
        )


class AdReportsResourceWithRawResponse:
    def __init__(self, ad_reports: AdReportsResource) -> None:
        self._ad_reports = ad_reports

        self.retrieve = to_raw_response_wrapper(
            ad_reports.retrieve,
        )


class AsyncAdReportsResourceWithRawResponse:
    def __init__(self, ad_reports: AsyncAdReportsResource) -> None:
        self._ad_reports = ad_reports

        self.retrieve = async_to_raw_response_wrapper(
            ad_reports.retrieve,
        )


class AdReportsResourceWithStreamingResponse:
    def __init__(self, ad_reports: AdReportsResource) -> None:
        self._ad_reports = ad_reports

        self.retrieve = to_streamed_response_wrapper(
            ad_reports.retrieve,
        )


class AsyncAdReportsResourceWithStreamingResponse:
    def __init__(self, ad_reports: AsyncAdReportsResource) -> None:
        self._ad_reports = ad_reports

        self.retrieve = async_to_streamed_response_wrapper(
            ad_reports.retrieve,
        )
