# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of CS Crawler MCP by [@CoachSteff](https://github.com/CoachSteff)
- Support for single URL crawling with multiple output formats
- Metadata extraction from web pages
- Cross-platform Python support
- Comprehensive installation script for all platforms
- Extensive documentation and examples
- CI/CD pipeline with automated testing
- Support for Claude Desktop and other MCP clients

### Changed
- N/A

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

### Security
- N/A

## [1.0.0] - 2025-09-23

### Added
- 🌐 **Single URL Crawling** - Extract clean, structured content from any website
- 📊 **Multiple Output Formats** - Markdown, HTML, JSON, and plain text
- 📋 **Metadata Extraction** - Get page titles, descriptions, and SEO information
- 🚀 **Easy Deployment** - Simple Python installation and setup
- 🔧 **Flexible Configuration** - Customize for different environments
- 📚 **Comprehensive Documentation** - Complete usage guide and examples
- 🚀 **Easy Installation** - One-command setup for all platforms
- 🔄 **CI/CD Pipeline** - Automated testing and deployment
- 🛠️ **MCP Integration** - Works with Claude Desktop, Cursor, VS Code, and more

### Technical Details
- Built with Python 3.8+ support
- Uses Crawl4AI for advanced web crawling
- Implements Model Context Protocol (MCP) specification
- Supports Playwright for browser automation
- Includes comprehensive error handling and logging
- Provides both programmatic and CLI interfaces

### Installation Methods
- **Automatic Installation**: `./install.sh`
- **Manual Installation**: Virtual environment setup
- **Systemd Service**: Linux service installation
- **Package Installation**: `pip install cs-crawler-mcp`

### Supported Platforms
- macOS (Intel and Apple Silicon)
- Linux (Ubuntu, Debian, CentOS, RHEL)
- Windows (with WSL or native Python)

### MCP Client Support
- Claude Desktop
- Cursor
- VS Code (with MCP extension)
- Any MCP-compatible application

---

## Version History

### v1.0.0 (Initial Release)
- Complete MCP server implementation
- Single URL crawling with multiple output formats
- Metadata extraction capabilities
- Cross-platform compatibility
- Cross-platform installation scripts
- Comprehensive documentation
- Example usage scenarios
- CI/CD automation
- Security scanning integration

---

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on how to:

- Report bugs
- Suggest new features
- Submit pull requests
- Set up development environment

## Support

- **Issues**: [GitHub Issues](https://github.com/CoachSteff/cs-crawler-mcp/issues)
- **Discussions**: [GitHub Discussions](https://github.com/CoachSteff/cs-crawler-mcp/discussions)
- **Documentation**: [Wiki](https://github.com/CoachSteff/ccs-crawler-mcp/wiki)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
