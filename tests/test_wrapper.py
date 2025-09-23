#!/usr/bin/env python3
"""
Test script to verify the wrapper configuration
"""

import json
import os

def test_config():
    """Test if the config.json file is valid and paths exist"""
    
    print("🧪 Testing Wrapper Configuration")
    print("=" * 40)
    
    # Check if config.json exists
    config_path = "config.json"
    if not os.path.exists(config_path):
        print("❌ config.json not found")
        print("   Please run ./install.sh first")
        return False
    
    print("✅ config.json found")
    
    # Load and validate config
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        print("✅ config.json is valid JSON")
    except Exception as e:
        print(f"❌ Invalid config.json: {e}")
        return False
    
    # Check required fields
    required_fields = ["python_path", "server_path"]
    for field in required_fields:
        if field not in config:
            print(f"❌ Missing required field: {field}")
            return False
        print(f"✅ {field}: {config[field]}")
    
    # Check if paths exist
    python_path = config["python_path"]
    server_path = config["server_path"]
    
    if not os.path.exists(python_path):
        print(f"❌ Python path does not exist: {python_path}")
        return False
    print(f"✅ Python executable found: {python_path}")
    
    if not os.path.exists(server_path):
        print(f"❌ Server path does not exist: {server_path}")
        return False
    print(f"✅ Server file found: {server_path}")
    
    # Check wrapper script
    wrapper_path = "./cs-crawler-mcp"
    if not os.path.exists(wrapper_path):
        print(f"❌ Wrapper script not found: {wrapper_path}")
        return False
    print(f"✅ Wrapper script found: {wrapper_path}")
    
    return True

def main():
    """Main test function"""
    success = test_config()
    
    print("\n" + "=" * 40)
    if success:
        print("🎉 Configuration is valid!")
        print("\n📋 Your MCP client should use:")
        print('   "command": "/path/to/cs-crawler-mcp/cs-crawler-mcp"')
        print('   "args": []')
        print('   "env": {}')
    else:
        print("❌ Configuration has issues. Please check the errors above.")
    
    return 0 if success else 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
