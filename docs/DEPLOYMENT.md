# 🚀 Deployment Guide

This guide covers all deployment options for the CS Crawler MCP.

## 📋 Prerequisites

- Python 3.8 or higher
- Git
- Internet connection
- 2GB+ free disk space

## 🎯 Deployment Options

### Option 1: Automatic Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/CoachSteff/cs-crawler-mcp.git
cd cs-crawler-mcp

# Run the installation script
./install.sh
```

**What it does:**
- ✅ Checks system dependencies
- ✅ Creates Python virtual environment
- ✅ Installs Crawl4AI and MCP dependencies
- ✅ Configures MCP client (Claude Desktop, etc.)
- ✅ Runs tests to verify installation

### Option 2: Manual Installation

```bash
# 1. Create virtual environment
python3 -m venv ~/venv-crawl4ai
source ~/venv-crawl4ai/bin/activate

# 2. Install dependencies
pip install crawl4ai mcp

# 3. Install Playwright browsers
python -m playwright install chromium

# 4. Configure MCP client (see Configuration section)
```

### Option 3: Docker Installation

```bash
# Build and run with Docker Compose
docker-compose up -d

# Or build manually
docker build -t cs-crawler-mcp .
docker run -it cs-crawler-mcp
```

### Option 4: Package Installation (Future)

```bash
# Install from PyPI (when published)
pip install cs-crawler-mcp

# Or install from source
pip install git+https://github.com/CoachSteff/ccs-crawler-mcp.git
```

## ⚙️ Configuration

### Claude Desktop Configuration

**macOS:** `~/Library/Application Support/Claude/config.json`
**Linux:** `~/.config/claude/config.json`
**Windows:** `%APPDATA%/Claude/config.json`

```json
{
  "mcpServers": {
    "cs-crawler": {
      "command": "/path/to/your/venv-crawl4ai/bin/python",
      "args": ["/path/to/cs-crawler-mcp/server.py"],
      "env": {
        "PYTHONPATH": "/path/to/your/venv-crawl4ai/lib/python3.x/site-packages"
      }
    }
  }
}
```

### Other MCP Clients

For Cursor, VS Code, or other MCP clients:

```json
{
  "mcpServers": {
    "cs-crawler": {
      "command": "./cs-crawler-mcp",
      "args": [],
      "env": {}
    }
  }
}
```

### Environment Variables

```bash
export CRAWL4AI_PYTHON_PATH="/custom/path/to/python"
export CRAWL4AI_SERVER_PATH="/custom/path/to/server.py"
export CRAWL4AI_DEBUG=true
```

## 🐳 Docker Deployment

### Basic Docker Run

```bash
# Build the image
docker build -t cs-crawler-mcp .

# Run the server
docker run -it cs-crawler-mcp
```

### Docker Compose

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f cs-crawler-mcp

# Stop services
docker-compose down
```

### Docker with Custom Configuration

```bash
# Mount custom config
docker run -v $(pwd)/config.json:/app/config.json:ro cs-crawler-mcp

# Set environment variables
docker run -e CRAWL4AI_DEBUG=true cs-crawler-mcp
```

### Docker Registry

```bash
# Pull from GitHub Container Registry
docker pull ghcr.io/coachsteff/cs-crawler-mcp:latest

# Run from registry
docker run -it ghcr.io/coachsteff/cs-crawler-mcp:latest
```

## 🔧 Platform-Specific Instructions

### macOS

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install python3 git

# Run installation
./install.sh
```

### Ubuntu/Debian

```bash
# Update package list
sudo apt update

# Install dependencies
sudo apt install python3 python3-pip python3-venv git curl

# Run installation
./install.sh
```

### CentOS/RHEL

```bash
# Install dependencies
sudo yum install python3 python3-pip git curl

# Run installation
./install.sh
```

### Windows (WSL)

```bash
# Install WSL2 and Ubuntu
# Then follow Ubuntu instructions above
```

### Windows (Native)

```powershell
# Install Python from https://python.org
# Install Git from https://git-scm.com
# Run in PowerShell:
python -m venv venv-crawl4ai
venv-crawl4ai\Scripts\activate
pip install crawl4ai mcp
python -m playwright install chromium
```

## 🧪 Testing Deployment

### Test Installation

```bash
# Run comprehensive tests
python test_client.py

# Test with examples
python examples/basic_usage.py

# Test specific functionality
python -c "
import asyncio
from server import crawl_url
async def test():
    result = await crawl_url({'url': 'https://httpbin.org/html'})
    print('Test passed!' if result else 'Test failed!')
asyncio.run(test())
"
```

### Test with Claude Desktop

1. Restart Claude Desktop after configuration
2. Start a new conversation
3. Try: "Please crawl https://httpbin.org/html and show me the content"

### Test Docker Deployment

```bash
# Test Docker image
docker run --rm cs-crawler-mcp python -c "import crawl4ai, mcp; print('Docker test passed')"

# Test with actual crawling
docker run --rm cs-crawler-mcp python -c "
import asyncio
from server import crawl_url
async def test():
    result = await crawl_url({'url': 'https://httpbin.org/html'})
    print('Docker crawl test passed!' if result else 'Docker crawl test failed!')
asyncio.run(test())
"
```

## 🔍 Troubleshooting

### Common Issues

**1. "Module not found" errors**
```bash
# Check virtual environment
source ~/venv-crawl4ai/bin/activate
python -c "import crawl4ai; print('OK')"

# Reinstall if needed
pip install --upgrade crawl4ai mcp
```

**2. "Permission denied" errors**
```bash
# Make scripts executable
chmod +x install.sh
chmod +x cs-crawler-mcp
chmod +x start-server.sh
```

**3. "Browser not found" errors**
```bash
# Install Playwright browsers
source ~/venv-crawl4ai/bin/activate
python -m playwright install chromium
```

**4. "Docker build failed"**
```bash
# Check Docker is running
docker --version

# Clean Docker cache
docker system prune -a
```

**5. "MCP client not connecting"**
- Verify config.json file location and format
- Check file permissions
- Restart MCP client completely
- Check logs for error messages

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

# Check Docker
docker --version
docker-compose --version

# Check MCP configuration
cat ~/Library/Application\ Support/Claude/config.json  # macOS
cat ~/.config/claude/config.json  # Linux
```

## 📊 Performance Optimization

### System Requirements

**Minimum:**
- 2GB RAM
- 1GB free disk space
- Python 3.8+
- Internet connection

**Recommended:**
- 4GB+ RAM
- 2GB+ free disk space
- Python 3.11+
- Fast internet connection

### Performance Tuning

```bash
# Increase memory limits
export CRAWL4AI_MEMORY_LIMIT=4G

# Enable caching
export CRAWL4AI_CACHE_ENABLED=true

# Set concurrency limits
export CRAWL4AI_MAX_CONCURRENT=5
```

### Docker Performance

```yaml
# docker-compose.yml
services:
  cs-crawler-mcp:
    deploy:
      resources:
        limits:
          memory: 4G
          cpus: '2.0'
        reservations:
          memory: 2G
          cpus: '1.0'
```

## 🔒 Security Considerations

### Local Deployment
- Server runs locally, no external data transmission
- No API keys required
- Uses standard browser user agents
- Respects robots.txt by default

### Docker Deployment
- Runs in isolated container
- Non-root user by default
- Minimal attack surface
- Regular security updates

### Network Security
- No external network access required
- Can run behind firewall
- Supports proxy configuration
- Rate limiting built-in

## 📈 Monitoring and Logging

### Log Files

```bash
# Server logs
tail -f ~/cs-crawler-mcp/server.log

# Docker logs
docker-compose logs -f cs-crawler-mcp

# System logs
journalctl -u cs-crawler-mcp  # systemd
```

### Health Checks

```bash
# Test server health
python test_client.py

# Docker health check
docker run --rm cs-crawler-mcp python -c "import crawl4ai, mcp; print('OK')"
```

## 🚀 Production Deployment

### Systemd Service (Linux)

```ini
# /etc/systemd/system/cs-crawler-mcp.service
[Unit]
Description=CS Crawler MCP
After=network.target

[Service]
Type=simple
User=crawl4ai
WorkingDirectory=/opt/cs-crawler-mcp
ExecStart=/opt/cs-crawler-mcp/cs-crawler-mcp
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### Docker Swarm

```yaml
# docker-stack.yml
version: '3.8'
services:
  cs-crawler-mcp:
    image: ghcr.io/coachsteff/cs-crawler-mcp:latest
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
      restart_policy:
        condition: on-failure
    networks:
      - mcp-network

networks:
  mcp-network:
    driver: overlay
```

## Support

- **Issues**: [GitHub Issues](https://github.com/CoachSteff/cs-crawler-mcp/issues)
- **Discussions**: [GitHub Discussions](https://github.com/CoachSteff/cs-crawler-mcp/discussions)
- **Documentation**: [Wiki](https://github.com/CoachSteff/cs-crawler-mcp/wiki)

---

**Happy Deploying! 🚀**
