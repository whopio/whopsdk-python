#!/usr/bin/env bash
# whopsdk-python's CI, with Poetry: .github/workflows/ci.yml runs it, and so does whop-monorepo's SDK
# pipeline over every build it delivers.
set -euo pipefail
cd "$(dirname "$0")/.."

poetry install
poetry run mypy .
poetry run pytest -rP -n auto .

poetry install --extras "aiohttp user-tokens"
poetry run pytest -rP -n auto -m aiohttp .
poetry run pytest -rP tests/custom/test_verify_user_token_extra.py

# The user-tokens extra's floor is tested: its tests run again on the oldest PyJWT pyproject.toml allows.
floor="$(sed -n 's/^pyjwt = { version = ">=\([0-9.]*\),.*/\1/p' pyproject.toml)"
poetry run pip install --quiet "pyjwt[crypto]==${floor}"
poetry run pytest -rP tests/custom/test_verify_user_token_extra.py
