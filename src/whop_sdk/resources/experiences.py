# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    experience_list_params,
    experience_attach_params,
    experience_create_params,
    experience_detach_params,
    experience_update_params,
    experience_duplicate_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
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
from ..types.shared.experience import Experience
from ..types.experience_list_response import ExperienceListResponse
from ..types.experience_delete_response import ExperienceDeleteResponse

__all__ = ["ExperiencesResource", "AsyncExperiencesResource"]


class ExperiencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExperiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return ExperiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExperiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return ExperiencesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        app_id: str,
        company_id: str,
        is_public: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        section_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Experience:
        """
        Required permissions:

        - `experience:create`

        Args:
          app_id: The ID of the app to create the experience for

          company_id: The ID of the company to create the experience for

          is_public: Whether the experience is publicly accessible

          name: The name of the experience

          section_id: The ID of the section to create the experience in

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/experiences",
            body=maybe_transform(
                {
                    "app_id": app_id,
                    "company_id": company_id,
                    "is_public": is_public,
                    "name": name,
                    "section_id": section_id,
                },
                experience_create_params.ExperienceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experience,
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
    ) -> Experience:
        """
        Retrieves an experience by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/experiences/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experience,
        )

    def update(
        self,
        id: str,
        *,
        access_level: Optional[Literal["public", "private"]] | Omit = omit,
        is_public: Optional[bool] | Omit = omit,
        logo: Optional[experience_update_params.Logo] | Omit = omit,
        name: Optional[str] | Omit = omit,
        order: Optional[str] | Omit = omit,
        section_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Experience:
        """
        Required permissions:

        - `experience:update`

        Args:
          access_level: The different access levels for experiences (PUBLIC IS NEVER USED ANYMORE).

          is_public: Whether the experience is publicly accessible.

          logo: The logo for the experience

          name: The name of the experience.

          order: The order of the experience in the section.

          section_id: The ID of the section to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/experiences/{id}",
            body=maybe_transform(
                {
                    "access_level": access_level,
                    "is_public": is_public,
                    "logo": logo,
                    "name": name,
                    "order": order,
                    "section_id": section_id,
                },
                experience_update_params.ExperienceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experience,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        app_id: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[ExperienceListResponse]:
        """
        Lists experiences for a company

        Required permissions:

        - `experience:hidden_experience:read`

        Args:
          company_id: The ID of the company to filter experiences by

          after: Returns the elements in the list that come after the specified cursor.

          app_id: The ID of the app to filter experiences by

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          product_id: The ID of the product to filter experiences by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/experiences",
            page=SyncCursorPage[ExperienceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "after": after,
                        "app_id": app_id,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "last": last,
                        "product_id": product_id,
                    },
                    experience_list_params.ExperienceListParams,
                ),
            ),
            model=ExperienceListResponse,
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
    ) -> ExperienceDeleteResponse:
        """
        Required permissions:

        - `experience:delete`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/experiences/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceDeleteResponse,
        )

    def attach(
        self,
        id: str,
        *,
        product_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Experience:
        """
        Adds an experience to an product, making it accessible to the product's
        customers.

        Required permissions:

        - `experience:attach`

        Args:
          product_id: The ID of the Access Pass to add the Experience to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/experiences/{id}/attach",
            body=maybe_transform({"product_id": product_id}, experience_attach_params.ExperienceAttachParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experience,
        )

    def detach(
        self,
        id: str,
        *,
        product_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Experience:
        """
        Removes an experience from an product, making it inaccessible to the product's
        customers.

        Required permissions:

        - `experience:detach`

        Args:
          product_id: The ID of the Access Pass to add the Experience to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/experiences/{id}/detach",
            body=maybe_transform({"product_id": product_id}, experience_detach_params.ExperienceDetachParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experience,
        )

    def duplicate(
        self,
        id: str,
        *,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Experience:
        """Duplicates an existing experience.

        The name will be copied, unless provided. The
        new experience will be attached to the same products as the original experience.
        If duplicating a Forum or Chat experience, the new experience will have the same
        settings as the original experience, e.g. who can post, who can comment, etc. No
        content, e.g. posts, messages, lessons from within the original experience will
        be copied.

        Required permissions:

        - `experience:create`

        Args:
          name: The name of the new experience

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/experiences/{id}/duplicate",
            body=maybe_transform({"name": name}, experience_duplicate_params.ExperienceDuplicateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experience,
        )


class AsyncExperiencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExperiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExperiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExperiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncExperiencesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        app_id: str,
        company_id: str,
        is_public: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        section_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Experience:
        """
        Required permissions:

        - `experience:create`

        Args:
          app_id: The ID of the app to create the experience for

          company_id: The ID of the company to create the experience for

          is_public: Whether the experience is publicly accessible

          name: The name of the experience

          section_id: The ID of the section to create the experience in

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/experiences",
            body=await async_maybe_transform(
                {
                    "app_id": app_id,
                    "company_id": company_id,
                    "is_public": is_public,
                    "name": name,
                    "section_id": section_id,
                },
                experience_create_params.ExperienceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experience,
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
    ) -> Experience:
        """
        Retrieves an experience by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/experiences/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experience,
        )

    async def update(
        self,
        id: str,
        *,
        access_level: Optional[Literal["public", "private"]] | Omit = omit,
        is_public: Optional[bool] | Omit = omit,
        logo: Optional[experience_update_params.Logo] | Omit = omit,
        name: Optional[str] | Omit = omit,
        order: Optional[str] | Omit = omit,
        section_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Experience:
        """
        Required permissions:

        - `experience:update`

        Args:
          access_level: The different access levels for experiences (PUBLIC IS NEVER USED ANYMORE).

          is_public: Whether the experience is publicly accessible.

          logo: The logo for the experience

          name: The name of the experience.

          order: The order of the experience in the section.

          section_id: The ID of the section to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/experiences/{id}",
            body=await async_maybe_transform(
                {
                    "access_level": access_level,
                    "is_public": is_public,
                    "logo": logo,
                    "name": name,
                    "order": order,
                    "section_id": section_id,
                },
                experience_update_params.ExperienceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experience,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        app_id: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ExperienceListResponse, AsyncCursorPage[ExperienceListResponse]]:
        """
        Lists experiences for a company

        Required permissions:

        - `experience:hidden_experience:read`

        Args:
          company_id: The ID of the company to filter experiences by

          after: Returns the elements in the list that come after the specified cursor.

          app_id: The ID of the app to filter experiences by

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          product_id: The ID of the product to filter experiences by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/experiences",
            page=AsyncCursorPage[ExperienceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "after": after,
                        "app_id": app_id,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "last": last,
                        "product_id": product_id,
                    },
                    experience_list_params.ExperienceListParams,
                ),
            ),
            model=ExperienceListResponse,
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
    ) -> ExperienceDeleteResponse:
        """
        Required permissions:

        - `experience:delete`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/experiences/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceDeleteResponse,
        )

    async def attach(
        self,
        id: str,
        *,
        product_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Experience:
        """
        Adds an experience to an product, making it accessible to the product's
        customers.

        Required permissions:

        - `experience:attach`

        Args:
          product_id: The ID of the Access Pass to add the Experience to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/experiences/{id}/attach",
            body=await async_maybe_transform(
                {"product_id": product_id}, experience_attach_params.ExperienceAttachParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experience,
        )

    async def detach(
        self,
        id: str,
        *,
        product_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Experience:
        """
        Removes an experience from an product, making it inaccessible to the product's
        customers.

        Required permissions:

        - `experience:detach`

        Args:
          product_id: The ID of the Access Pass to add the Experience to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/experiences/{id}/detach",
            body=await async_maybe_transform(
                {"product_id": product_id}, experience_detach_params.ExperienceDetachParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experience,
        )

    async def duplicate(
        self,
        id: str,
        *,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Experience:
        """Duplicates an existing experience.

        The name will be copied, unless provided. The
        new experience will be attached to the same products as the original experience.
        If duplicating a Forum or Chat experience, the new experience will have the same
        settings as the original experience, e.g. who can post, who can comment, etc. No
        content, e.g. posts, messages, lessons from within the original experience will
        be copied.

        Required permissions:

        - `experience:create`

        Args:
          name: The name of the new experience

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/experiences/{id}/duplicate",
            body=await async_maybe_transform({"name": name}, experience_duplicate_params.ExperienceDuplicateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experience,
        )


class ExperiencesResourceWithRawResponse:
    def __init__(self, experiences: ExperiencesResource) -> None:
        self._experiences = experiences

        self.create = to_raw_response_wrapper(
            experiences.create,
        )
        self.retrieve = to_raw_response_wrapper(
            experiences.retrieve,
        )
        self.update = to_raw_response_wrapper(
            experiences.update,
        )
        self.list = to_raw_response_wrapper(
            experiences.list,
        )
        self.delete = to_raw_response_wrapper(
            experiences.delete,
        )
        self.attach = to_raw_response_wrapper(
            experiences.attach,
        )
        self.detach = to_raw_response_wrapper(
            experiences.detach,
        )
        self.duplicate = to_raw_response_wrapper(
            experiences.duplicate,
        )


class AsyncExperiencesResourceWithRawResponse:
    def __init__(self, experiences: AsyncExperiencesResource) -> None:
        self._experiences = experiences

        self.create = async_to_raw_response_wrapper(
            experiences.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            experiences.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            experiences.update,
        )
        self.list = async_to_raw_response_wrapper(
            experiences.list,
        )
        self.delete = async_to_raw_response_wrapper(
            experiences.delete,
        )
        self.attach = async_to_raw_response_wrapper(
            experiences.attach,
        )
        self.detach = async_to_raw_response_wrapper(
            experiences.detach,
        )
        self.duplicate = async_to_raw_response_wrapper(
            experiences.duplicate,
        )


class ExperiencesResourceWithStreamingResponse:
    def __init__(self, experiences: ExperiencesResource) -> None:
        self._experiences = experiences

        self.create = to_streamed_response_wrapper(
            experiences.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            experiences.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            experiences.update,
        )
        self.list = to_streamed_response_wrapper(
            experiences.list,
        )
        self.delete = to_streamed_response_wrapper(
            experiences.delete,
        )
        self.attach = to_streamed_response_wrapper(
            experiences.attach,
        )
        self.detach = to_streamed_response_wrapper(
            experiences.detach,
        )
        self.duplicate = to_streamed_response_wrapper(
            experiences.duplicate,
        )


class AsyncExperiencesResourceWithStreamingResponse:
    def __init__(self, experiences: AsyncExperiencesResource) -> None:
        self._experiences = experiences

        self.create = async_to_streamed_response_wrapper(
            experiences.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            experiences.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            experiences.update,
        )
        self.list = async_to_streamed_response_wrapper(
            experiences.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            experiences.delete,
        )
        self.attach = async_to_streamed_response_wrapper(
            experiences.attach,
        )
        self.detach = async_to_streamed_response_wrapper(
            experiences.detach,
        )
        self.duplicate = async_to_streamed_response_wrapper(
            experiences.duplicate,
        )
