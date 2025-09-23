# Claude Desktop Usage Examples

This document provides practical examples of how to use the CS Crawler MCP with Claude Desktop.

## 🚀 Getting Started

After installing and configuring the MCP server, restart Claude Desktop and start a new conversation. The crawl4ai tools will be automatically available.

## 📰 News and Content Analysis

### Example 1: News Article Summary
```
Please crawl https://news.ycombinator.com and give me a summary of the top 5 stories with their scores and comments count.
```

### Example 2: Blog Post Analysis
```
Crawl https://blog.example.com/latest-post and extract the main points, key quotes, and author information.
```

### Example 3: Multiple News Sources
```
Crawl these news URLs and compare the coverage of the same story:
- https://news-site-1.com/article
- https://news-site-2.com/article
- https://news-site-3.com/article
```

## 🛒 E-commerce and Product Research

### Example 4: Product Comparison
```
Extract all product information from https://store.example.com/products including names, prices, descriptions, and ratings. Format this as a comparison table.
```

### Example 5: Price Monitoring
```
Get the current prices for these products and track any discounts:
- https://store.com/product1
- https://store.com/product2
- https://store.com/product3
```

### Example 6: Product Reviews Analysis
```
Crawl https://reviews.example.com/product and extract all customer reviews with ratings, dates, and review text. Analyze the sentiment.
```

## 📚 Documentation and Learning

### Example 7: Documentation Deep Dive
```
Do a deep crawl of https://docs.python.org/3/tutorial/ starting from the introduction page. Give me a comprehensive overview of all the topics covered and create a learning path.
```

### Example 8: API Documentation
```
Extract all API endpoints from https://api-docs.example.com and create a reference guide with parameters, responses, and examples.
```

### Example 9: Technical Blog Series
```
Crawl this blog series and create a summary of all posts:
- https://blog.com/post-1
- https://blog.com/post-2
- https://blog.com/post-3
- https://blog.com/post-4
```

## 📊 Data Extraction and Analysis

### Example 10: Financial Data
```
Extract all financial tables from https://finance.example.com/earnings-report and analyze the quarterly performance trends.
```

### Example 11: Research Data
```
Get all the research data from https://research.example.com/study including methodology, findings, and conclusions.
```

### Example 12: Statistical Information
```
Extract all statistics and data points from https://stats.example.com/report and create a summary with key insights.
```

## 🔍 SEO and Website Analysis

### Example 13: SEO Audit
```
Analyze the SEO elements of https://example.com including title, meta description, headings, and internal linking structure.
```

### Example 14: Competitor Analysis
```
Compare the content structure and SEO elements of these competitor websites:
- https://competitor1.com
- https://competitor2.com
- https://competitor3.com
```

### Example 15: Content Audit
```
Do a deep crawl of https://blog.example.com and analyze the content topics, publication dates, and engagement metrics.
```

## 🏢 Business Intelligence

### Example 16: Company Research
```
Extract company information from https://company.example.com/about including team members, services, and contact details.
```

### Example 17: Market Research
```
Crawl these industry reports and extract key market trends and statistics:
- https://report1.com/market-analysis
- https://report2.com/industry-trends
- https://report3.com/forecast
```

### Example 18: Job Market Analysis
```
Extract all job listings from https://jobs.example.com and analyze the required skills, salary ranges, and company types.
```

## 🎓 Educational Content

### Example 19: Course Content
```
Crawl https://course.example.com and extract all lesson titles, descriptions, and learning objectives to create a course outline.
```

### Example 20: Academic Papers
```
Extract the abstract, methodology, and conclusions from these research papers:
- https://journal.com/paper1
- https://journal.com/paper2
- https://journal.com/paper3
```

### Example 21: Tutorial Series
```
Get all tutorials from https://tutorials.example.com and create a structured learning path with prerequisites and difficulty levels.
```

## 🎯 Advanced Use Cases

### Example 22: Multi-step Research
```
1. First, crawl https://overview.example.com to get the main topics
2. Then, for each topic, do a deep crawl to get detailed information
3. Finally, synthesize all the information into a comprehensive report
```

### Example 23: Data Validation
```
Crawl https://data-source.com and extract all the data, then validate it against the schema and identify any inconsistencies.
```

### Example 24: Content Migration
```
Extract all content from https://old-site.com and format it for migration to a new platform, preserving structure and metadata.
```

## 💡 Tips for Better Results

### 1. Be Specific with Requests
Instead of: "Crawl this website"
Try: "Crawl https://example.com and extract all product names, prices, and descriptions in a structured format"

### 2. Use Multiple Tools
Combine different tools for comprehensive analysis:
- Use `get_page_metadata` for quick overview
- Use `crawl_url` for detailed content
- Use `extract_tables` for structured data
- Use `deep_crawl` for comprehensive coverage

### 3. Specify Output Format
- Use `"markdown"` for readable content
- Use `"json"` for structured data
- Use `"html"` for preserving formatting

### 4. Handle Large Sites
For large websites, use `deep_crawl` with appropriate limits:
```
Do a deep crawl of https://large-site.com with max_pages=10 and same_domain_only=true
```

### 5. Error Handling
If a crawl fails, try:
- A simpler URL first
- Different output format
- Check if the site requires authentication

## 🔧 Troubleshooting

### Common Issues

**1. "Tool not found" error**
- Restart Claude Desktop
- Check your MCP configuration
- Verify the server is running

**2. "Crawl failed" error**
- Try a different URL
- Check if the site is accessible
- Verify your internet connection

**3. "Empty content" result**
- The site might be JavaScript-heavy
- Try a different output format
- Check if the site blocks automated access

### Getting Help

If you encounter issues:
1. Check the server logs
2. Test with simple URLs first
3. Verify your configuration
4. Check the GitHub issues page

## 🎉 Conclusion

The CS Crawler MCP opens up powerful web crawling capabilities directly in Claude Desktop. Use these examples as starting points and adapt them to your specific needs. The key is to be specific about what you want to extract and how you want it formatted.

Happy crawling! 🚀
