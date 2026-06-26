from bs4 import BeautifulSoup
import json

def analyze_existing_schema(html_content: str):
    """
    Checks for existing JSON-LD schema on the page.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    schemas = soup.find_all("script", type="application/ld+json")
    
    report = []
    if not schemas:
        report.append("❌ Missing Schema")
    else:
        report.append(f"✅ Found {len(schemas)} Schema block(s)")
        # Basic validation
        for i, s in enumerate(schemas):
            try:
                data = json.loads(s.string)
                if isinstance(data, dict) and "@type" in data:
                    report.append(f"  - Valid Schema Type: {data['@type']}")
                elif isinstance(data, list) and len(data) > 0 and "@type" in data[0]:
                    report.append(f"  - Valid Schema Type: {data[0]['@type']}")
            except Exception:
                report.append(f"❌ Invalid JSON in Schema block {i+1}")
                
    return report
