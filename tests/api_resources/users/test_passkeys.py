# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.users import (
    Passkey,
    PasskeyDeleteResponse,
    PasskeyChallengeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPasskeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        passkey = client.users.passkeys.create(
            attestation_object="YXR0ZXN0YXRpb24",
            client_data_json="Y2xpZW50LWRhdGE",
            credential_id="bmV3LWNyZWRlbnRpYWw",
            nickname="Work laptop",
        )
        assert_matches_type(Passkey, passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.users.passkeys.with_raw_response.create(
            attestation_object="YXR0ZXN0YXRpb24",
            client_data_json="Y2xpZW50LWRhdGE",
            credential_id="bmV3LWNyZWRlbnRpYWw",
            nickname="Work laptop",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passkey = response.parse()
        assert_matches_type(Passkey, passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.users.passkeys.with_streaming_response.create(
            attestation_object="YXR0ZXN0YXRpb24",
            client_data_json="Y2xpZW50LWRhdGE",
            credential_id="bmV3LWNyZWRlbnRpYWw",
            nickname="Work laptop",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passkey = response.parse()
            assert_matches_type(Passkey, passkey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        passkey = client.users.passkeys.list()
        assert_matches_type(SyncCursorPage[Passkey], passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        passkey = client.users.passkeys.list(
            after="after",
            before="before",
            direction="asc",
            first=0,
            last=0,
            order="created_at",
        )
        assert_matches_type(SyncCursorPage[Passkey], passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.users.passkeys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passkey = response.parse()
        assert_matches_type(SyncCursorPage[Passkey], passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.users.passkeys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passkey = response.parse()
            assert_matches_type(SyncCursorPage[Passkey], passkey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        passkey = client.users.passkeys.delete(
            id="id",
            authenticator_data="YXV0aGVudGljYXRvci1kYXRh",
            client_data_json="Y2xpZW50LWRhdGE",
            signature="c2lnbmF0dXJl",
        )
        assert_matches_type(PasskeyDeleteResponse, passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.users.passkeys.with_raw_response.delete(
            id="id",
            authenticator_data="YXV0aGVudGljYXRvci1kYXRh",
            client_data_json="Y2xpZW50LWRhdGE",
            signature="c2lnbmF0dXJl",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passkey = response.parse()
        assert_matches_type(PasskeyDeleteResponse, passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.users.passkeys.with_streaming_response.delete(
            id="id",
            authenticator_data="YXV0aGVudGljYXRvci1kYXRh",
            client_data_json="Y2xpZW50LWRhdGE",
            signature="c2lnbmF0dXJl",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passkey = response.parse()
            assert_matches_type(PasskeyDeleteResponse, passkey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.passkeys.with_raw_response.delete(
                id="",
                authenticator_data="YXV0aGVudGljYXRvci1kYXRh",
                client_data_json="Y2xpZW50LWRhdGE",
                signature="c2lnbmF0dXJl",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_challenge(self, client: Whop) -> None:
        passkey = client.users.passkeys.challenge(
            challenge_type="registration",
        )
        assert_matches_type(PasskeyChallengeResponse, passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_challenge_with_all_params(self, client: Whop) -> None:
        passkey = client.users.passkeys.challenge(
            challenge_type="registration",
            passkey_id="wcred_xxxxxxxxxxxxxx",
        )
        assert_matches_type(PasskeyChallengeResponse, passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_challenge(self, client: Whop) -> None:
        response = client.users.passkeys.with_raw_response.challenge(
            challenge_type="registration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passkey = response.parse()
        assert_matches_type(PasskeyChallengeResponse, passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_challenge(self, client: Whop) -> None:
        with client.users.passkeys.with_streaming_response.challenge(
            challenge_type="registration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passkey = response.parse()
            assert_matches_type(PasskeyChallengeResponse, passkey, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPasskeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        passkey = await async_client.users.passkeys.create(
            attestation_object="YXR0ZXN0YXRpb24",
            client_data_json="Y2xpZW50LWRhdGE",
            credential_id="bmV3LWNyZWRlbnRpYWw",
            nickname="Work laptop",
        )
        assert_matches_type(Passkey, passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.users.passkeys.with_raw_response.create(
            attestation_object="YXR0ZXN0YXRpb24",
            client_data_json="Y2xpZW50LWRhdGE",
            credential_id="bmV3LWNyZWRlbnRpYWw",
            nickname="Work laptop",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passkey = await response.parse()
        assert_matches_type(Passkey, passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.users.passkeys.with_streaming_response.create(
            attestation_object="YXR0ZXN0YXRpb24",
            client_data_json="Y2xpZW50LWRhdGE",
            credential_id="bmV3LWNyZWRlbnRpYWw",
            nickname="Work laptop",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passkey = await response.parse()
            assert_matches_type(Passkey, passkey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        passkey = await async_client.users.passkeys.list()
        assert_matches_type(AsyncCursorPage[Passkey], passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        passkey = await async_client.users.passkeys.list(
            after="after",
            before="before",
            direction="asc",
            first=0,
            last=0,
            order="created_at",
        )
        assert_matches_type(AsyncCursorPage[Passkey], passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.users.passkeys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passkey = await response.parse()
        assert_matches_type(AsyncCursorPage[Passkey], passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.users.passkeys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passkey = await response.parse()
            assert_matches_type(AsyncCursorPage[Passkey], passkey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        passkey = await async_client.users.passkeys.delete(
            id="id",
            authenticator_data="YXV0aGVudGljYXRvci1kYXRh",
            client_data_json="Y2xpZW50LWRhdGE",
            signature="c2lnbmF0dXJl",
        )
        assert_matches_type(PasskeyDeleteResponse, passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.users.passkeys.with_raw_response.delete(
            id="id",
            authenticator_data="YXV0aGVudGljYXRvci1kYXRh",
            client_data_json="Y2xpZW50LWRhdGE",
            signature="c2lnbmF0dXJl",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passkey = await response.parse()
        assert_matches_type(PasskeyDeleteResponse, passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.users.passkeys.with_streaming_response.delete(
            id="id",
            authenticator_data="YXV0aGVudGljYXRvci1kYXRh",
            client_data_json="Y2xpZW50LWRhdGE",
            signature="c2lnbmF0dXJl",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passkey = await response.parse()
            assert_matches_type(PasskeyDeleteResponse, passkey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.passkeys.with_raw_response.delete(
                id="",
                authenticator_data="YXV0aGVudGljYXRvci1kYXRh",
                client_data_json="Y2xpZW50LWRhdGE",
                signature="c2lnbmF0dXJl",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_challenge(self, async_client: AsyncWhop) -> None:
        passkey = await async_client.users.passkeys.challenge(
            challenge_type="registration",
        )
        assert_matches_type(PasskeyChallengeResponse, passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_challenge_with_all_params(self, async_client: AsyncWhop) -> None:
        passkey = await async_client.users.passkeys.challenge(
            challenge_type="registration",
            passkey_id="wcred_xxxxxxxxxxxxxx",
        )
        assert_matches_type(PasskeyChallengeResponse, passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_challenge(self, async_client: AsyncWhop) -> None:
        response = await async_client.users.passkeys.with_raw_response.challenge(
            challenge_type="registration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passkey = await response.parse()
        assert_matches_type(PasskeyChallengeResponse, passkey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_challenge(self, async_client: AsyncWhop) -> None:
        async with async_client.users.passkeys.with_streaming_response.challenge(
            challenge_type="registration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passkey = await response.parse()
            assert_matches_type(PasskeyChallengeResponse, passkey, path=["response"])

        assert cast(Any, response.is_closed) is True
