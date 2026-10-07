#!/usr/bin/env bash
# AI Exploration 2026 - Automated Setup for Linux / macOS
set -e

echo "========================================================"
echo " AI Exploration 2026 - Automated Setup (Kalab / Bartek / Kamil)"
echo "========================================================"
echo ""

# 1. Check Python
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] python3 not found! Please install Python 3.11+."
    exit 1
fi

# 2. Virtual Environment
if [ ! -d ".venv" ]; then
    echo "[*] Creating virtual environment in .venv..."
    python3 -m venv .venv
fi

# 3. Dependencies
echo "[*] Installing dependencies..."
source .venv/bin/activate
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt > /dev/null 2>&1
pip install ruff black pytest > /dev/null 2>&1

# 4. Environment config
if [ ! -f ".env" ]; then
    echo "[*] Creating .env from .env.example..."
    cp .env.example .env
    echo "[!] Remember to edit .env and set your CONTRIBUTOR_NAME!"
fi

# 5. Git Hooks
echo "[*] Installing Git pre-commit hooks..."
bash scripts/setup-hooks.sh

# 6. Check MEX
echo "[*] Verifying .mex architecture memory..."
npx promexeus check

echo ""
echo "========================================================"
echo " Setup complete! Run: source .venv/bin/activate to start."
echo "========================================================"
