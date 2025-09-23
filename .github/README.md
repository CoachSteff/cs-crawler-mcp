# CS Crawler MCP

A Model Context Protocol (MCP) server that provides web crawling functionality via the crawl4ai library.

## Features

- Web crawling with multiple output formats
- Metadata extraction
- MCP integration
- Easy deployment

## Quick Start

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Install Playwright: `python -m playwright install chromium`
4. Configure your MCP client

## Installation

```bash
git clone https://github.com/CoachSteff/cs-crawler-mcp.git
cd cs-crawler-mcp
pip install -r requirements.txt
python -m playwright install chromium
```

## Usage

Add to your Claude Desktop configuration:

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

## Available Tools

- `crawl_url` - Crawl a single URL
- `get_page_metadata` - Extract page metadata

## License

MIT License - see LICENSE file for details.
