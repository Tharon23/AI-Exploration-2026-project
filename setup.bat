@echo off
setlocal enabledelayedexpansion

echo ========================================================
echo  AI Exploration 2026 - Automated Setup (Kalab / Bartek / Kamil)
echo ========================================================
echo.

:: 1. Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found in PATH! Install Python 3.11+.
    pause
    exit /b 1
)

:: 2. Create virtual environment if missing
if not exist ".venv" (
    echo [*] Creating virtual environment in .venv...
    python -m venv .venv
)

:: 3. Install dependencies
echo [*] Installing dependencies...
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt >nul 2>&1
pip install ruff black pytest >nul 2>&1

:: 4. Copy .env if not exists
if not exist ".env" (
    echo [*] Creating .env from .env.example...
    copy .env.example .env >nul
    echo [!] Remember to edit .env and set your CONTRIBUTOR_NAME!
)

:: 5. Install Git Hooks
echo [*] Installing Git pre-commit hooks...
powershell -ExecutionPolicy Bypass -File scripts\setup-hooks.ps1 >nul 2>&1

:: 6. Check MEX Drift
echo [*] Verifying .mex architecture memory...
call npx promexeus check

echo.
echo ========================================================
echo  Setup complete! Virtual environment active in .venv.
echo  Run: call .venv\Scripts\activate.bat to start working.
echo ========================================================
