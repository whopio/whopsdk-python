#!/usr/bin/env bash
# Packages a whopsdk-python release: the build job of .github/workflows/publish-main.yml runs it with
# VERSION, and the pypi job publishes the dist/ it leaves.
set -euo pipefail
cd "$(dirname "$0")/.."

python -m pip install --disable-pip-version-check --quiet build twine
python -m build --sdist --wheel --outdir dist .

python -m twine check --strict dist/*

python -m venv /tmp/smoke
/tmp/smoke/bin/pip install --disable-pip-version-check --quiet dist/*.whl
/tmp/smoke/bin/python - "$VERSION" <<'PY'
import sys
from importlib import metadata

from whop_sdk import AsyncWhop, Whop

expected = sys.argv[1]
installed = metadata.version("whop-sdk")
if installed != expected:
    sys.exit(f"wheel reports {installed}, expected {expected}")

Whop(token="smoke-test")
AsyncWhop(token="smoke-test")
print(f"whop-sdk {installed} imports and constructs")
PY
