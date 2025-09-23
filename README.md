# CS Crawler MCP

[![CI/CD Pipeline](https://github.com/CoachSteff/cs-crawler-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/CoachSteff/cs-crawler-mcp/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A **Model Context Protocol (MCP) server** that provides powerful web crawling functionality via the `crawl4ai` library. This server allows you to use `crawl4ai`'s advanced web crawling capabilities directly within MCP-enabled applications like **Claude Desktop**, **Cursor**, and other MCP clients.

## ✨ Features

- 🌐 **Web Crawling**: Crawl any publicly accessible URL and extract clean, structured content
- 📄 **Multiple Output Formats**: Get content as Markdown, HTML, plain text, or structured JSON
- 📊 **Metadata Extraction**: Extract page metadata including title, description, links, and SEO information
- 🔧 **MCP Integration**: Seamlessly integrates with any MCP-enabled application
- 🚀 **Easy Deployment**: Simple Python installation and setup
- ⚡ **Async Performance**: Built with Python asyncio for optimal performance
- 🛡️ **Error Handling**: Robust error handling and logging
- 🔒 **Security**: Respects robots.txt and includes rate limiting

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** (3.9+ recommended)
- **Crawl4AI** (automatically installed as dependency)
- **Playwright browsers** (automatically installed during setup)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/CoachSteff/cs-crawler-mcp.git
   cd cs-crawler-mcp
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers**
   ```bash
   python -m playwright install chromium
   ```

4. **Test the installation**
   ```bash
   python3 tests/test_wrapper.py
   ```

## 🔧 MCP Client Integration

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

**Configuration locations:**
- **macOS**: `~/Library/Application Support/Claude/config.json`
- **Linux**: `~/.config/claude/config.json`
- **Windows**: `%APPDATA%\Claude\config.json`

### Other MCP Clients

Use the wrapper script as your MCP server command:
- **Command**: `/path/to/cs-crawler-mcp/cs-crawler-mcp`
- **Args**: `[]`
- **Env**: `{}`

## 🛠️ Available Tools

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

## 📋 Example Outputs

### Markdown Output
```markdown
# Example Page Title

This is the main content of the page...

## Section 1
Content here...

### Subsection
More content...
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
    "language": "en",
    "author": "Page Author",
    "keywords": "example, test, page"
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

## 🎯 Use Cases

### News and Content Analysis
- **News Article Summary**: Extract and summarize news articles
- **Blog Post Analysis**: Analyze blog posts for key points and insights
- **Content Comparison**: Compare coverage across multiple sources

### E-commerce and Product Research
- **Product Comparison**: Extract product information for comparison
- **Price Monitoring**: Track product prices and discounts
- **Review Analysis**: Analyze customer reviews and ratings

### Documentation and Learning
- **Documentation Deep Dive**: Extract comprehensive documentation
- **API Documentation**: Create reference guides from API docs
- **Technical Blog Series**: Summarize technical blog series

### Data Extraction and Analysis
- **Financial Data**: Extract financial tables and reports
- **Research Data**: Get research data and methodology
- **Statistical Information**: Extract statistics and data points

### SEO and Website Analysis
- **SEO Audit**: Analyze SEO elements and structure
- **Competitor Analysis**: Compare competitor websites
- **Content Audit**: Analyze content topics and engagement

## 🚀 Advanced Usage

### Running Examples

Try the included examples to see the server in action:

```bash
# Run basic usage examples
python3 examples/basic_usage.py

# Run advanced examples
python3 examples/advanced_usage.py
```

### Programmatic Usage

```python
import asyncio
from server import crawl_url, get_page_metadata

async def main():
    # Crawl a URL
    result = await crawl_url({
        "url": "https://example.com",
        "output_format": "markdown"
    })
    
    # Get metadata
    metadata = await get_page_metadata({
        "url": "https://example.com"
    })

asyncio.run(main())
```

### Server Deployment

For production deployment:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python server.py
```

### Configuration Options

The server can be configured through the `config.json` file:

```json
{
  "python_path": "/usr/bin/python3",
  "server_path": "/path/to/server.py",
  "headless": true,
  "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
  "viewport": {
    "width": 1920,
    "height": 1080
  },
  "timeout": 30,
  "max_retries": 3
}
```

## 🔍 Troubleshooting

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

4. **MCP client not connecting**
   - Verify config.json file location and format
   - Check file permissions
   - Restart MCP client completely
   - Check logs for error messages

### Logs

Check the log file for debugging information:
```bash
tail -f cs-crawler-mcp.log
```

### Diagnostic Commands

```bash
# Check system dependencies
python3 --version
pip --version
git --version

# Check virtual environment
ls ~/venv-crawl4ai/
source ~/venv-crawl4ai/bin/activate
pip list | grep -E "(crawl4ai|mcp)"

# Check MCP configuration
cat ~/Library/Application\ Support/Claude/config.json  # macOS
cat ~/.config/claude/config.json  # Linux
```

## 🧪 Development

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

### Development Dependencies

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

## 📚 Documentation

- **[Installation Guide](docs/DEPLOYMENT.md)** - Comprehensive installation and deployment guide
- **[Claude Desktop Examples](examples/claude_desktop_examples.md)** - Practical usage examples
- **[Changelog](docs/CHANGELOG.md)** - Version history and updates
- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute to the project

## 🤝 Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[Crawl4AI](https://github.com/unclecode/crawl4ai)** - The powerful web crawling library that powers this MCP server
- **[Model Context Protocol](https://modelcontextprotocol.io/)** - The protocol that enables seamless integration with AI applications
- **Claude Desktop** - For providing an excellent MCP client experience

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/CoachSteff/cs-crawler-mcp/issues)
- **Discussions**: [GitHub Discussions](https://github.com/CoachSteff/cs-crawler-mcp/discussions)
- **Documentation**: [Wiki](https://github.com/CoachSteff/cs-crawler-mcp/wiki)

---

**Happy Crawling! 🚀**

*Built with ❤️ by [@CoachSteff](https://github.com/CoachSteff)*

<!-- Last updated: $(date) -->