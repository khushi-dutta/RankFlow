from crawl4ai import AsyncWebCrawler
import asyncio
import os

async def crawl_site(url: str, output_dir: str = "output"):
    """
    Crawls a given URL and saves both HTML and Markdown representations.
    """
    os.makedirs(output_dir, exist_ok=True)
    print(f"Crawling {url}...")
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        
        # We simplify the filename based on the URL
        safe_name = url.replace("https://", "").replace("http://", "").replace("/", "_").strip("_")
        if not safe_name:
            safe_name = "index"
            
        md_path = os.path.join(output_dir, f"{safe_name}.md")
        html_path = os.path.join(output_dir, f"{safe_name}.html")
        
        if result.markdown is None or result.html is None:
            print(f"Failed to crawl {url}. Ensure the URL is correct and the site is online.")
            # Provide an empty string or error message so the pipeline doesn't crash completely
            result.markdown = f"# Error\n\nFailed to load {url}. The site may be offline or blocking crawlers."
            result.html = f"<html><body><h1>Error</h1><p>Failed to load {url}</p></body></html>"
            
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(result.markdown)
            
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(result.html)
            
        print(f"Saved {md_path} and {html_path}")
        return result.markdown, result.html, safe_name

# For standalone testing
if __name__ == "__main__":
    asyncio.run(crawl_site("https://example.com"))
