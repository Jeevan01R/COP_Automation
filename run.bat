@echo off
echo =========================================================
echo   ISCFIT PLATFORM REPORTING COCKPIT
echo   Professional Enterprise Dashboard
echo =========================================================
echo.

cd /d "%~dp0"

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://python.org
    pause
    exit /b 1
)

echo Installing/Updating requirements...
python -m pip install -r requirements.txt --quiet

if errorlevel 1 (
    echo.
    echo WARNING: Some packages might not have installed correctly
    echo Continuing anyway...
    echo.
)

echo.
echo ========================================
echo   Starting ISCFIT Platform Dashboard
echo ========================================
echo.
echo Dashboard will open in your default browser
echo URL: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

python -m streamlit run main.py --server.headless true --server.enableCORS false --server.enableXsrfProtection false

pause