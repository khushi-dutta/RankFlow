from bs4 import BeautifulSoup
from collections import Counter

def analyze_headings(html_content: str):
    """
    Analyzes heading structures (H1-H6) for SEO best practices.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    
    report = []
    h1s = [h for h in headings if h.name == "h1"]
    
    if len(h1s) == 0:
        report.append("❌ No H1")
    elif len(h1s) > 1:
        report.append("❌ Multiple H1")
    else:
        report.append("✅ Single H1 Found")
        
    # Check for empty headings
    empty_headings = [h for h in headings if not h.text.strip()]
    if empty_headings:
        report.append(f"❌ {len(empty_headings)} Empty heading(s)")
        
    # Duplicate headings
    heading_texts = [h.text.strip() for h in headings if h.text.strip()]
    duplicates = [text for text, count in Counter(heading_texts).items() if count > 1]
    if duplicates:
        report.append(f"❌ {len(duplicates)} Duplicate heading(s) found")
        
    # Checking for jumps (e.g. h2 -> h4)
    previous_level = 0
    jump_found = False
    for h in headings:
        level = int(h.name[1])
        if previous_level > 0 and level > previous_level + 1:
            jump_found = True
            report.append(f"❌ Jump from H{previous_level} to H{level}")
        previous_level = level
        
    if not jump_found:
        report.append("✅ No Heading Jumps")
        
    return report
