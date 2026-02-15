#!/bin/bash
# JobRunner Docker - Start Script (macOS/Linux)
# Usage: ./start.sh [--build]

cd "$(dirname "$0")"

if [ "$1" == "--build" ]; then
    echo "Building and starting JobRunner..."
    docker compose -p jobrunner up -d --build
else
    echo "Starting JobRunner..."
    docker compose -p jobrunner up -d
fi

echo ""
echo "JobRunner started!"
echo "Prefect UI: http://localhost:4200"
