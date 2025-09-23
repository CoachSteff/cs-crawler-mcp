#!/usr/bin/env python3
"""
CS Crawler MCP
A Model Context Protocol server that provides web crawling functionality via Crawl4AI.
"""

import asyncio
import json
import logging
import sys
import os
import contextlib
from io import StringIO
from typing import Any, Dict, List, Optional, Sequence
from urllib.parse import urlparse

# Redirect stdout/stderr to suppress Crawl4AI progress messages
class StdoutRedirect:
    def __init__(self):
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr
        
    def __enter__(self):
        # Redirect to devnull to suppress all output
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Restore original stdout/stderr
        if sys.stdout != self.original_stdout:
            sys.stdout.close()
        if sys.stderr != self.original_stderr:
            sys.stderr.close()
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr

# Import Crawl4AI with suppressed output
with StdoutRedirect():
    try:
        import crawl4ai
        from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
    except ImportError as e:
        # Restore stdout to show error
        print(f"Error: Failed to import crawl4ai: {e}", file=sys.__stderr__)
        print("Please install crawl4ai: pip install crawl4ai", file=sys.__stderr__)
        sys.exit(1)

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
    print(f"Error: Failed to import MCP: {e}", file=sys.__stderr__)
    print("Please install MCP: pip install mcp", file=sys.__stderr__)
    sys.exit(1)

# Configure logging to file only
log_file = os.path.join(os.path.dirname(__file__), "crawl4ai-mcp.log")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler(log_file)]
)
logger = logging.getLogger(__name__)

# Create MCP server
server = Server("cs-crawler-mcp")

# Global crawler instance
crawler = None

async def get_crawler(config: Dict[str, Any] = None) -> AsyncWebCrawler:
    """Get or create a crawler instance"""
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
            with StdoutRedirect():
                await crawler.aclose()
            logger.info("Crawler closed successfully")
        except Exception as e:
            logger.error(f"Error closing crawler: {e}")
        finally:
            crawler = None

@server.list_tools()
async def list_tools() -> List[Tool]:
    """List all available tools"""
    logger.info("Tools list requested")
    return [
        Tool(
            name="crawl_url",
            description="Crawl a single URL and extract content as clean Markdown",
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
                        "default": "markdown",
                        "description": "Output format for the content"
                    }
                },
                "required": ["url"]
            }
        ),
        Tool(
            name="get_page_metadata",
            description="Extract metadata from a webpage (title, description, etc.)",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "URL to get metadata from"
                    }
                },
                "required": ["url"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Handle tool calls"""
    logger.info(f"Tool called: {name} with args: {arguments}")
    try:
        if name == "crawl_url":
            return await crawl_url(arguments)
        elif name == "get_page_metadata":
            return await get_page_metadata(arguments)
        else:
            error_msg = f"Unknown tool: {name}"
            logger.error(error_msg)
            return [TextContent(type="text", text=error_msg)]
    except Exception as e:
        error_msg = f"Error executing tool {name}: {str(e)}"
        logger.error(error_msg)
        return [TextContent(type="text", text=error_msg)]

async def crawl_url(args: Dict[str, Any]) -> List[TextContent]:
    """Crawl a single URL"""
    url = args["url"]
    output_format = args.get("output_format", "markdown")
    
    logger.info(f"Crawling URL: {url} in format: {output_format}")

    try:
        crawler_instance = await get_crawler()
        
        # Suppress all Crawl4AI output during crawling
        with StdoutRedirect():
            run_config = CrawlerRunConfig(
                word_count_threshold=200,
                bypass_cache=False
            )

            result = await crawler_instance.arun(url=url, config=run_config)
        
        if result.success:
            content = ""
            if output_format == "markdown":
                content = result.markdown or "No markdown content available"
            elif output_format == "html":
                content = result.html or "No HTML content available"
            elif output_format == "text":
                content = result.cleaned_html or "No text content available"
            elif output_format == "json":
                content = json.dumps({
                    "url": url,
                    "title": result.metadata.get("title", "") if result.metadata else "",
                    "markdown": result.markdown or "",
                    "html": result.html or "",
                    "metadata": result.metadata or {}
                }, indent=2, ensure_ascii=False)

            logger.info(f"Successfully crawled {url}")
            return [TextContent(type="text", text=content)]
        else:
            error_msg = f"Error crawling {url}: {result.error_message}"
            logger.error(error_msg)
            return [TextContent(type="text", text=error_msg)]
            
    except Exception as e:
        error_msg = f"Exception while crawling {url}: {str(e)}"
        logger.error(error_msg)
        return [TextContent(type="text", text=error_msg)]

async def get_page_metadata(args: Dict[str, Any]) -> List[TextContent]:
    """Get metadata from a webpage"""
    url = args["url"]
    
    logger.info(f"Getting metadata for URL: {url}")

    try:
        crawler_instance = await get_crawler()
        
        # Suppress all Crawl4AI output during crawling
        with StdoutRedirect():
            run_config = CrawlerRunConfig(
                word_count_threshold=0  # We only want metadata
            )

            result = await crawler_instance.arun(url=url, config=run_config)
        
        if result.success:
            metadata = {
                "url": url,
                "title": result.metadata.get("title", "") if result.metadata else "",
                "description": result.metadata.get("description", "") if result.metadata else "",
                "keywords": result.metadata.get("keywords", "") if result.metadata else "",
                "language": result.metadata.get("language", "") if result.metadata else "",
                "author": result.metadata.get("author", "") if result.metadata else "",
                "links_count": len(result.links) if result.links else 0,
                "media_count": len(result.media) if result.media else 0,
                "word_count": len(result.markdown.split()) if result.markdown else 0,
                "status_code": getattr(result, 'status_code', None),
                "response_headers": getattr(result, 'response_headers', {})
            }
            
            logger.info(f"Successfully retrieved metadata for {url}")
            return [TextContent(type="text", text=json.dumps(metadata, indent=2, ensure_ascii=False))]
        else:
            error_msg = f"Error retrieving metadata from {url}: {result.error_message}"
            logger.error(error_msg)
            return [TextContent(type="text", text=error_msg)]
            
    except Exception as e:
        error_msg = f"Exception while getting metadata for {url}: {str(e)}"
        logger.error(error_msg)
        return [TextContent(type="text", text=error_msg)]

async def main():
    """Main function"""
    logger.info("Starting CS Crawler MCP")
    
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
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.__stderr__)
        sys.exit(1)
