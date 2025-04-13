# Simple Arithmetic MCP Server

A simple arithmetic MCP server that integrates with Claude for Desktop, providing basic calculation functions.

## Overview

This repository provides code and configuration for an arithmetic server using the Model Context Protocol (MCP). The server adds addition, subtraction, multiplication, and division capabilities to Claude for Desktop through the MCP integration.

## Requirements

- Python 3.12 or higher
- uv package manager
- Claude for Desktop

## Setup Instructions

### 1. Install uv Package Manager

```powershell
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Project Setup

```bash
# Initialize project
uv init .

# Create virtual environment
uv venv

# Activate virtual environment (Windows)
.venv\Scripts\activate

# Install required packages
uv add "mcp[cli]"
```

### 3. Claude for Desktop Integration

Add the following content to the Claude for Desktop configuration file (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "calculator": {
      "command": "uv",
      "args": [
        "--directory",
        "absolute path to this repository",
        "run",
        "calculator.py"
      ]
    }
  }
}
```

## Usage

1. Start Claude for Desktop
2. Click the tools icon (hammer) in the bottom left to verify the registered tools
3. Request calculations in your prompt (e.g., "What is 5 + 3? Calculate using MCP")

## Implemented Functions

- `add`: Addition
- `subtract`: Subtraction
- `multiply`: Multiplication
- `divide`: Division

## Further Information

For more details, please refer to the following article:

- [Creating a Simple Arithmetic MCP Server and Using it with Claude for Desktop](https://qiita.com/enumura1/items/9b372f71f2af1bd22f22) (in Japanese)
