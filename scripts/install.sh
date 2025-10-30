#!/bin/bash

# CS Crawler MCP Installation Script
# This script helps you set up the MCP server for Claude Desktop and other MCP clients

set -e

echo "🚀 CS Crawler MCP Installation"
echo "=================================="

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "📁 Project directory: $PROJECT_DIR"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Check if virtual environment exists
VENV_PATH=""
if [ -d "$HOME/venv-crawl4ai" ]; then
    VENV_PATH="$HOME/venv-crawl4ai"
    echo "✅ Found existing virtual environment: $VENV_PATH"
elif [ -d "$PROJECT_DIR/venv" ]; then
    VENV_PATH="$PROJECT_DIR/venv"
    echo "✅ Found project virtual environment: $VENV_PATH"
else
    echo "⚠️  No virtual environment found. Proceeding with system Python."
    echo "   Tip: Create one with: python3 -m venv ~/venv-crawl4ai && source ~/venv-crawl4ai/bin/activate"
fi

# Find Python executable
if [ -n "$VENV_PATH" ] && [ -f "$VENV_PATH/bin/python" ]; then
    PYTHON_PATH="$VENV_PATH/bin/python"
    SITE_PACKAGES="$VENV_PATH/lib/python3.*/site-packages"
    SITE_PACKAGES=$(echo $SITE_PACKAGES | head -1)  # Take the first match
    echo "✅ Using Python from virtual environment: $PYTHON_PATH"
else
    PYTHON_PATH=$(which python3)
    SITE_PACKAGES=""
    echo "⚠️  Using system Python: $PYTHON_PATH"
    echo "   Note: Make sure crawl4ai and mcp are installed"
fi

# Test if crawl4ai is available
echo "🧪 Testing Crawl4AI availability..."
if $PYTHON_PATH -c "import crawl4ai; print('Crawl4AI version:', crawl4ai.__version__)" 2>/dev/null; then
    echo "✅ Crawl4AI is available"
else
    echo "❌ Crawl4AI is not available in $PYTHON_PATH"
    echo "   Please install it with: pip install crawl4ai"
    exit 1
fi

# Test if mcp is available
echo "🧪 Testing MCP availability..."
if $PYTHON_PATH -c "import mcp; print('MCP available')" 2>/dev/null; then
    echo "✅ MCP is available"
else
    echo "❌ MCP is not available in $PYTHON_PATH"
    echo "   Please install it with: pip install mcp"
    exit 1
fi

# Generate configuration
echo "📝 Generating configuration..."

# Determine the config file location based on OS
if [[ "$OSTYPE" == "darwin"* ]]; then
    CONFIG_DIR="$HOME/Library/Application Support/Claude"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    CONFIG_DIR="$HOME/.config/claude"
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    CONFIG_DIR="$APPDATA/Claude"
else
    CONFIG_DIR="$HOME/.config/claude"
fi

CONFIG_FILE="$CONFIG_DIR/config.json"

echo "📁 Config directory: $CONFIG_DIR"
echo "📄 Config file: $CONFIG_FILE"

# Create config directory if it doesn't exist
mkdir -p "$CONFIG_DIR"

# Create or update config.json
if [ -f "$CONFIG_FILE" ]; then
    echo "⚠️  Config file already exists. Creating backup..."
    cp "$CONFIG_FILE" "$CONFIG_FILE.backup.$(date +%Y%m%d_%H%M%S)"
fi

# Generate the configuration
cat > "$CONFIG_FILE" << EOF
{
  "mcpServers": {
    "cs-crawler": {
      "command": "$PROJECT_DIR/cs-crawler-mcp",
      "args": [],
      "env": {}
    }
  }
}
EOF

# Create wrapper config
cat > "$PROJECT_DIR/config.json" << EOF
{
  "python_path": "$PYTHON_PATH",
  "server_path": "$PROJECT_DIR/server.py",
  "env": {
    "PYTHONPATH": "$SITE_PACKAGES"
  }
}
EOF

echo "✅ Configuration written to $CONFIG_FILE"
echo "✅ Wrapper configuration written to $PROJECT_DIR/config.json"

echo ""
echo "🎉 Installation complete!"
echo ""
echo "📋 Next steps:"
echo "1. Restart Claude Desktop (or your MCP client)"
echo "2. Test the connection by asking Claude to crawl a website"
echo "3. Example: 'Can you crawl https://httpbin.org/html and show me the content?'"
echo ""
echo "🔧 Configuration details:"
echo "   Python: $PYTHON_PATH"
echo "   Server: $PROJECT_DIR/server.py"
echo "   PYTHONPATH: $SITE_PACKAGES"
echo ""
echo "📚 For more information, see README.md"
echo ""
echo "🧪 To test the installation, run:"
echo "   python3 tests/test_wrapper.py"