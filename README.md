# CS Crawler MCP Server

A **Model Context Protocol (MCP) server** that provides web crawling functionality via the `crawl4ai` library. This server allows you to use `crawl4ai`'s powerful web crawling capabilities directly within MCP-enabled applications like **Claude Desktop** and other MCP clients.

## Features

- 🌐 **Web Crawling**: Crawl any publicly accessible URL and extract content
- 📄 **Multiple Output Formats**: Get content as Markdown, HTML, plain text, or structured JSON
- 📊 **Metadata Extraction**: Extract page metadata including title, description, links, and more
- 🔧 **MCP Integration**: Seamlessly integrates with any MCP-enabled application
- 🐳 **Flexible Deployment**: Run locally, on a VPS, or in a Docker container
- ⚡ **Async Performance**: Built with Python asyncio for optimal performance

## Prerequisites

- **Python 3.8+** (3.9+ recommended)
- **Crawl4AI** (automatically installed as dependency)
- **Playwright browsers** (automatically installed during setup)

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/CoachSteff/cs-crawler-mcp.git
cd cs-crawler-mcp
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Playwright browsers

```bash
python -m playwright install chromium
```

### 4. Configure for MCP client

Copy the configuration template and update paths:

```bash
cp config.json.template config.json
# Edit config.json with your Python and server paths
```

### 5. Test the installation

```bash
python3 tests/test_wrapper.py
```

## MCP Client Integration

### Claude Desktop

Add this to your Claude Desktop configuration (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "cs-crawler": {
      "command": "/path/to/cs-crawler-mcp/cs-crawler-mcp",
      "args": [],
      "env": {}
    }
  }
}
```

### Other MCP Clients

Use the wrapper script as your MCP server command:
- **Command**: `/path/to/cs-crawler-mcp/cs-crawler-mcp`
- **Args**: `[]`
- **Env**: `{}`

## Available Tools

### 1. `crawl_url`

Crawl a single URL and extract content in your preferred format.

**Parameters:**
- `url` (required): The URL to crawl
- `output_format` (optional): Output format - `markdown`, `html`, `text`, or `json` (default: `markdown`)

**Example Usage in Claude Desktop:**
```
Please crawl https://example.com and extract the content as markdown.
```

### 2. `get_page_metadata`

Extract metadata from a webpage without downloading the full content.

**Parameters:**
- `url` (required): The URL to get metadata from

**Example Usage in Claude Desktop:**
```
Get the metadata for https://example.com
```

## Example Outputs

### Markdown Output
```markdown
# Example Page Title

This is the main content of the page...

## Section 1
Content here...
```

### JSON Output
```json
{
  "url": "https://example.com",
  "title": "Example Page Title",
  "markdown": "# Example Page Title\n\nThis is the main content...",
  "html": "<html>...</html>",
  "metadata": {
    "title": "Example Page Title",
    "description": "Page description",
    "language": "en"
  }
}
```

### Metadata Output
```json
{
  "url": "https://example.com",
  "title": "Example Page Title",
  "description": "Page description",
  "keywords": "example, test, page",
  "language": "en",
  "author": "Page Author",
  "links_count": 15,
  "media_count": 3,
  "word_count": 250,
  "status_code": 200
}
```

## Advanced Usage

### Running Examples

Try the included examples to see the server in action:

```bash
# Run basic usage examples
python3 examples/basic_usage.py

# Run advanced examples
python3 examples/advanced_usage.py
```

### Docker Deployment

For containerized deployment:

```bash
# Build the Docker image
docker build -t cs-crawler-mcp .

# Run the container
docker run -p 3000:3000 cs-crawler-mcp
```

### Configuration Options

The server can be configured through the `config.json` file:

```json
{
  "python_path": "/usr/bin/python3",
  "server_path": "/path/to/server.py",
  "headless": true,
  "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}
```

## Troubleshooting

### Common Issues

1. **Playwright browser not found**
   ```bash
   python -m playwright install chromium
   ```

2. **Permission denied on wrapper script**
   ```bash
   chmod +x cs-crawler-mcp
   ```

3. **Import errors**
   ```bash
   pip install -r requirements.txt
   ```

### Logs

Check the log file for debugging information:
```bash
tail -f cs-crawler-mcp.log
```

## Development

### Running Tests

```bash
# Run configuration tests
python3 tests/test_wrapper.py

# Run server tests (if available)
pytest tests/
```

### Code Quality

The project uses several tools for code quality:

```bash
# Format code
black server.py

# Lint code
flake8 server.py

# Type checking
mypy server.py
```

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.