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

## Configuration

### Configure test client

Update the python folder in `test_agent.py`.

```python

async def get_tools_async():
    print("Attempting to connect to MCP Coffee Shop server...")

    tools, exit_stack = await MCPToolset.from_server(
        # Use StdioServerParameters for local process communication
        connection_params=StdioServerParameters(
            command="python",  # Command to run the server
            args=[
                "[GIT_ROOT]/mcp-coffee-shop/src/mcp_coffee_shop/"
            ],
        )
    )
    print("MCP Toolset created successfully.")
```

Debug with inspector.

```bash
npx @modelcontextprotocol/inspector uv run mcp-coffee-shop
```

### Configure for Cline

You need to update `GITREPO_ROOT`.

```json
{
  "mcpServers": {
    "mcp-coffee-shop": {
      "timeout": 60,
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "[GITREPO_ROOT]/mcp-coffee-shop",
        "mcp-coffee-shop"
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

