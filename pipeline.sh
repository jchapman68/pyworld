#!/bin/bash

set -euo pipefail

: SECRETS

BRANCH=$(git rev-parse --abbrev-ref HEAD)

fly -t tutorial set-pipeline -p  pwpipe \
    -v branch="$BRANCH" \
    -c pipeline.yml \
    -l params.yml \
    -l $SECRETS

echo "updated"