@echo off
REM ============================================================
REM RamaBJP Windows Launcher
REM ============================================================

echo.
echo ============================================================
echo   RamaBJP - Predictive Maintenance for Defence Equipment
echo   Windows Launcher
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python 3.12 from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python detected
python --version
echo.

REM Check if virtual environment exists
if not exist ".venv\Scripts\activate.bat" (
    echo [INFO] Virtual environment not found. Creating...
    py -3.12 -m venv .venv
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment.
        pause
        exit /b 1
    )
    echo [OK] Virtual environment created
)

echo [INFO] Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install dependencies
echo [INFO] Installing dependencies...
pip install -r requirements.txt --quiet

REM Initialize database if not exists
if not exist "data\ramabjp.db" (
    echo [INFO] Initializing database...
    python -m database.db
    python -m database.seed
)

echo.
echo ============================================================
echo   Starting RamaBJP...
echo   Browser will open at http://localhost:8501
echo   Press Ctrl+C to stop.
echo ============================================================
echo.

streamlit run app.py

pause