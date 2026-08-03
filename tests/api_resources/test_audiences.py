# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    Audience,
    AudienceCreateResponse,
    AudienceDeleteResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudiences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        audience = client.audiences.create(
            account_id="account_id",
        )
        assert_matches_type(AudienceCreateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        audience = client.audiences.create(
            account_id="account_id",
            audience_type="custom",
            auto_refresh=True,
            column_mapping={
                "country": "country",
                "email": "email",
                "first_name": "first_name",
                "last_name": "last_name",
                "phone": "phone",
            },
            count=0,
            file_id="file_id",
            filters={},
            name="name",
            percentage=0,
            source_audience_id="source_audience_id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AudienceCreateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.audiences.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(AudienceCreateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.audiences.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(AudienceCreateResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        audience = client.audiences.update(
            audience_id="audience_id",
        )
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        audience = client.audiences.update(
            audience_id="audience_id",
            filters={},
            name="name",
        )
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.audiences.with_raw_response.update(
            audience_id="audience_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.audiences.with_streaming_response.update(
            audience_id="audience_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(Audience, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            client.audiences.with_raw_response.update(
                audience_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        audience = client.audiences.list(
            account_id="account_id",
        )
        assert_matches_type(SyncCursorPage[Audience], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        audience = client.audiences.list(
            account_id="account_id",
            after="after",
            audience_id="audience_id",
            audience_type="custom",
            first=0,
            source_type="csv_upload",
        )
        assert_matches_type(SyncCursorPage[Audience], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.audiences.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(SyncCursorPage[Audience], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.audiences.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(SyncCursorPage[Audience], audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        audience = client.audiences.delete(
            "audience_id",
        )
        assert_matches_type(AudienceDeleteResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.audiences.with_raw_response.delete(
            "audience_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(AudienceDeleteResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.audiences.with_streaming_response.delete(
            "audience_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(AudienceDeleteResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            client.audiences.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_people(self, client: Whop) -> None:
        audience = client.audiences.add_people(
            audience_id="audience_id",
            file_id="file_id",
        )
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_people_with_all_params(self, client: Whop) -> None:
        audience = client.audiences.add_people(
            audience_id="audience_id",
            file_id="file_id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_people(self, client: Whop) -> None:
        response = client.audiences.with_raw_response.add_people(
            audience_id="audience_id",
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_people(self, client: Whop) -> None:
        with client.audiences.with_streaming_response.add_people(
            audience_id="audience_id",
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(Audience, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_people(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            client.audiences.with_raw_response.add_people(
                audience_id="",
                file_id="file_id",
            )


class TestAsyncAudiences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        audience = await async_client.audiences.create(
            account_id="account_id",
        )
        assert_matches_type(AudienceCreateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        audience = await async_client.audiences.create(
            account_id="account_id",
            audience_type="custom",
            auto_refresh=True,
            column_mapping={
                "country": "country",
                "email": "email",
                "first_name": "first_name",
                "last_name": "last_name",
                "phone": "phone",
            },
            count=0,
            file_id="file_id",
            filters={},
            name="name",
            percentage=0,
            source_audience_id="source_audience_id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AudienceCreateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.audiences.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(AudienceCreateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.audiences.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(AudienceCreateResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        audience = await async_client.audiences.update(
            audience_id="audience_id",
        )
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        audience = await async_client.audiences.update(
            audience_id="audience_id",
            filters={},
            name="name",
        )
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.audiences.with_raw_response.update(
            audience_id="audience_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.audiences.with_streaming_response.update(
            audience_id="audience_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(Audience, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            await async_client.audiences.with_raw_response.update(
                audience_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        audience = await async_client.audiences.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncCursorPage[Audience], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        audience = await async_client.audiences.list(
            account_id="account_id",
            after="after",
            audience_id="audience_id",
            audience_type="custom",
            first=0,
            source_type="csv_upload",
        )
        assert_matches_type(AsyncCursorPage[Audience], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.audiences.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(AsyncCursorPage[Audience], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.audiences.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(AsyncCursorPage[Audience], audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        audience = await async_client.audiences.delete(
            "audience_id",
        )
        assert_matches_type(AudienceDeleteResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.audiences.with_raw_response.delete(
            "audience_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(AudienceDeleteResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.audiences.with_streaming_response.delete(
            "audience_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(AudienceDeleteResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            await async_client.audiences.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_people(self, async_client: AsyncWhop) -> None:
        audience = await async_client.audiences.add_people(
            audience_id="audience_id",
            file_id="file_id",
        )
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_people_with_all_params(self, async_client: AsyncWhop) -> None:
        audience = await async_client.audiences.add_people(
            audience_id="audience_id",
            file_id="file_id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_people(self, async_client: AsyncWhop) -> None:
        response = await async_client.audiences.with_raw_response.add_people(
            audience_id="audience_id",
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_people(self, async_client: AsyncWhop) -> None:
        async with async_client.audiences.with_streaming_response.add_people(
            audience_id="audience_id",
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(Audience, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_people(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            await async_client.audiences.with_raw_response.add_people(
                audience_id="",
                file_id="file_id",
            )
