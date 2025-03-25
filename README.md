# MCP Ponder Tool Server

A Model Context Protocol (MCP) server implementing the "ponder" tool for improving Claude's complex reasoning capabilities.

## Overview

This MCP server implements the "ponder" tool, inspired by Anthropic's "think" tool as described in their [blog post](https://www.anthropic.com/engineering/claude-think-tool), which provides Claude with a dedicated space for structured thinking during complex problem-solving tasks. The ponder tool has been shown to significantly improve performance in complex tasks requiring policy adherence and reasoning in long chains of tool calls.

## Features

- **Structured Thinking Space**: Provides Claude with a dedicated place to break down complex problems
- **Thought History**: Maintains a log of all ponderings with timestamps for reference
- **Statistics and Analysis**: Offers metadata about thinking patterns
- **Clean Slate Option**: Allows clearing pondering history when starting fresh

## Installation

Install from PyPI:

```bash
pip install mcp-ponder-tool
```

## Configuration

To use this tool with Claude, add the following configuration to your MCP config file:

```json
"ponder": {
    "command": "/home/xxx/.local/bin/mcp-ponder-tool",
    "args": [],
    "type": "stdio",
    "pollingInterval": 30000,
    "startupTimeout": 30000,
    "restartOnFailure": true
}
```

The `command` field should point to the directory where you installed the python package using pip.