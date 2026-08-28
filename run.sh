#!/bin/bash
# Script để chạy streamlit với PYTHONPATH được set đúng
# Dùng thay cho: uv run streamlit run src/langgraph_agent/app.py

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHONPATH="$SCRIPT_DIR/src" uv run streamlit run "$SCRIPT_DIR/src/langgraph_agent/app.py"
