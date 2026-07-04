#!/usr/bin/env bash
set -e

cd /opt/ai-enterprise-os/core/kernel

source .venv/bin/activate

exec uvicorn kernel.app:app \
    --host 0.0.0.0 \
    --port 9100
