# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import media_generate_params
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
from .._base_client import make_request_options
from ..types.media_asset import MediaAsset

__all__ = ["MediaResource", "AsyncMediaResource"]


class MediaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return MediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return MediaResourceWithStreamingResponse(self)

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
    ) -> MediaAsset:
        """Retrieves a media asset by ID.

        Poll this while the asset is `processing`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/media/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaAsset,
        )

    def generate(
        self,
        *,
        prompt: str,
        type: Literal["video", "image"],
        account_id: str | Omit = omit,
        duration_seconds: Literal[5, 10, 15] | Omit = omit,
        reference_media: SequenceNotStr[str] | Omit = omit,
        resolution: Literal["480p", "720p", "1080p", "4k"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaAsset:
        """Starts an AI media generation job billed from the account's balance.

        Generation
        is asynchronous — poll `GET /media/{id}` until the asset is `ready`, then use
        `file.id` anywhere attachments are accepted.

        Args:
          prompt: What to generate. Up to 2,000 characters.

          type: The kind of media to generate.

          account_id: Account ID, prefixed `biz_`. Defaults to the account the API key belongs to.

          duration_seconds: Video length in seconds. Video only; defaults to 5.

          reference_media: Optional reference image file IDs (`file_` prefixed), up to 4. For video, a
              single reference seeds the opening frame; multiple references guide subject and
              style instead.

          resolution: Video resolution. Video only; defaults to `1080p`. `1080p` is not supported by
              Seedance 2.0 Fast or Mini; `4k` is only supported by Seedance 2.0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/media/generate",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "type": type,
                    "account_id": account_id,
                    "duration_seconds": duration_seconds,
                    "reference_media": reference_media,
                    "resolution": resolution,
                },
                media_generate_params.MediaGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaAsset,
        )


class AsyncMediaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncMediaResourceWithStreamingResponse(self)

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
    ) -> MediaAsset:
        """Retrieves a media asset by ID.

        Poll this while the asset is `processing`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/media/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaAsset,
        )

    async def generate(
        self,
        *,
        prompt: str,
        type: Literal["video", "image"],
        account_id: str | Omit = omit,
        duration_seconds: Literal[5, 10, 15] | Omit = omit,
        reference_media: SequenceNotStr[str] | Omit = omit,
        resolution: Literal["480p", "720p", "1080p", "4k"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaAsset:
        """Starts an AI media generation job billed from the account's balance.

        Generation
        is asynchronous — poll `GET /media/{id}` until the asset is `ready`, then use
        `file.id` anywhere attachments are accepted.

        Args:
          prompt: What to generate. Up to 2,000 characters.

          type: The kind of media to generate.

          account_id: Account ID, prefixed `biz_`. Defaults to the account the API key belongs to.

          duration_seconds: Video length in seconds. Video only; defaults to 5.

          reference_media: Optional reference image file IDs (`file_` prefixed), up to 4. For video, a
              single reference seeds the opening frame; multiple references guide subject and
              style instead.

          resolution: Video resolution. Video only; defaults to `1080p`. `1080p` is not supported by
              Seedance 2.0 Fast or Mini; `4k` is only supported by Seedance 2.0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/media/generate",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "type": type,
                    "account_id": account_id,
                    "duration_seconds": duration_seconds,
                    "reference_media": reference_media,
                    "resolution": resolution,
                },
                media_generate_params.MediaGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaAsset,
        )


class MediaResourceWithRawResponse:
    def __init__(self, media: MediaResource) -> None:
        self._media = media

        self.retrieve = to_raw_response_wrapper(
            media.retrieve,
        )
        self.generate = to_raw_response_wrapper(
            media.generate,
        )


class AsyncMediaResourceWithRawResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
        self._media = media

        self.retrieve = async_to_raw_response_wrapper(
            media.retrieve,
        )
        self.generate = async_to_raw_response_wrapper(
            media.generate,
        )


class MediaResourceWithStreamingResponse:
    def __init__(self, media: MediaResource) -> None:
        self._media = media

        self.retrieve = to_streamed_response_wrapper(
            media.retrieve,
        )
        self.generate = to_streamed_response_wrapper(
            media.generate,
        )


class AsyncMediaResourceWithStreamingResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
        self._media = media

        self.retrieve = async_to_streamed_response_wrapper(
            media.retrieve,
        )
        self.generate = async_to_streamed_response_wrapper(
            media.generate,
        )
