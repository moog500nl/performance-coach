@echo off
setlocal enabledelayedexpansion

echo ===================================================
echo            Local Performance Coach Sync            
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

:: Run Intervals.icu Sync
echo [1/2] Syncing training data from Intervals.icu...
python sync.py --output latest.json
if %errorlevel% neq 0 (
    echo [warning] Intervals.icu sync failed or completed with warnings.
) else (
    echo [ok] Intervals.icu sync completed.
)
echo.

:: Run Cronometer Sync
echo [2/2] Syncing nutrition data from Cronometer CSVs...
python sync_cronometer.py
if %errorlevel% neq 0 (
    echo [warning] Cronometer nutrition sync failed.
) else (
    echo [ok] Cronometer nutrition sync completed.
)
echo.

:end
echo ===================================================
echo Sync process finished.
echo ===================================================
pause
