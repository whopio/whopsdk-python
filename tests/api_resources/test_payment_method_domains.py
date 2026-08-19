# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    PaymentMethodDomain,
    PaymentMethodDomainDeleteResponse,
)
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentMethodDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        payment_method_domain = client.payment_method_domains.create(
            hostname="pending.shinetime.example",
        )
        assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        payment_method_domain = client.payment_method_domains.create(
            hostname="pending.shinetime.example",
            account_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.payment_method_domains.with_raw_response.create(
            hostname="pending.shinetime.example",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method_domain = response.parse()
        assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.payment_method_domains.with_streaming_response.create(
            hostname="pending.shinetime.example",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method_domain = response.parse()
            assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        payment_method_domain = client.payment_method_domains.retrieve(
            "id",
        )
        assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.payment_method_domains.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method_domain = response.parse()
        assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.payment_method_domains.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method_domain = response.parse()
            assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payment_method_domains.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        payment_method_domain = client.payment_method_domains.list()
        assert_matches_type(SyncCursorPage[PaymentMethodDomain], payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        payment_method_domain = client.payment_method_domains.list(
            account_id="account_id",
            after="after",
            before="before",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            direction="asc",
            first=100,
            hostname="hostname",
            last=100,
            order="created_at",
            provider="apple",
            status="pending",
        )
        assert_matches_type(SyncCursorPage[PaymentMethodDomain], payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.payment_method_domains.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method_domain = response.parse()
        assert_matches_type(SyncCursorPage[PaymentMethodDomain], payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.payment_method_domains.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method_domain = response.parse()
            assert_matches_type(SyncCursorPage[PaymentMethodDomain], payment_method_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        payment_method_domain = client.payment_method_domains.delete(
            "id",
        )
        assert_matches_type(PaymentMethodDomainDeleteResponse, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.payment_method_domains.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method_domain = response.parse()
        assert_matches_type(PaymentMethodDomainDeleteResponse, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.payment_method_domains.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method_domain = response.parse()
            assert_matches_type(PaymentMethodDomainDeleteResponse, payment_method_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payment_method_domains.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify(self, client: Whop) -> None:
        payment_method_domain = client.payment_method_domains.verify(
            "id",
        )
        assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify(self, client: Whop) -> None:
        response = client.payment_method_domains.with_raw_response.verify(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method_domain = response.parse()
        assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify(self, client: Whop) -> None:
        with client.payment_method_domains.with_streaming_response.verify(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method_domain = response.parse()
            assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_verify(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payment_method_domains.with_raw_response.verify(
                "",
            )


class TestAsyncPaymentMethodDomains:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        payment_method_domain = await async_client.payment_method_domains.create(
            hostname="pending.shinetime.example",
        )
        assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        payment_method_domain = await async_client.payment_method_domains.create(
            hostname="pending.shinetime.example",
            account_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.payment_method_domains.with_raw_response.create(
            hostname="pending.shinetime.example",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method_domain = await response.parse()
        assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.payment_method_domains.with_streaming_response.create(
            hostname="pending.shinetime.example",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method_domain = await response.parse()
            assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        payment_method_domain = await async_client.payment_method_domains.retrieve(
            "id",
        )
        assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.payment_method_domains.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method_domain = await response.parse()
        assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.payment_method_domains.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method_domain = await response.parse()
            assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payment_method_domains.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        payment_method_domain = await async_client.payment_method_domains.list()
        assert_matches_type(AsyncCursorPage[PaymentMethodDomain], payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        payment_method_domain = await async_client.payment_method_domains.list(
            account_id="account_id",
            after="after",
            before="before",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            direction="asc",
            first=100,
            hostname="hostname",
            last=100,
            order="created_at",
            provider="apple",
            status="pending",
        )
        assert_matches_type(AsyncCursorPage[PaymentMethodDomain], payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.payment_method_domains.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method_domain = await response.parse()
        assert_matches_type(AsyncCursorPage[PaymentMethodDomain], payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.payment_method_domains.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method_domain = await response.parse()
            assert_matches_type(AsyncCursorPage[PaymentMethodDomain], payment_method_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        payment_method_domain = await async_client.payment_method_domains.delete(
            "id",
        )
        assert_matches_type(PaymentMethodDomainDeleteResponse, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.payment_method_domains.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method_domain = await response.parse()
        assert_matches_type(PaymentMethodDomainDeleteResponse, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.payment_method_domains.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method_domain = await response.parse()
            assert_matches_type(PaymentMethodDomainDeleteResponse, payment_method_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payment_method_domains.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify(self, async_client: AsyncWhop) -> None:
        payment_method_domain = await async_client.payment_method_domains.verify(
            "id",
        )
        assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncWhop) -> None:
        response = await async_client.payment_method_domains.with_raw_response.verify(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method_domain = await response.parse()
        assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncWhop) -> None:
        async with async_client.payment_method_domains.with_streaming_response.verify(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method_domain = await response.parse()
            assert_matches_type(PaymentMethodDomain, payment_method_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_verify(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payment_method_domains.with_raw_response.verify(
                "",
            )
