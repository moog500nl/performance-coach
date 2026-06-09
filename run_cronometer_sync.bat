@echo off
setlocal enabledelayedexpansion

echo ===================================================
echo       Local Performance Coach Nutrition Sync       
echo ===================================================
echo.

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [error] Python was not found in your system PATH.
    echo Please install Python and try again.
    goto end
)

:: Run Cronometer Sync
echo Syncing nutrition data from Cronometer CSVs...
python sync_cronometer.py
if %errorlevel% neq 0 (
    echo [warning] Cronometer nutrition sync failed.
) else (
    echo [ok] Cronometer nutrition sync completed.
)
echo.

:end
echo ===================================================
echo Nutrition sync process finished.
echo ===================================================
pause
