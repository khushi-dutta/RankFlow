import asyncio
import sys
import os
from dotenv import load_dotenv

load_dotenv()

from crawler.crawl import crawl_site
from analyzers.metadata import analyze_metadata
from analyzers.headings import analyze_headings
from analyzers.readability import analyze_readability
from analyzers.schema import analyze_existing_schema
from analyzers.internal_links import suggest_internal_links
from generators.faq import generate_faq
from generators.schema_gen import generate_faq_schema
from generators.rewrite import rewrite_for_ai
from generators.markdown_gen import generate_llm_markdown
from reports.scores import calculate_scores
from reports.html_report import generate_html_report

async def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1]
    output_dir = "output"
    
    print("=== Step 1: Crawling ===")
    md_content, html_content, page_name = await crawl_site(url, output_dir=output_dir)
    
    print("=== Step 2-4: Analyzers ===")
    meta_report = analyze_metadata(html_content)
    headings_report = analyze_headings(html_content)
    readability_report = analyze_readability(md_content)
    schema_report = analyze_existing_schema(html_content)
    
    # Internal links requires multiple pages. We mock it for a single page run.
    # In a full crawler, we'd pass all crawled pages.
    pages_dict = {
        page_name: md_content,
        "dummy_page_1": "This is some dummy content about SEO.",
        "dummy_page_2": "Technical guides and information.",
    }
    links_report = suggest_internal_links(pages_dict)
    
    print("=== Step 5-8: Generators ===")
    faqs = generate_faq(md_content)
    faq_schema = generate_faq_schema(faqs)
    rewritten_md = rewrite_for_ai(md_content)
    
    final_md = generate_llm_markdown(
        page_name=page_name, 
        original_md=md_content, 
        schema_json=faq_schema, 
        internal_links=links_report.get(page_name, []),
        rewritten_text=rewritten_md
    )
    
    final_md_path = os.path.join(output_dir, f"{page_name}_optimized.md")
    with open(final_md_path, "w", encoding="utf-8") as f:
        f.write(final_md)
        
    print("=== Step 9: Report Generation ===")
    scores = calculate_scores(
        metadata_report=meta_report,
        headings_report=headings_report,
        readability_report=readability_report,
        has_schema=bool(faq_schema),
        missing_links_count=0 if links_report.get(page_name) else 1
    )
    
    report_data = {
        "scores": scores,
        "metadata": meta_report,
        "headings": headings_report,
        "readability": readability_report,
        "schema": schema_report,
        "internal_links": links_report
    }
    
    generate_html_report(report_data, output_path=os.path.join(output_dir, "report.html"))
    
    print(f"Pipeline Complete! Check the '{output_dir}' directory.")

if __name__ == "__main__":
    asyncio.run(main())
