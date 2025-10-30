# CS Crawler MCP

A Model Context Protocol (MCP) server that provides web crawling functionality via Crawl4AI.

## Quick Start

- Install: `pip install -r requirements.txt`
- Playwright: `python -m playwright install chromium`
- Local config:
  - Copy `config.json.template` to `config.json`
  - Set `python_path` and `server_path`
- Configure your MCP client to launch `cs-crawler-mcp`

## Tools

- `crawl_url` — Crawl a single URL and return markdown/html/text/json
- `get_metadata` — Extract page metadata without downloading full content

See `README.md` for full setup and usage.
