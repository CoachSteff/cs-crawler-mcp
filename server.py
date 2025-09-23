#!/usr/bin/env python3
"""
CS Crawler MCP
A Model Context Protocol server that provides web crawling functionality via Crawl4AI.
"""

import asyncio
import json
import logging
import os
import sys
from contextlib import contextmanager
from typing import Any, Dict, List, Optional, Sequence
from urllib.parse import urlparse

# Redirect stdout/stderr to suppress Crawl4AI progress messages
class StdoutRedirect:
    def __init__(self):
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr
        self.devnull = open(os.devnull, 'w')
    
    def __enter__(self):
        sys.stdout = self.devnull
        sys.stderr = self.devnull
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if sys.stdout != self.original_stdout:
            sys.stdout.close()
        if sys.stderr != self.original_stderr:
            sys.stderr.close()
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr

# Configure logging to file only
log_file = os.path.join(os.path.dirname(__file__), "crawl4ai-mcp.log")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler(log_file)]
)
logger = logging.getLogger(__name__)

# Global crawler instance
crawler = None

async def get_crawler(config: Dict[str, Any] = None):
    """Get or create a crawler instance"""
    # Import Crawl4AI when needed
    try:
        from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
    except ImportError as e:
        logger.error(f"Failed to import crawl4ai: {e}")
        raise RuntimeError("Crawl4AI is not installed. Please install it with: pip install crawl4ai")
    
    global crawler
    if crawler is None:
        try:
            with StdoutRedirect():  # Suppress crawler initialization output
                browser_config = BrowserConfig(
                    headless=config.get("headless", True) if config else True,
                    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    viewport={"width": 1920, "height": 1080},
                    extra_args=["--disable-dev-shm-usage", "--no-sandbox"]
                )
                crawler = AsyncWebCrawler(config=browser_config)
                # Warm up the crawler if the method exists
                if hasattr(crawler, 'awarmup'):
                    await crawler.awarmup()
                logger.info("Crawler instance created successfully")
        except Exception as e:
            logger.error(f"Failed to create crawler: {e}")
            raise
    return crawler

async def cleanup():
    """Cleanup crawler instance"""
    global crawler
    if crawler:
        try:
            await crawler.close()
            logger.info("Crawler instance closed")
        except Exception as e:
            logger.error(f"Error closing crawler: {e}")
        finally:
            crawler = None

async def crawl_url_handler(arguments: Dict[str, Any]):
    """Handle crawl_url tool calls"""
    try:
        url = arguments.get("url")
        if not url:
            return [{"type": "text", "text": "Error: URL is required"}]
        
        # Validate URL
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            return [{"type": "text", "text": f"Error: Invalid URL format: {url}"}]
        
        output_format = arguments.get("output_format", "markdown")
        if output_format not in ["markdown", "html", "text", "json"]:
            return [{"type": "text", "text": f"Error: Invalid output format: {output_format}"}]
        
        # Get crawler instance
        crawler_instance = await get_crawler()
        
        # Suppress all Crawl4AI output during crawling
        with StdoutRedirect():
            result = await crawler_instance.arun(url=url)
        
        if not result.success:
            error_msg = f"Failed to crawl {url}: {result.error_message if hasattr(result, 'error_message') else 'Unknown error'}"
            logger.error(error_msg)
            return [{"type": "text", "text": error_msg}]
        
        # Format output based on requested format
        if output_format == "markdown":
            content = result.markdown if hasattr(result, 'markdown') and result.markdown else result.cleaned_html
        elif output_format == "html":
            content = result.cleaned_html if hasattr(result, 'cleaned_html') else result.html
        elif output_format == "text":
            content = result.cleaned_html if hasattr(result, 'cleaned_html') else result.html
        elif output_format == "json":
            content = json.dumps({
                "url": url,
                "title": getattr(result, 'title', ''),
                "content": result.markdown if hasattr(result, 'markdown') and result.markdown else result.cleaned_html,
                "metadata": {
                    "status_code": getattr(result, 'status_code', 200),
                    "word_count": len((result.markdown or result.cleaned_html or '').split()),
                    "links_count": len(getattr(result, 'links', [])),
                    "media_count": len(getattr(result, 'media', []))
                }
            }, indent=2)
        
        logger.info(f"Successfully crawled {url} with {output_format} format")
        return [{"type": "text", "text": content}]
        
    except Exception as e:
        error_msg = f"Exception while crawling {url}: {str(e)}"
        logger.error(error_msg)
        return [{"type": "text", "text": error_msg}]

async def get_metadata_handler(arguments: Dict[str, Any]):
    """Handle get_metadata tool calls"""
    try:
        url = arguments.get("url")
        if not url:
            return [{"type": "text", "text": "Error: URL is required"}]
        
        # Validate URL
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            return [{"type": "text", "text": f"Error: Invalid URL format: {url}"}]
        
        # Get crawler instance
        crawler_instance = await get_crawler()
        
        # Suppress all Crawl4AI output during crawling
        with StdoutRedirect():
            result = await crawler_instance.arun(url=url)
        
        if not result.success:
            error_msg = f"Failed to crawl {url}: {result.error_message if hasattr(result, 'error_message') else 'Unknown error'}"
            logger.error(error_msg)
            return [{"type": "text", "text": error_msg}]
        
        # Extract metadata
        metadata = {
            "url": url,
            "title": getattr(result, 'title', ''),
            "word_count": len((result.markdown or result.cleaned_html or '').split()),
            "links_count": len(getattr(result, 'links', [])),
            "media_count": len(getattr(result, 'media', [])),
            "status_code": getattr(result, 'status_code', 200),
            "language": getattr(result, 'language', '')
        }
        
        logger.info(f"Successfully extracted metadata for {url}")
        return [{"type": "text", "text": json.dumps(metadata, indent=2)}]
        
    except Exception as e:
        error_msg = f"Exception while getting metadata for {url}: {str(e)}"
        logger.error(error_msg)
        return [{"type": "text", "text": error_msg}]

async def main():
    """Main function"""
    # Import MCP when needed
    try:
        from mcp.server import Server
        from mcp.server.stdio import stdio_server
        from mcp.types import (
            CallToolResult,
            ListToolsResult,
            TextContent,
            Tool,
        )
    except ImportError as e:
        logger.error(f"Failed to import MCP: {e}")
        raise RuntimeError("MCP is not installed. Please install it with: pip install mcp")
    
    logger.info("Starting CS Crawler MCP")
    
    # Create MCP server
    server = Server("cs-crawler-mcp")
    
    # Register tools
    @server.list_tools()
    async def list_tools() -> ListToolsResult:
        return ListToolsResult(
            tools=[
                Tool(
                    name="crawl_url",
                    description="Crawl a single URL and extract content in your preferred format",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "url": {
                                "type": "string",
                                "description": "The URL to crawl"
                            },
                            "output_format": {
                                "type": "string",
                                "enum": ["markdown", "html", "text", "json"],
                                "description": "Output format (default: markdown)"
                            }
                        },
                        "required": ["url"]
                    }
                ),
                Tool(
                    name="get_metadata",
                    description="Get metadata about a URL without downloading the full content",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "url": {
                                "type": "string",
                                "description": "The URL to get metadata for"
                            }
                        },
                        "required": ["url"]
                    }
                )
            ]
        )
    
    @server.call_tool()
    async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
        if name == "crawl_url":
            result = await crawl_url_handler(arguments)
            return [TextContent(type="text", text=result[0]["text"])]
        elif name == "get_metadata":
            result = await get_metadata_handler(arguments)
            return [TextContent(type="text", text=result[0]["text"])]
        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]
    
    try:
        options = server.create_initialization_options()
        async with stdio_server() as (read_stream, write_stream):
            logger.info("MCP server started successfully")
            await server.run(read_stream, write_stream, options, raise_exceptions=True)
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise
    finally:
        await cleanup()
        logger.info("Server cleanup completed")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Server interrupted by user")
    except Exception as e:
        logger.error(f"Server failed to start: {e}")
        sys.exit(1)