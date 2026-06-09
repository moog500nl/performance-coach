@echo off
setlocal enabledelayedexpansion

echo ===================================================
echo        Local Performance Coach History Sync        
echo ===================================================
echo.

:: Check for requests library
python -c "import requests" 2>nul
if %errorlevel% neq 0 (
    echo [info] Installing required Python library: requests...
    pip install requests
    if !errorlevel! neq 0 (
        echo [error] Failed to install requests. Please run 'pip install requests' manually.
        goto end
    )
    echo [ok] requests library installed.
    echo.
)

:: Check if configuration exists
if not exist .sync_config.json (
    echo [warning] Configuration file .sync_config.json not found.
    echo [info] Running setup wizard...
    python sync.py --setup
    if !errorlevel! neq 0 (
        echo [error] Setup failed or was cancelled.
        goto end
    )
    echo.
)

:: Run Intervals.icu History Sync
echo Syncing long-term fitness history from Intervals.icu (up to 3 years)...
python sync.py --generate-history --output history.json
if %errorlevel% neq 0 (
    echo [warning] History generation failed.
) else (
    echo [ok] history.json updated successfully.
)
echo.

:end
echo ===================================================
echo History sync process finished.
echo ===================================================
pause
