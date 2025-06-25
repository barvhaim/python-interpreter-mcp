# Python Interpreter MCP

A Model Context Protocol (MCP) server that provides Python code execution capabilities through a REST API interface.

## Overview

This MCP server exposes a single tool `execute_python_code` that allows AI assistants and other MCP clients to execute Python code remotely. The server acts as a bridge between MCP clients and a Python interpreter REST API service.

## Features

- Execute arbitrary Python code through MCP
- Returns complete execution results including stdout, stderr, exit codes, and file outputs
- Built with FastMCP for easy MCP server development
- Async HTTP client for reliable communication with the Python interpreter service

## Prerequisites

- Python 3.11 or higher
- A Python interpreter REST API service running on `localhost:50081` (such as [BeeAI Code Interpreter](https://github.com/i-am-bee/beeai-code-interpreter))

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd python-interpreter-mcp
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

## Usage

### Running the MCP Server

Start the MCP server:

```bash
python main.py
```

The server will start and expose the `execute_python_code` tool via the MCP protocol.

### Adding to Claude Desktop

Add this configuration to your Claude Desktop MCP settings:

```json
{
  "mcpServers": {
    "python-interpreter": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/python-interpreter-mcp",
        "run",
        "main.py"
      ]
    }
  }
}
```

Replace `/path/to/python-interpreter-mcp` with the actual path to your project directory.

### Tool: `execute_python_code`

Executes Python code using a remote interpreter service.

**Parameters:**
- `source_code` (string): The Python code to execute

**Returns:**
A dictionary containing:
- `stdout`: Standard output from the Python execution
- `stderr`: Standard error output (if any)
- `exit_code`: Exit code of the Python process
- `files`: Any files generated during execution

**Example usage:**
```python
# Through an MCP client
result = await execute_python_code("print('Hello, World!')")
# Returns: {"stdout": "Hello, World!\n", "stderr": "", "exit_code": 0, "files": {}}
```

## Configuration

The server is configured to connect to a Python interpreter REST API at:
- **URL**: `http://localhost:50081/v1/execute`
- **Method**: POST
- **Content-Type**: application/json

To use a different interpreter service, modify the URL in `main.py:23`.

## Error Handling

The server handles various error conditions:
- **Request errors**: Network connectivity issues
- **HTTP errors**: API service errors (4xx/5xx responses)
- **Timeout errors**: Long-running code execution

All errors are returned in the standard response format with appropriate error messages in the `stderr` field.

## Dependencies

- **fastmcp**: MCP server framework
- **httpx**: Async HTTP client for API communication

## License

MIT License