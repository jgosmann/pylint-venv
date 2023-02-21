#!/bin/bash

set -o errexit -o nounset -o pipefail -o xtrace

WORKDIR=$(dirname "$0")
PYLINT_CMD=$(which pylint)
VENV_DIR=$(mktemp -d)

python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"
"$PYLINT_CMD" --rcfile "$WORKDIR/pylintrc" "$WORKDIR/empty.py" 2>&1 | tee "$VENV_DIR/pylint.log" | grep "^Using venv: $VENV_DIR\$"
rm -r "$VENV_DIR"
