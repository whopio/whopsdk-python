# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from whopsdk import Whopsdk, AsyncWhopsdk
from tests.utils import assert_matches_type
from whopsdk.types import (
    ExperienceListResponse,
    ExperienceDeleteResponse,
)
from whopsdk.pagination import SyncCursorPage, AsyncCursorPage
from whopsdk.types.shared import Experience

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExperiences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whopsdk) -> None:
        experience = client.experiences.create(
            app_id="app_xxxxxxxxxxxxxx",
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whopsdk) -> None:
        experience = client.experiences.create(
            app_id="app_xxxxxxxxxxxxxx",
            company_id="biz_xxxxxxxxxxxxxx",
            name="name",
            section_id="section_id",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whopsdk) -> None:
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
    def test_streaming_response_create(self, client: Whopsdk) -> None:
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
    def test_method_retrieve(self, client: Whopsdk) -> None:
        experience = client.experiences.retrieve(
            "exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whopsdk) -> None:
        response = client.experiences.with_raw_response.retrieve(
            "exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = response.parse()
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whopsdk) -> None:
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
    def test_path_params_retrieve(self, client: Whopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.experiences.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Whopsdk) -> None:
        experience = client.experiences.update(
            id="exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whopsdk) -> None:
        experience = client.experiences.update(
            id="exp_xxxxxxxxxxxxxx",
            access_level="public",
            logo={
                "id": "id",
                "direct_upload_id": "direct_upload_id",
            },
            name="name",
            order="123.45",
            section_id="section_id",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whopsdk) -> None:
        response = client.experiences.with_raw_response.update(
            id="exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = response.parse()
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whopsdk) -> None:
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
    def test_path_params_update(self, client: Whopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.experiences.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whopsdk) -> None:
        experience = client.experiences.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[Optional[ExperienceListResponse]], experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whopsdk) -> None:
        experience = client.experiences.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            app_id="app_xxxxxxxxxxxxxx",
            before="before",
            first=42,
            last=42,
            product_id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[Optional[ExperienceListResponse]], experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whopsdk) -> None:
        response = client.experiences.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = response.parse()
        assert_matches_type(SyncCursorPage[Optional[ExperienceListResponse]], experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whopsdk) -> None:
        with client.experiences.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = response.parse()
            assert_matches_type(SyncCursorPage[Optional[ExperienceListResponse]], experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whopsdk) -> None:
        experience = client.experiences.delete(
            "exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(ExperienceDeleteResponse, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whopsdk) -> None:
        response = client.experiences.with_raw_response.delete(
            "exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = response.parse()
        assert_matches_type(ExperienceDeleteResponse, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whopsdk) -> None:
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
    def test_path_params_delete(self, client: Whopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.experiences.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_attach(self, client: Whopsdk) -> None:
        experience = client.experiences.attach(
            id="exp_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_attach(self, client: Whopsdk) -> None:
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
    def test_streaming_response_attach(self, client: Whopsdk) -> None:
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
    def test_path_params_attach(self, client: Whopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.experiences.with_raw_response.attach(
                id="",
                product_id="prod_xxxxxxxxxxxxx",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_detach(self, client: Whopsdk) -> None:
        experience = client.experiences.detach(
            id="exp_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_detach(self, client: Whopsdk) -> None:
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
    def test_streaming_response_detach(self, client: Whopsdk) -> None:
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
    def test_path_params_detach(self, client: Whopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.experiences.with_raw_response.detach(
                id="",
                product_id="prod_xxxxxxxxxxxxx",
            )


class TestAsyncExperiences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhopsdk) -> None:
        experience = await async_client.experiences.create(
            app_id="app_xxxxxxxxxxxxxx",
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhopsdk) -> None:
        experience = await async_client.experiences.create(
            app_id="app_xxxxxxxxxxxxxx",
            company_id="biz_xxxxxxxxxxxxxx",
            name="name",
            section_id="section_id",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhopsdk) -> None:
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
    async def test_streaming_response_create(self, async_client: AsyncWhopsdk) -> None:
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
    async def test_method_retrieve(self, async_client: AsyncWhopsdk) -> None:
        experience = await async_client.experiences.retrieve(
            "exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.experiences.with_raw_response.retrieve(
            "exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = await response.parse()
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhopsdk) -> None:
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
    async def test_path_params_retrieve(self, async_client: AsyncWhopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.experiences.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhopsdk) -> None:
        experience = await async_client.experiences.update(
            id="exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhopsdk) -> None:
        experience = await async_client.experiences.update(
            id="exp_xxxxxxxxxxxxxx",
            access_level="public",
            logo={
                "id": "id",
                "direct_upload_id": "direct_upload_id",
            },
            name="name",
            order="123.45",
            section_id="section_id",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.experiences.with_raw_response.update(
            id="exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = await response.parse()
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhopsdk) -> None:
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
    async def test_path_params_update(self, async_client: AsyncWhopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.experiences.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhopsdk) -> None:
        experience = await async_client.experiences.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[Optional[ExperienceListResponse]], experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhopsdk) -> None:
        experience = await async_client.experiences.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            app_id="app_xxxxxxxxxxxxxx",
            before="before",
            first=42,
            last=42,
            product_id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[Optional[ExperienceListResponse]], experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.experiences.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = await response.parse()
        assert_matches_type(AsyncCursorPage[Optional[ExperienceListResponse]], experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhopsdk) -> None:
        async with async_client.experiences.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = await response.parse()
            assert_matches_type(AsyncCursorPage[Optional[ExperienceListResponse]], experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhopsdk) -> None:
        experience = await async_client.experiences.delete(
            "exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(ExperienceDeleteResponse, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.experiences.with_raw_response.delete(
            "exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = await response.parse()
        assert_matches_type(ExperienceDeleteResponse, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhopsdk) -> None:
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
    async def test_path_params_delete(self, async_client: AsyncWhopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.experiences.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_attach(self, async_client: AsyncWhopsdk) -> None:
        experience = await async_client.experiences.attach(
            id="exp_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_attach(self, async_client: AsyncWhopsdk) -> None:
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
    async def test_streaming_response_attach(self, async_client: AsyncWhopsdk) -> None:
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
    async def test_path_params_attach(self, async_client: AsyncWhopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.experiences.with_raw_response.attach(
                id="",
                product_id="prod_xxxxxxxxxxxxx",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_detach(self, async_client: AsyncWhopsdk) -> None:
        experience = await async_client.experiences.detach(
            id="exp_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(Experience, experience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_detach(self, async_client: AsyncWhopsdk) -> None:
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
    async def test_streaming_response_detach(self, async_client: AsyncWhopsdk) -> None:
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
    async def test_path_params_detach(self, async_client: AsyncWhopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.experiences.with_raw_response.detach(
                id="",
                product_id="prod_xxxxxxxxxxxxx",
            )
