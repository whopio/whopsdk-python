# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    AdGroup,
    AdGroupListResponse,
    AdGroupDeleteResponse,
)
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        ad_group = client.ad_groups.retrieve(
            id="adgrp_xxxxxxxxxxxx",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Whop) -> None:
        ad_group = client.ad_groups.retrieve(
            id="adgrp_xxxxxxxxxxxx",
            stats_from=parse_datetime("2023-12-01T05:00:00.401Z"),
            stats_to=parse_datetime("2023-12-01T05:00:00.401Z"),
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.retrieve(
            id="adgrp_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.retrieve(
            id="adgrp_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ad_groups.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        ad_group = client.ad_groups.update(
            id="adgrp_xxxxxxxxxxxx",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        ad_group = client.ad_groups.update(
            id="adgrp_xxxxxxxxxxxx",
            budget=6.9,
            title="title",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.update(
            id="adgrp_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.update(
            id="adgrp_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ad_groups.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        ad_group = client.ad_groups.list()
        assert_matches_type(SyncCursorPage[AdGroupListResponse], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        ad_group = client.ad_groups.list(
            ad_campaign_id="ad_campaign_id",
            ad_campaign_ids=["string"],
            after="after",
            before="before",
            campaign_id="campaign_id",
            company_id="biz_xxxxxxxxxxxxxx",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            direction="asc",
            first=42,
            last=42,
            order="created_at",
            query="query",
            stats_from=parse_datetime("2023-12-01T05:00:00.401Z"),
            stats_to=parse_datetime("2023-12-01T05:00:00.401Z"),
            status="active",
        )
        assert_matches_type(SyncCursorPage[AdGroupListResponse], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(SyncCursorPage[AdGroupListResponse], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(SyncCursorPage[AdGroupListResponse], ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        ad_group = client.ad_groups.delete(
            "adgrp_xxxxxxxxxxxx",
        )
        assert_matches_type(AdGroupDeleteResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.delete(
            "adgrp_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(AdGroupDeleteResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.delete(
            "adgrp_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(AdGroupDeleteResponse, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ad_groups.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pause(self, client: Whop) -> None:
        ad_group = client.ad_groups.pause(
            "adgrp_xxxxxxxxxxxx",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_pause(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.pause(
            "adgrp_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_pause(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.pause(
            "adgrp_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_pause(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ad_groups.with_raw_response.pause(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unpause(self, client: Whop) -> None:
        ad_group = client.ad_groups.unpause(
            "adgrp_xxxxxxxxxxxx",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unpause(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.unpause(
            "adgrp_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unpause(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.unpause(
            "adgrp_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unpause(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ad_groups.with_raw_response.unpause(
                "",
            )


class TestAsyncAdGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.retrieve(
            id="adgrp_xxxxxxxxxxxx",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.retrieve(
            id="adgrp_xxxxxxxxxxxx",
            stats_from=parse_datetime("2023-12-01T05:00:00.401Z"),
            stats_to=parse_datetime("2023-12-01T05:00:00.401Z"),
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.retrieve(
            id="adgrp_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.retrieve(
            id="adgrp_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ad_groups.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.update(
            id="adgrp_xxxxxxxxxxxx",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.update(
            id="adgrp_xxxxxxxxxxxx",
            budget=6.9,
            title="title",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.update(
            id="adgrp_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.update(
            id="adgrp_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ad_groups.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.list()
        assert_matches_type(AsyncCursorPage[AdGroupListResponse], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.list(
            ad_campaign_id="ad_campaign_id",
            ad_campaign_ids=["string"],
            after="after",
            before="before",
            campaign_id="campaign_id",
            company_id="biz_xxxxxxxxxxxxxx",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            direction="asc",
            first=42,
            last=42,
            order="created_at",
            query="query",
            stats_from=parse_datetime("2023-12-01T05:00:00.401Z"),
            stats_to=parse_datetime("2023-12-01T05:00:00.401Z"),
            status="active",
        )
        assert_matches_type(AsyncCursorPage[AdGroupListResponse], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AsyncCursorPage[AdGroupListResponse], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AsyncCursorPage[AdGroupListResponse], ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.delete(
            "adgrp_xxxxxxxxxxxx",
        )
        assert_matches_type(AdGroupDeleteResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.delete(
            "adgrp_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AdGroupDeleteResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.delete(
            "adgrp_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AdGroupDeleteResponse, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ad_groups.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pause(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.pause(
            "adgrp_xxxxxxxxxxxx",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_pause(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.pause(
            "adgrp_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_pause(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.pause(
            "adgrp_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_pause(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ad_groups.with_raw_response.pause(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unpause(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.unpause(
            "adgrp_xxxxxxxxxxxx",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unpause(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.unpause(
            "adgrp_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unpause(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.unpause(
            "adgrp_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unpause(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ad_groups.with_raw_response.unpause(
                "",
            )
