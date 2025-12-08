# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    ExperienceListResponse,
    ExperienceDeleteResponse,
)
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.shared import Experience

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExperiences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        experience = client.experiences.create(
            app_id="app_xxxxxxxxxxxxxx",
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        experience = client.experiences.create(
            app_id="app_xxxxxxxxxxxxxx",
            company_id="biz_xxxxxxxxxxxxxx",
            is_public=True,
            name="name",
            section_id="section_id",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.experiences.with_raw_response.create(
            app_id="app_xxxxxxxxxxxxxx",
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = response.parse()
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.experiences.with_streaming_response.create(
            app_id="app_xxxxxxxxxxxxxx",
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = response.parse()
            assert_matches_type(Experience, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        experience = client.experiences.retrieve(
            "exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.experiences.with_raw_response.retrieve(
            "exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = response.parse()
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.experiences.with_streaming_response.retrieve(
            "exp_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = response.parse()
            assert_matches_type(Experience, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.experiences.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        experience = client.experiences.update(
            id="exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        experience = client.experiences.update(
            id="exp_xxxxxxxxxxxxxx",
            access_level="public",
            is_public=True,
            logo={"direct_upload_id": "direct_upload_id"},
            name="name",
            order="123.45",
            section_id="section_id",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.experiences.with_raw_response.update(
            id="exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = response.parse()
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.experiences.with_streaming_response.update(
            id="exp_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = response.parse()
            assert_matches_type(Experience, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.experiences.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        experience = client.experiences.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[ExperienceListResponse], experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        experience = client.experiences.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            app_id="app_xxxxxxxxxxxxxx",
            before="before",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            first=42,
            last=42,
            product_id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[ExperienceListResponse], experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.experiences.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = response.parse()
        assert_matches_type(SyncCursorPage[ExperienceListResponse], experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.experiences.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = response.parse()
            assert_matches_type(SyncCursorPage[ExperienceListResponse], experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        experience = client.experiences.delete(
            "exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(ExperienceDeleteResponse, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.experiences.with_raw_response.delete(
            "exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = response.parse()
        assert_matches_type(ExperienceDeleteResponse, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.experiences.with_streaming_response.delete(
            "exp_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = response.parse()
            assert_matches_type(ExperienceDeleteResponse, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.experiences.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_attach(self, client: Whop) -> None:
        experience = client.experiences.attach(
            id="exp_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_attach(self, client: Whop) -> None:
        response = client.experiences.with_raw_response.attach(
            id="exp_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = response.parse()
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_attach(self, client: Whop) -> None:
        with client.experiences.with_streaming_response.attach(
            id="exp_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = response.parse()
            assert_matches_type(Experience, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_attach(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.experiences.with_raw_response.attach(
                id="",
                product_id="prod_xxxxxxxxxxxxx",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_detach(self, client: Whop) -> None:
        experience = client.experiences.detach(
            id="exp_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_detach(self, client: Whop) -> None:
        response = client.experiences.with_raw_response.detach(
            id="exp_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = response.parse()
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_detach(self, client: Whop) -> None:
        with client.experiences.with_streaming_response.detach(
            id="exp_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = response.parse()
            assert_matches_type(Experience, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_detach(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.experiences.with_raw_response.detach(
                id="",
                product_id="prod_xxxxxxxxxxxxx",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_duplicate(self, client: Whop) -> None:
        experience = client.experiences.duplicate(
            id="exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_duplicate_with_all_params(self, client: Whop) -> None:
        experience = client.experiences.duplicate(
            id="exp_xxxxxxxxxxxxxx",
            name="name",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_duplicate(self, client: Whop) -> None:
        response = client.experiences.with_raw_response.duplicate(
            id="exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = response.parse()
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_duplicate(self, client: Whop) -> None:
        with client.experiences.with_streaming_response.duplicate(
            id="exp_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = response.parse()
            assert_matches_type(Experience, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_duplicate(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.experiences.with_raw_response.duplicate(
                id="",
            )


class TestAsyncExperiences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        experience = await async_client.experiences.create(
            app_id="app_xxxxxxxxxxxxxx",
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        experience = await async_client.experiences.create(
            app_id="app_xxxxxxxxxxxxxx",
            company_id="biz_xxxxxxxxxxxxxx",
            is_public=True,
            name="name",
            section_id="section_id",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.experiences.with_raw_response.create(
            app_id="app_xxxxxxxxxxxxxx",
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = await response.parse()
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.experiences.with_streaming_response.create(
            app_id="app_xxxxxxxxxxxxxx",
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = await response.parse()
            assert_matches_type(Experience, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        experience = await async_client.experiences.retrieve(
            "exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.experiences.with_raw_response.retrieve(
            "exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = await response.parse()
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.experiences.with_streaming_response.retrieve(
            "exp_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = await response.parse()
            assert_matches_type(Experience, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.experiences.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        experience = await async_client.experiences.update(
            id="exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        experience = await async_client.experiences.update(
            id="exp_xxxxxxxxxxxxxx",
            access_level="public",
            is_public=True,
            logo={"direct_upload_id": "direct_upload_id"},
            name="name",
            order="123.45",
            section_id="section_id",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.experiences.with_raw_response.update(
            id="exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = await response.parse()
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.experiences.with_streaming_response.update(
            id="exp_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = await response.parse()
            assert_matches_type(Experience, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.experiences.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        experience = await async_client.experiences.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[ExperienceListResponse], experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        experience = await async_client.experiences.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            app_id="app_xxxxxxxxxxxxxx",
            before="before",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            first=42,
            last=42,
            product_id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[ExperienceListResponse], experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.experiences.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = await response.parse()
        assert_matches_type(AsyncCursorPage[ExperienceListResponse], experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.experiences.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = await response.parse()
            assert_matches_type(AsyncCursorPage[ExperienceListResponse], experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        experience = await async_client.experiences.delete(
            "exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(ExperienceDeleteResponse, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.experiences.with_raw_response.delete(
            "exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = await response.parse()
        assert_matches_type(ExperienceDeleteResponse, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.experiences.with_streaming_response.delete(
            "exp_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = await response.parse()
            assert_matches_type(ExperienceDeleteResponse, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.experiences.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_attach(self, async_client: AsyncWhop) -> None:
        experience = await async_client.experiences.attach(
            id="exp_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_attach(self, async_client: AsyncWhop) -> None:
        response = await async_client.experiences.with_raw_response.attach(
            id="exp_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = await response.parse()
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_attach(self, async_client: AsyncWhop) -> None:
        async with async_client.experiences.with_streaming_response.attach(
            id="exp_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = await response.parse()
            assert_matches_type(Experience, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_attach(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.experiences.with_raw_response.attach(
                id="",
                product_id="prod_xxxxxxxxxxxxx",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_detach(self, async_client: AsyncWhop) -> None:
        experience = await async_client.experiences.detach(
            id="exp_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_detach(self, async_client: AsyncWhop) -> None:
        response = await async_client.experiences.with_raw_response.detach(
            id="exp_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = await response.parse()
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_detach(self, async_client: AsyncWhop) -> None:
        async with async_client.experiences.with_streaming_response.detach(
            id="exp_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = await response.parse()
            assert_matches_type(Experience, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_detach(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.experiences.with_raw_response.detach(
                id="",
                product_id="prod_xxxxxxxxxxxxx",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_duplicate(self, async_client: AsyncWhop) -> None:
        experience = await async_client.experiences.duplicate(
            id="exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_duplicate_with_all_params(self, async_client: AsyncWhop) -> None:
        experience = await async_client.experiences.duplicate(
            id="exp_xxxxxxxxxxxxxx",
            name="name",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_duplicate(self, async_client: AsyncWhop) -> None:
        response = await async_client.experiences.with_raw_response.duplicate(
            id="exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = await response.parse()
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_duplicate(self, async_client: AsyncWhop) -> None:
        async with async_client.experiences.with_streaming_response.duplicate(
            id="exp_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = await response.parse()
            assert_matches_type(Experience, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_duplicate(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.experiences.with_raw_response.duplicate(
                id="",
            )
