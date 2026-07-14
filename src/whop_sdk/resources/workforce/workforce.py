# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .bounties import (
    BountiesResource,
    AsyncBountiesResource,
    BountiesResourceWithRawResponse,
    AsyncBountiesResourceWithRawResponse,
    BountiesResourceWithStreamingResponse,
    AsyncBountiesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["WorkforceResource", "AsyncWorkforceResource"]


class WorkforceResource(SyncAPIResource):
    @cached_property
    def bounties(self) -> BountiesResource:
        """A Workforce Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Workforce Bounties API to list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        return BountiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkforceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return WorkforceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkforceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return WorkforceResourceWithStreamingResponse(self)


class AsyncWorkforceResource(AsyncAPIResource):
    @cached_property
    def bounties(self) -> AsyncBountiesResource:
        """A Workforce Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Workforce Bounties API to list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        return AsyncBountiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkforceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkforceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkforceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncWorkforceResourceWithStreamingResponse(self)


class WorkforceResourceWithRawResponse:
    def __init__(self, workforce: WorkforceResource) -> None:
        self._workforce = workforce

    @cached_property
    def bounties(self) -> BountiesResourceWithRawResponse:
        """A Workforce Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Workforce Bounties API to list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        return BountiesResourceWithRawResponse(self._workforce.bounties)


class AsyncWorkforceResourceWithRawResponse:
    def __init__(self, workforce: AsyncWorkforceResource) -> None:
        self._workforce = workforce

    @cached_property
    def bounties(self) -> AsyncBountiesResourceWithRawResponse:
        """A Workforce Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Workforce Bounties API to list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        return AsyncBountiesResourceWithRawResponse(self._workforce.bounties)


class WorkforceResourceWithStreamingResponse:
    def __init__(self, workforce: WorkforceResource) -> None:
        self._workforce = workforce

    @cached_property
    def bounties(self) -> BountiesResourceWithStreamingResponse:
        """A Workforce Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Workforce Bounties API to list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        return BountiesResourceWithStreamingResponse(self._workforce.bounties)


class AsyncWorkforceResourceWithStreamingResponse:
    def __init__(self, workforce: AsyncWorkforceResource) -> None:
        self._workforce = workforce

    @cached_property
    def bounties(self) -> AsyncBountiesResourceWithStreamingResponse:
        """A Workforce Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Workforce Bounties API to list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        return AsyncBountiesResourceWithStreamingResponse(self._workforce.bounties)
