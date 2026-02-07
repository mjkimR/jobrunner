@echo off
REM JobRunner Docker - Start Script (Windows)
REM Usage: start.bat [--build]

cd /d "%~dp0"

if "%1"=="--build" (
    echo Building and starting JobRunner...
    docker compose -p jobrunner up -d --build
) else (
    echo Starting JobRunner...
    docker compose -p jobrunner up -d
)

echo.
echo JobRunner started!
echo Dagster UI: http://localhost:3000
echo.
pause
