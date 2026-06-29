#!/usr/bin/env bash
# Idempotent environment setup for SGML Sales.
# Installs the package with dev extras so `pytest` and `ruff` are available.
set -euo pipefail

cd "$(dirname "$0")/.."

python -m pip install --quiet --upgrade pip
python -m pip install --quiet -e ".[dev]"

echo "SGML Sales environment ready: run 'pytest' and 'ruff check .'"
