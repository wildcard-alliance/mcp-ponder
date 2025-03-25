#!/bin/bash

# Activate the virtual environment and run the server
cd "$(dirname "$0")" || exit 1
source .venv/bin/activate

# Install the mcp package if it's not already installed
if ! pip show mcp > /dev/null 2>&1; then
  echo "Installing MCP package..."
  pip install mcp>=1.2.0
fi

# Install this package in development mode
if ! pip show mcp-ponder-tool > /dev/null 2>&1; then
  echo "Installing MCP Ponder Tool in development mode..."
  pip install -e .
fi

# Run the ponder server
python src/ponder_tool/server.py