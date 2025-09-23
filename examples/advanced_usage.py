#!/usr/bin/env python3
"""
Advanced Usage Examples for CS Crawler MCP
This script demonstrates advanced features and use cases.
"""

import asyncio
import json
import sys
import os
from typing import List, Dict, Any

# Add the parent directory to the path so we can import the server
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import crawl_url, get_page_metadata

class Crawl4AIAdvanced:
    """Advanced Crawl4AI usage examples"""
    
    def __init__(self):
        self.results = []
    
    async def batch_crawl(self, urls: List[str], output_format: str = "markdown") -> List[Dict[str, Any]]:
        """Crawl multiple URLs in batch"""
        print(f"🔄 Batch crawling {len(urls)} URLs...")
        
        tasks = []
        for url in urls:
            task = crawl_url({
                "url": url,
                "output_format": output_format
            })
            tasks.append(task)
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        processed_results = []
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                processed_results.append({
                    "url": urls[i],
                    "success": False,
                    "error": str(result)
                })
            elif result and len(result) > 0:
                processed_results.append({
                    "url": urls[i],
                    "success": True,
                    "content": result[0].text,
                    "length": len(result[0].text)
                })
            else:
                processed_results.append({
                    "url": urls[i],
                    "success": False,
                    "error": "No content returned"
                })
        
        return processed_results
    
    async def analyze_content_quality(self, url: str) -> Dict[str, Any]:
        """Analyze the quality and structure of content from a URL"""
        print(f"🔍 Analyzing content quality for {url}")
        
        # Get both content and metadata
        content_result = await crawl_url({
            "url": url,
            "output_format": "markdown"
        })
        
        metadata_result = await get_page_metadata({
            "url": url
        })
        
        if not content_result or not metadata_result:
            return {"error": "Failed to fetch content or metadata"}
        
        content = content_result[0].text
        metadata = json.loads(metadata_result[0].text)
        
        # Analyze content structure
        lines = content.split('\n')
        headings = [line for line in lines if line.startswith('#')]
        links = [line for line in lines if '[' in line and '](' in line]
        lists = [line for line in lines if line.strip().startswith('-') or line.strip().startswith('*')]
        
        # Calculate readability metrics
        words = content.split()
        sentences = content.split('.')
        paragraphs = [p for p in content.split('\n\n') if p.strip()]
        
        analysis = {
            "url": url,
            "metadata": metadata,
            "content_analysis": {
                "total_words": len(words),
                "total_sentences": len(sentences),
                "total_paragraphs": len(paragraphs),
                "headings_count": len(headings),
                "links_count": len(links),
                "lists_count": len(lists),
                "average_words_per_sentence": len(words) / max(len(sentences), 1),
                "average_sentences_per_paragraph": len(sentences) / max(len(paragraphs), 1),
                "readability_score": self._calculate_readability(words, sentences)
            },
            "structure_quality": {
                "has_headings": len(headings) > 0,
                "has_links": len(links) > 0,
                "has_lists": len(lists) > 0,
                "heading_structure": self._analyze_heading_structure(headings)
            }
        }
        
        return analysis
    
    def _calculate_readability(self, words: List[str], sentences: List[str]) -> float:
        """Simple readability score calculation"""
        if not words or not sentences:
            return 0.0
        
        avg_words_per_sentence = len(words) / len(sentences)
        avg_syllables_per_word = sum(self._count_syllables(word) for word in words) / len(words)
        
        # Simplified Flesch Reading Ease formula
        score = 206.835 - (1.015 * avg_words_per_sentence) - (84.6 * avg_syllables_per_word)
        return max(0, min(100, score))
    
    def _count_syllables(self, word: str) -> int:
        """Count syllables in a word (approximation)"""
        word = word.lower()
        vowels = "aeiouy"
        syllable_count = 0
        prev_was_vowel = False
        
        for char in word:
            if char in vowels:
                if not prev_was_vowel:
                    syllable_count += 1
                prev_was_vowel = True
            else:
                prev_was_vowel = False
        
        # Handle silent 'e'
        if word.endswith('e') and syllable_count > 1:
            syllable_count -= 1
        
        return max(1, syllable_count)
    
    def _analyze_heading_structure(self, headings: List[str]) -> Dict[str, Any]:
        """Analyze heading structure and hierarchy"""
        if not headings:
            return {"valid": False, "reason": "No headings found"}
        
        levels = []
        for heading in headings:
            level = len(heading) - len(heading.lstrip('#'))
            levels.append(level)
        
        # Check for proper hierarchy
        valid_hierarchy = True
        for i in range(1, len(levels)):
            if levels[i] > levels[i-1] + 1:
                valid_hierarchy = False
                break
        
        return {
            "valid": valid_hierarchy,
            "levels": levels,
            "max_level": max(levels) if levels else 0,
            "min_level": min(levels) if levels else 0,
            "total_headings": len(headings)
        }
    
    async def content_comparison(self, urls: List[str]) -> Dict[str, Any]:
        """Compare content across multiple URLs"""
        print(f"📊 Comparing content across {len(urls)} URLs...")
        
        # Get content from all URLs
        results = await self.batch_crawl(urls, "markdown")
        
        # Analyze each URL
        analyses = []
        for result in results:
            if result["success"]:
                analysis = await self.analyze_content_quality(result["url"])
                analyses.append(analysis)
        
        # Compare metrics
        comparison = {
            "urls": [analysis["url"] for analysis in analyses],
            "word_counts": [analysis["content_analysis"]["total_words"] for analysis in analyses],
            "readability_scores": [analysis["content_analysis"]["readability_score"] for analysis in analyses],
            "heading_counts": [analysis["content_analysis"]["headings_count"] for analysis in analyses],
            "average_metrics": {
                "words": sum(analysis["content_analysis"]["total_words"] for analysis in analyses) / len(analyses),
                "readability": sum(analysis["content_analysis"]["readability_score"] for analysis in analyses) / len(analyses),
                "headings": sum(analysis["content_analysis"]["headings_count"] for analysis in analyses) / len(analyses)
            }
        }
        
        return comparison
    
    async def extract_structured_data(self, url: str, data_type: str) -> Dict[str, Any]:
        """Extract specific types of structured data from a URL"""
        print(f"🔍 Extracting {data_type} data from {url}")
        
        # Get content in JSON format for easier parsing
        result = await crawl_url({
            "url": url,
            "output_format": "json"
        })
        
        if not result or len(result) == 0:
            return {"error": "Failed to fetch content"}
        
        data = json.loads(result[0].text)
        content = data.get("markdown", "")
        metadata = data.get("metadata", {})
        
        # Extract different types of data
        if data_type == "contact_info":
            return self._extract_contact_info(content, metadata)
        elif data_type == "product_info":
            return self._extract_product_info(content, metadata)
        elif data_type == "article_info":
            return self._extract_article_info(content, metadata)
        else:
            return {"error": f"Unknown data type: {data_type}"}
    
    def _extract_contact_info(self, content: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Extract contact information from content"""
        import re
        
        # Email patterns
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, content)
        
        # Phone patterns
        phone_pattern = r'(\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})'
        phones = re.findall(phone_pattern, content)
        
        # Address patterns (simplified)
        address_pattern = r'\d+\s+[A-Za-z\s]+(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Drive|Dr|Lane|Ln)'
        addresses = re.findall(address_pattern, content)
        
        return {
            "emails": list(set(emails)),
            "phones": [''.join(phone) for phone in phones],
            "addresses": addresses,
            "title": metadata.get("title", ""),
            "description": metadata.get("description", "")
        }
    
    def _extract_product_info(self, content: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Extract product information from content"""
        import re
        
        # Price patterns
        price_pattern = r'\$[\d,]+\.?\d*'
        prices = re.findall(price_pattern, content)
        
        # Look for product-related keywords
        product_keywords = ["product", "item", "model", "brand", "price", "buy", "purchase"]
        product_sections = []
        
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if any(keyword in line.lower() for keyword in product_keywords):
                product_sections.append({
                    "line_number": i,
                    "content": line.strip()
                })
        
        return {
            "prices": prices,
            "product_sections": product_sections[:10],  # Limit to first 10
            "title": metadata.get("title", ""),
            "description": metadata.get("description", "")
        }
    
    def _extract_article_info(self, content: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Extract article information from content"""
        lines = content.split('\n')
        
        # Find headings
        headings = [line for line in lines if line.startswith('#')]
        
        # Find paragraphs
        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip() and not p.startswith('#')]
        
        # Estimate reading time (average 200 words per minute)
        word_count = len(content.split())
        reading_time = max(1, word_count // 200)
        
        return {
            "headings": headings,
            "paragraph_count": len(paragraphs),
            "word_count": word_count,
            "estimated_reading_time": f"{reading_time} minutes",
            "title": metadata.get("title", ""),
            "description": metadata.get("description", ""),
            "author": metadata.get("author", ""),
            "language": metadata.get("language", "")
        }

async def main():
    """Run advanced examples"""
    print("🚀 CS Crawler MCP - Advanced Usage Examples")
    print("=" * 60)
    print()
    
    crawler = Crawl4AIAdvanced()
    
    try:
        # Example 1: Batch crawling
        print("📋 Example 1: Batch Crawling")
        print("-" * 30)
        urls = [
            "https://httpbin.org/html",
            "https://httpbin.org/json",
            "https://httpbin.org/xml"
        ]
        
        batch_results = await crawler.batch_crawl(urls)
        for result in batch_results:
            status = "✅" if result["success"] else "❌"
            print(f"{status} {result['url']}: {result.get('length', 0)} chars")
        print()
        
        # Example 2: Content quality analysis
        print("🔍 Example 2: Content Quality Analysis")
        print("-" * 30)
        analysis = await crawler.analyze_content_quality("https://httpbin.org/html")
        if "error" not in analysis:
            ca = analysis["content_analysis"]
            print(f"📊 Word count: {ca['total_words']}")
            print(f"📊 Readability score: {ca['readability_score']:.1f}")
            print(f"📊 Headings: {ca['headings_count']}")
            print(f"📊 Links: {ca['links_count']}")
        print()
        
        # Example 3: Content comparison
        print("📊 Example 3: Content Comparison")
        print("-" * 30)
        comparison = await crawler.content_comparison(urls)
        print(f"📊 Average word count: {comparison['average_metrics']['words']:.0f}")
        print(f"📊 Average readability: {comparison['average_metrics']['readability']:.1f}")
        print()
        
        # Example 4: Structured data extraction
        print("🔍 Example 4: Structured Data Extraction")
        print("-" * 30)
        article_info = await crawler.extract_structured_data("https://httpbin.org/html", "article_info")
        if "error" not in article_info:
            print(f"📝 Title: {article_info['title']}")
            print(f"📝 Word count: {article_info['word_count']}")
            print(f"📝 Reading time: {article_info['estimated_reading_time']}")
            print(f"📝 Paragraphs: {article_info['paragraph_count']}")
        print()
        
        print("🎉 Advanced examples completed!")
        print()
        print("💡 These examples demonstrate:")
        print("   • Batch processing multiple URLs")
        print("   • Content quality analysis")
        print("   • Comparative analysis")
        print("   • Structured data extraction")
        print("   • Advanced text processing")
        
    except Exception as e:
        print(f"❌ Error running advanced examples: {e}")
        print("💡 Make sure the server is properly installed and configured")

if __name__ == "__main__":
    asyncio.run(main())
