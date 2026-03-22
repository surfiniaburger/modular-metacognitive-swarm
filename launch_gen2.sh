#!/bin/bash
# launch_gen2.sh

echo "🚀 Launching Gen-2 Modular Swarm Infrastructure..."

# 1. Start the Hub (Background)
echo "📡 Starting Observability Hub (Port 8000)..."
PYTHONPATH=. uv run hub/app.py > hub.log 2>&1 &
HUB_PID=$!

# 2. Start the Executor (Background)
echo "🐚 Starting Research Executor (MCP)..."
PYTHONPATH=. uv run executor/mcp_server.py > executor.log 2>&1 &
EXEC_PID=$!

# 3. Give them a moment to boot
sleep 5

# 4. Run the Mediator
echo "🤖 Starting Research Mediator (Main Loop)..."
PYTHONPATH=. uv run main.py

# Cleanup on exit
echo "🧹 Cleaning up infrastructure..."
kill $HUB_PID $EXEC_PID > /dev/null 2>&1
echo "✅ Swarm Retired."
