# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import file_create_params
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
from .._base_client import make_request_options
from ..types.file_create_response import FileCreateResponse
from ..types.file_retrieve_response import FileRetrieveResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    """A File is an uploaded document or media object, identified by a `file_` ID.

    Creating a file returns a presigned destination; upload the bytes there and the file becomes `ready`.

    Use the Files API to create a file, upload its content directly to storage (in one PUT, or in parts for large files), and retrieve it while polling for readiness. A ready file's ID can be attached wherever Whop accepts files.
    """

    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        filename: str,
        byte_size: int | Omit = omit,
        multipart: bool | Omit = omit,
        visibility: Literal["public", "private"] | Omit = omit,
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileCreateResponse:
        """Creates a file and returns a presigned destination to upload its bytes to.

        PUT
        the bytes to `upload_url` (single-part), or to each of `multipart_upload_urls`
        and then call Complete File Multipart Upload. Once the bytes land the file
        becomes `ready`, and its ID can be attached wherever a file is accepted —
        account legal documents, dispute evidence documents. For a step-by-step
        walkthrough of single-part and multipart uploads, see the
        [direct file uploads guide](/developer/guides/direct-file-uploads).

        Args:
          filename: The name of the file including its extension, e.g. `terms.pdf`.

          byte_size: The file's size in bytes. Required when `multipart` is `true`. Multipart uploads
              support at most 10,000 parts of 5MB each (about 50 GB).

          multipart: Upload the file in 5MB parts. Required for files larger than 5GB; useful above
              ~100MB. The file must be larger than 5MB.

          visibility: `public` files are served via an unsigned CDN URL — use for assets anyone may
              see. `private` files are served via a signed, expiring URL — use for sensitive
              documents. Defaults to `private`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/files",
            body=maybe_transform(
                {
                    "filename": filename,
                    "byte_size": byte_size,
                    "multipart": multipart,
                    "visibility": visibility,
                },
                file_create_params.FileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileRetrieveResponse:
        """
        Retrieves a file you uploaded — poll it after uploading the bytes to see
        `upload_status` become `ready`. Only the creator can retrieve a file this way; a
        file attached to another resource is read through that resource.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get(
            path_template("/files/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileRetrieveResponse,
        )


class AsyncFilesResource(AsyncAPIResource):
    """A File is an uploaded document or media object, identified by a `file_` ID.

    Creating a file returns a presigned destination; upload the bytes there and the file becomes `ready`.

    Use the Files API to create a file, upload its content directly to storage (in one PUT, or in parts for large files), and retrieve it while polling for readiness. A ready file's ID can be attached wherever Whop accepts files.
    """

    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        filename: str,
        byte_size: int | Omit = omit,
        multipart: bool | Omit = omit,
        visibility: Literal["public", "private"] | Omit = omit,
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileCreateResponse:
        """Creates a file and returns a presigned destination to upload its bytes to.

        PUT
        the bytes to `upload_url` (single-part), or to each of `multipart_upload_urls`
        and then call Complete File Multipart Upload. Once the bytes land the file
        becomes `ready`, and its ID can be attached wherever a file is accepted —
        account legal documents, dispute evidence documents. For a step-by-step
        walkthrough of single-part and multipart uploads, see the
        [direct file uploads guide](/developer/guides/direct-file-uploads).

        Args:
          filename: The name of the file including its extension, e.g. `terms.pdf`.

          byte_size: The file's size in bytes. Required when `multipart` is `true`. Multipart uploads
              support at most 10,000 parts of 5MB each (about 50 GB).

          multipart: Upload the file in 5MB parts. Required for files larger than 5GB; useful above
              ~100MB. The file must be larger than 5MB.

          visibility: `public` files are served via an unsigned CDN URL — use for assets anyone may
              see. `private` files are served via a signed, expiring URL — use for sensitive
              documents. Defaults to `private`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/files",
            body=await async_maybe_transform(
                {
                    "filename": filename,
                    "byte_size": byte_size,
                    "multipart": multipart,
                    "visibility": visibility,
                },
                file_create_params.FileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileRetrieveResponse:
        """
        Retrieves a file you uploaded — poll it after uploading the bytes to see
        `upload_status` become `ready`. Only the creator can retrieve a file this way; a
        file attached to another resource is read through that resource.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return await self._get(
            path_template("/files/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileRetrieveResponse,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.create = to_raw_response_wrapper(
            files.create,
        )
        self.retrieve = to_raw_response_wrapper(
            files.retrieve,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create = async_to_raw_response_wrapper(
            files.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            files.retrieve,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.create = to_streamed_response_wrapper(
            files.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            files.retrieve,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create = async_to_streamed_response_wrapper(
            files.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            files.retrieve,
        )
