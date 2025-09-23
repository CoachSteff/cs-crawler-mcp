#!/usr/bin/env python3
"""
Basic Usage Examples for CS Crawler MCP
This script demonstrates how to use the MCP server tools programmatically.
"""

import asyncio
import json
import sys
import os

# Add the parent directory to the path so we can import the server
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import crawl_url, get_page_metadata

async def example_single_crawl():
    """Example: Crawl a single URL"""
    print("🌐 Example 1: Single URL Crawling")
    print("=" * 50)
    
    result = await crawl_url({
        "url": "https://httpbin.org/html",
        "output_format": "markdown"
    })
    
    if result and len(result) > 0:
        content = result[0].text
        print(f"✅ Successfully crawled URL")
        print(f"📄 Content length: {len(content)} characters")
        print(f"📝 First 200 characters: {content[:200]}...")
    else:
        print("❌ Failed to crawl URL")
    
    print()

async def example_metadata_extraction():
    """Example: Extract page metadata"""
    print("📊 Example 2: Metadata Extraction")
    print("=" * 50)
    
    result = await get_page_metadata({
        "url": "https://httpbin.org/html"
    })
    
    if result and len(result) > 0:
        metadata = json.loads(result[0].text)
        print("✅ Successfully extracted metadata:")
        print(f"   📍 URL: {metadata.get('url', 'N/A')}")
        print(f"   📝 Title: {metadata.get('title', 'N/A')}")
        print(f"   📄 Word count: {metadata.get('word_count', 'N/A')}")
        print(f"   🔗 Links count: {metadata.get('links_count', 'N/A')}")
        print(f"   🖼️  Media count: {metadata.get('media_count', 'N/A')}")
        print(f"   📊 Status code: {metadata.get('status_code', 'N/A')}")
    else:
        print("❌ Failed to extract metadata")
    
    print()

async def example_json_output():
    """Example: Get JSON output format"""
    print("📋 Example 3: JSON Output Format")
    print("=" * 50)
    
    result = await crawl_url({
        "url": "https://httpbin.org/json",
        "output_format": "json"
    })
    
    if result and len(result) > 0:
        data = json.loads(result[0].text)
        print("✅ Successfully crawled with JSON output:")
        print(f"   📍 URL: {data.get('url', 'N/A')}")
        print(f"   📝 Title: {data.get('title', 'N/A')}")
        print(f"   📄 Markdown length: {len(data.get('markdown', ''))} characters")
        print(f"   🏷️  Metadata keys: {list(data.get('metadata', {}).keys())}")
    else:
        print("❌ Failed to crawl with JSON output")
    
    print()

async def example_error_handling():
    """Example: Error handling"""
    print("⚠️  Example 4: Error Handling")
    print("=" * 50)
    
    # Try to crawl an invalid URL
    result = await crawl_url({
        "url": "https://this-domain-does-not-exist-12345.com",
        "output_format": "markdown"
    })
    
    if result and len(result) > 0:
        content = result[0].text
        if "Error" in content:
            print("✅ Error handling working correctly:")
            print(f"   ⚠️  Error message: {content}")
        else:
            print("❌ Expected error but got success")
    else:
        print("❌ No result returned")
    
    print()

async def main():
    """Run all examples"""
    print("🚀 CS Crawler MCP - Basic Usage Examples")
    print("=" * 60)
    print()
    
    try:
        await example_single_crawl()
        await example_metadata_extraction()
        await example_json_output()
        await example_error_handling()
        
        print("🎉 All examples completed!")
        print()
        print("💡 Next steps:")
        print("   1. Try the examples with different URLs")
        print("   2. Experiment with different output formats")
        print("   3. Use the tools in Claude Desktop or other MCP clients")
        print("   4. Check out the advanced examples in the examples/ directory")
        
    except Exception as e:
        print(f"❌ Error running examples: {e}")
        print("💡 Make sure the server is properly installed and configured")

if __name__ == "__main__":
    asyncio.run(main())
