# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    Card,
    CardDispute,
    CardCashback,
    CardDailySpend,
    CardListResponse,
    CardAccountBalance,
    CardDepositAddress,
    CardTransactionList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        card = client.cards.create(
            account_id="account_id",
        )
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        card = client.cards.create(
            account_id="account_id",
            name="name",
            spend_limit="spend_limit",
            spend_limit_frequency="daily",
            transaction_limit="transaction_limit",
        )
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.cards.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.cards.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        card = client.cards.retrieve(
            "id",
        )
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.cards.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.cards.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.cards.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        card = client.cards.update(
            id="id",
        )
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        card = client.cards.update(
            id="id",
            name="name",
            spend_limit="spend_limit",
            spend_limit_frequency="daily",
            transaction_limit="transaction_limit",
        )
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.cards.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.cards.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.cards.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        card = client.cards.list(
            account_id="account_id",
        )
        assert_matches_type(CardListResponse, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.cards.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardListResponse, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.cards.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardListResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_balance(self, client: Whop) -> None:
        card = client.cards.balance(
            "id",
        )
        assert_matches_type(CardAccountBalance, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_balance(self, client: Whop) -> None:
        response = client.cards.with_raw_response.balance(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardAccountBalance, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_balance(self, client: Whop) -> None:
        with client.cards.with_streaming_response.balance(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardAccountBalance, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_balance(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.cards.with_raw_response.balance(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_card_transactions(self, client: Whop) -> None:
        card = client.cards.card_transactions(
            id="id",
        )
        assert_matches_type(CardTransactionList, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_card_transactions_with_all_params(self, client: Whop) -> None:
        card = client.cards.card_transactions(
            id="id",
            created_after="created_after",
            created_before="created_before",
            page=0,
            per=0,
            status="pending",
        )
        assert_matches_type(CardTransactionList, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_card_transactions(self, client: Whop) -> None:
        response = client.cards.with_raw_response.card_transactions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardTransactionList, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_card_transactions(self, client: Whop) -> None:
        with client.cards.with_streaming_response.card_transactions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardTransactionList, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_card_transactions(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.cards.with_raw_response.card_transactions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cashback(self, client: Whop) -> None:
        card = client.cards.cashback(
            "id",
        )
        assert_matches_type(CardCashback, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cashback(self, client: Whop) -> None:
        response = client.cards.with_raw_response.cashback(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardCashback, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cashback(self, client: Whop) -> None:
        with client.cards.with_streaming_response.cashback(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardCashback, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cashback(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.cards.with_raw_response.cashback(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_dispute(self, client: Whop) -> None:
        card = client.cards.create_dispute(
            id="id",
            dispute_type="fraud",
            text_evidence="text_evidence",
            transaction_id="transaction_id",
        )
        assert_matches_type(CardDispute, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_dispute_with_all_params(self, client: Whop) -> None:
        card = client.cards.create_dispute(
            id="id",
            dispute_type="fraud",
            text_evidence="text_evidence",
            transaction_id="transaction_id",
            dispute_amount_cents=0,
        )
        assert_matches_type(CardDispute, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_dispute(self, client: Whop) -> None:
        response = client.cards.with_raw_response.create_dispute(
            id="id",
            dispute_type="fraud",
            text_evidence="text_evidence",
            transaction_id="transaction_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardDispute, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_dispute(self, client: Whop) -> None:
        with client.cards.with_streaming_response.create_dispute(
            id="id",
            dispute_type="fraud",
            text_evidence="text_evidence",
            transaction_id="transaction_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardDispute, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_dispute(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.cards.with_raw_response.create_dispute(
                id="",
                dispute_type="fraud",
                text_evidence="text_evidence",
                transaction_id="transaction_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_dispute_attachment(self, client: Whop) -> None:
        card = client.cards.create_dispute_attachment(
            dispute_id="dispute_id",
            id="id",
            attachment={},
        )
        assert_matches_type(CardDispute, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_dispute_attachment_with_all_params(self, client: Whop) -> None:
        card = client.cards.create_dispute_attachment(
            dispute_id="dispute_id",
            id="id",
            attachment={
                "id": "id",
                "direct_upload_id": "direct_upload_id",
            },
        )
        assert_matches_type(CardDispute, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_dispute_attachment(self, client: Whop) -> None:
        response = client.cards.with_raw_response.create_dispute_attachment(
            dispute_id="dispute_id",
            id="id",
            attachment={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardDispute, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_dispute_attachment(self, client: Whop) -> None:
        with client.cards.with_streaming_response.create_dispute_attachment(
            dispute_id="dispute_id",
            id="id",
            attachment={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardDispute, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_dispute_attachment(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.cards.with_raw_response.create_dispute_attachment(
                dispute_id="dispute_id",
                id="",
                attachment={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_id` but received ''"):
            client.cards.with_raw_response.create_dispute_attachment(
                dispute_id="",
                id="id",
                attachment={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_daily_spend(self, client: Whop) -> None:
        card = client.cards.daily_spend(
            id="id",
        )
        assert_matches_type(CardDailySpend, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_daily_spend_with_all_params(self, client: Whop) -> None:
        card = client.cards.daily_spend(
            id="id",
            timezone="timezone",
        )
        assert_matches_type(CardDailySpend, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_daily_spend(self, client: Whop) -> None:
        response = client.cards.with_raw_response.daily_spend(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardDailySpend, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_daily_spend(self, client: Whop) -> None:
        with client.cards.with_streaming_response.daily_spend(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardDailySpend, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_daily_spend(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.cards.with_raw_response.daily_spend(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deactivate(self, client: Whop) -> None:
        card = client.cards.deactivate(
            "id",
        )
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deactivate(self, client: Whop) -> None:
        response = client.cards.with_raw_response.deactivate(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deactivate(self, client: Whop) -> None:
        with client.cards.with_streaming_response.deactivate(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_deactivate(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.cards.with_raw_response.deactivate(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deposit_address(self, client: Whop) -> None:
        card = client.cards.deposit_address(
            "id",
        )
        assert_matches_type(CardDepositAddress, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deposit_address(self, client: Whop) -> None:
        response = client.cards.with_raw_response.deposit_address(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardDepositAddress, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deposit_address(self, client: Whop) -> None:
        with client.cards.with_streaming_response.deposit_address(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardDepositAddress, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_deposit_address(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.cards.with_raw_response.deposit_address(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_freeze(self, client: Whop) -> None:
        card = client.cards.freeze(
            "id",
        )
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_freeze(self, client: Whop) -> None:
        response = client.cards.with_raw_response.freeze(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_freeze(self, client: Whop) -> None:
        with client.cards.with_streaming_response.freeze(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_freeze(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.cards.with_raw_response.freeze(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_transactions(self, client: Whop) -> None:
        card = client.cards.transactions(
            account_id="account_id",
        )
        assert_matches_type(CardTransactionList, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_transactions_with_all_params(self, client: Whop) -> None:
        card = client.cards.transactions(
            account_id="account_id",
            card_id="card_id",
            created_after="created_after",
            created_before="created_before",
            page=0,
            per=0,
            status="pending",
        )
        assert_matches_type(CardTransactionList, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_transactions(self, client: Whop) -> None:
        response = client.cards.with_raw_response.transactions(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardTransactionList, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_transactions(self, client: Whop) -> None:
        with client.cards.with_streaming_response.transactions(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardTransactionList, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unfreeze(self, client: Whop) -> None:
        card = client.cards.unfreeze(
            "id",
        )
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unfreeze(self, client: Whop) -> None:
        response = client.cards.with_raw_response.unfreeze(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unfreeze(self, client: Whop) -> None:
        with client.cards.with_streaming_response.unfreeze(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unfreeze(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.cards.with_raw_response.unfreeze(
                "",
            )


class TestAsyncCards:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.create(
            account_id="account_id",
        )
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.create(
            account_id="account_id",
            name="name",
            spend_limit="spend_limit",
            spend_limit_frequency="daily",
            transaction_limit="transaction_limit",
        )
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.cards.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.cards.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.retrieve(
            "id",
        )
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.cards.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.cards.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.cards.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.update(
            id="id",
        )
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.update(
            id="id",
            name="name",
            spend_limit="spend_limit",
            spend_limit_frequency="daily",
            transaction_limit="transaction_limit",
        )
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.cards.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.cards.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.cards.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.list(
            account_id="account_id",
        )
        assert_matches_type(CardListResponse, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.cards.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardListResponse, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.cards.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardListResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_balance(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.balance(
            "id",
        )
        assert_matches_type(CardAccountBalance, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_balance(self, async_client: AsyncWhop) -> None:
        response = await async_client.cards.with_raw_response.balance(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardAccountBalance, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_balance(self, async_client: AsyncWhop) -> None:
        async with async_client.cards.with_streaming_response.balance(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardAccountBalance, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_balance(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.cards.with_raw_response.balance(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_card_transactions(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.card_transactions(
            id="id",
        )
        assert_matches_type(CardTransactionList, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_card_transactions_with_all_params(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.card_transactions(
            id="id",
            created_after="created_after",
            created_before="created_before",
            page=0,
            per=0,
            status="pending",
        )
        assert_matches_type(CardTransactionList, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_card_transactions(self, async_client: AsyncWhop) -> None:
        response = await async_client.cards.with_raw_response.card_transactions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardTransactionList, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_card_transactions(self, async_client: AsyncWhop) -> None:
        async with async_client.cards.with_streaming_response.card_transactions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardTransactionList, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_card_transactions(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.cards.with_raw_response.card_transactions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cashback(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.cashback(
            "id",
        )
        assert_matches_type(CardCashback, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cashback(self, async_client: AsyncWhop) -> None:
        response = await async_client.cards.with_raw_response.cashback(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardCashback, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cashback(self, async_client: AsyncWhop) -> None:
        async with async_client.cards.with_streaming_response.cashback(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardCashback, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cashback(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.cards.with_raw_response.cashback(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_dispute(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.create_dispute(
            id="id",
            dispute_type="fraud",
            text_evidence="text_evidence",
            transaction_id="transaction_id",
        )
        assert_matches_type(CardDispute, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_dispute_with_all_params(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.create_dispute(
            id="id",
            dispute_type="fraud",
            text_evidence="text_evidence",
            transaction_id="transaction_id",
            dispute_amount_cents=0,
        )
        assert_matches_type(CardDispute, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_dispute(self, async_client: AsyncWhop) -> None:
        response = await async_client.cards.with_raw_response.create_dispute(
            id="id",
            dispute_type="fraud",
            text_evidence="text_evidence",
            transaction_id="transaction_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardDispute, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_dispute(self, async_client: AsyncWhop) -> None:
        async with async_client.cards.with_streaming_response.create_dispute(
            id="id",
            dispute_type="fraud",
            text_evidence="text_evidence",
            transaction_id="transaction_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardDispute, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_dispute(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.cards.with_raw_response.create_dispute(
                id="",
                dispute_type="fraud",
                text_evidence="text_evidence",
                transaction_id="transaction_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_dispute_attachment(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.create_dispute_attachment(
            dispute_id="dispute_id",
            id="id",
            attachment={},
        )
        assert_matches_type(CardDispute, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_dispute_attachment_with_all_params(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.create_dispute_attachment(
            dispute_id="dispute_id",
            id="id",
            attachment={
                "id": "id",
                "direct_upload_id": "direct_upload_id",
            },
        )
        assert_matches_type(CardDispute, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_dispute_attachment(self, async_client: AsyncWhop) -> None:
        response = await async_client.cards.with_raw_response.create_dispute_attachment(
            dispute_id="dispute_id",
            id="id",
            attachment={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardDispute, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_dispute_attachment(self, async_client: AsyncWhop) -> None:
        async with async_client.cards.with_streaming_response.create_dispute_attachment(
            dispute_id="dispute_id",
            id="id",
            attachment={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardDispute, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_dispute_attachment(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.cards.with_raw_response.create_dispute_attachment(
                dispute_id="dispute_id",
                id="",
                attachment={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_id` but received ''"):
            await async_client.cards.with_raw_response.create_dispute_attachment(
                dispute_id="",
                id="id",
                attachment={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_daily_spend(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.daily_spend(
            id="id",
        )
        assert_matches_type(CardDailySpend, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_daily_spend_with_all_params(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.daily_spend(
            id="id",
            timezone="timezone",
        )
        assert_matches_type(CardDailySpend, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_daily_spend(self, async_client: AsyncWhop) -> None:
        response = await async_client.cards.with_raw_response.daily_spend(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardDailySpend, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_daily_spend(self, async_client: AsyncWhop) -> None:
        async with async_client.cards.with_streaming_response.daily_spend(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardDailySpend, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_daily_spend(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.cards.with_raw_response.daily_spend(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deactivate(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.deactivate(
            "id",
        )
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deactivate(self, async_client: AsyncWhop) -> None:
        response = await async_client.cards.with_raw_response.deactivate(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deactivate(self, async_client: AsyncWhop) -> None:
        async with async_client.cards.with_streaming_response.deactivate(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_deactivate(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.cards.with_raw_response.deactivate(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deposit_address(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.deposit_address(
            "id",
        )
        assert_matches_type(CardDepositAddress, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deposit_address(self, async_client: AsyncWhop) -> None:
        response = await async_client.cards.with_raw_response.deposit_address(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardDepositAddress, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deposit_address(self, async_client: AsyncWhop) -> None:
        async with async_client.cards.with_streaming_response.deposit_address(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardDepositAddress, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_deposit_address(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.cards.with_raw_response.deposit_address(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_freeze(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.freeze(
            "id",
        )
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_freeze(self, async_client: AsyncWhop) -> None:
        response = await async_client.cards.with_raw_response.freeze(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_freeze(self, async_client: AsyncWhop) -> None:
        async with async_client.cards.with_streaming_response.freeze(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_freeze(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.cards.with_raw_response.freeze(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_transactions(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.transactions(
            account_id="account_id",
        )
        assert_matches_type(CardTransactionList, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_transactions_with_all_params(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.transactions(
            account_id="account_id",
            card_id="card_id",
            created_after="created_after",
            created_before="created_before",
            page=0,
            per=0,
            status="pending",
        )
        assert_matches_type(CardTransactionList, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_transactions(self, async_client: AsyncWhop) -> None:
        response = await async_client.cards.with_raw_response.transactions(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardTransactionList, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_transactions(self, async_client: AsyncWhop) -> None:
        async with async_client.cards.with_streaming_response.transactions(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardTransactionList, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unfreeze(self, async_client: AsyncWhop) -> None:
        card = await async_client.cards.unfreeze(
            "id",
        )
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unfreeze(self, async_client: AsyncWhop) -> None:
        response = await async_client.cards.with_raw_response.unfreeze(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(Card, card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unfreeze(self, async_client: AsyncWhop) -> None:
        async with async_client.cards.with_streaming_response.unfreeze(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unfreeze(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.cards.with_raw_response.unfreeze(
                "",
            )
