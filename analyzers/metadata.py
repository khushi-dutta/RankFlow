from bs4 import BeautifulSoup

def analyze_metadata(html_content: str):
    """
    Analyzes basic SEO metadata tags in the provided HTML.
    Returns a list of finding strings.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    
    title = soup.title
    description = soup.find("meta", attrs={"name": "description"})
    canonical = soup.find("link", attrs={"rel": "canonical"})
    robots = soup.find("meta", attrs={"name": "robots"})
    og_title = soup.find("meta", attrs={"property": "og:title"})
    twitter_card = soup.find("meta", attrs={"name": "twitter:card"})
    
    report = []
    
    if not title or not title.string:
        report.append("❌ Missing Title")
    else:
        report.append("✅ Title Found")
        
    if not description or not description.get("content"):
        report.append("❌ Missing Description")
    else:
        report.append("✅ Description Found")
        
    if not canonical:
        report.append("❌ Missing Canonical")
    else:
        report.append("✅ Canonical Found")
        
    if not og_title:
        report.append("❌ Missing OpenGraph Title")
    else:
        report.append("✅ OpenGraph Title Found")
        
    if not twitter_card:
        report.append("❌ Missing Twitter Card")
    else:
        report.append("✅ Twitter Card Found")
        
    return report
