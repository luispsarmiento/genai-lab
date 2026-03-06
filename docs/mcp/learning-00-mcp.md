# Learning 00-MCP

## Summary of what was done

In this section we explored Anthropic's **Model Context Protocol (MCP)** framework, which allows creating servers that expose tools, resources, and prompts to LLM clients.

### 00-mcp-hello-world

Basic first example demonstrating the fundamental structure of an MCP server:

- **server.py**: Creates a `FastMCP` server with:
  - An `add` tool that adds two numbers
  - A dynamic resource `greeting://{name}` that returns personalized greetings

- **client.py**: Client that connects to the server using `StdioServerParameters` and demonstrates:
  - Listing available resources
  - Listing available tools
  - Reading resources
  - Invoking tools

### 02-mcp-server-example

More complete example implementing:

- An HTTP server (`streamable-http`) called `calculatormcp`
- A `get_weather` tool that returns simulated weather information
- Configuration in `.aitk/mcp.json` for connecting with aitoolkit

## VS Code Configuration

**Important**: In VS Code, MCP servers can be configured **globally** using the official **AIToolkit** plugin. This allows any client or extension that supports MCP to use the configured servers without per-project configuration.

Global configuration is typically found in: `datauser/.aitk/mcp.json`

## Requirements for Running MCP Servers

**Important**: Whether the MCP server is local or hosted in the cloud, **it must be running** for the client to connect and use its tools. This means:

1. **Local servers**: Must be started manually (e.g., `python server.py` or via npm/node)
2. **Cloud servers**: Must be deployed and active
3. **AIToolkit configuration**: The servers must be configured and running to appear available in the plugin

## MCP Inspector Tool

We can use the **MCP Inspector** tool from npx to review the list of tools offered by MCP servers. This is useful for:

- Verifying which tools are available
- Testing tools manually
- Debugging connection with the server

```bash
npx @modelcontextprotocol/inspector
```

When running the inspector, it will connect to the configured MCP server and display all available tools, resources, and prompts, allowing you to test them directly from the inspector interface.

## Key Concepts

- **FastMCP**: Simplified framework for creating MCP servers in Python
- **Tools**: Functions that the LLM can invoke
- **Resources**: Data that the LLM can read
- **Prompts**: Predefined prompt templates
- **StdioServerParameters**: For local servers that communicate via stdio
- **Streamable HTTP**: For HTTP servers that allow persistent connections
