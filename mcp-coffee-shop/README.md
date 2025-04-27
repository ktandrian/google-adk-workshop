# Coffee Shop MCP Server

A simple MCP server that simulates a coffee shop, providing information about coffee beans, menu items, and friendly barista greetings.

## Available Tools

- **greeting**
  - A simple tool that returns a greeting from Barista
  - Arguments:
    - `greeting` (string, required): the greeting to return

- **list-coffee-bean**
  - Returns a list of sample coffee beans
  - No arguments required

- **list-menu**
  - Returns a sample coffee shop menu with prices
  - No arguments required

## Installation

### Using uv

```bash
uv run mcp-hello-world
```

## Configuration

### Configure for Cline

```json
{
  "mcpServers": {
    "mcp-coffee-shop": {
      "timeout": 60,
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/Users/weiyih/work/github/agentic-softwares/google-adk-workshop/mcp-hello-world",
        "mcp-hello-world"
      ],
      "transportType": "stdio",
      "disabled": false,
      "autoApprove": [
        "list-coffee-bean",
        "list-menu"
      ]
    }
  }
}
```

## Debugging

You can use the MCP inspector to debug the server. For uvx installations:

```
docker run --rm -p 5173:5173 -p 3000:3000 -v /var/run/docker.sock:/var/run/docker.sock --pull=always mcp/inspector
```
