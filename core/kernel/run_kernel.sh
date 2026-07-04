#!/usr/bin/env bash
set -e
cd /opt/ai-enterprise-os/core/kernel
python3 -m venv .venv
source .venv/bin/activate
pip install -q --upgrade pip
pip install -q -r requirements.txt
uvicorn kernel.app:app --host 0.0.0.0 --port 9100
