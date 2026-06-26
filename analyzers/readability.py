import re

def analyze_readability(text_content: str):
    """
    Basic readability checks targeting AI-friendly formatting.
    """
    report = []
    
    # Check for long paragraphs
    paragraphs = text_content.split("\n\n")
    long_paragraphs = [p for p in paragraphs if len(p.split()) > 60]
    if long_paragraphs:
        report.append(f"❌ {len(long_paragraphs)} Long Paragraph(s) (>60 words)")
    else:
        report.append("✅ No Long Paragraphs")
        
    # Check for lists
    if "- " in text_content or "* " in text_content or "1. " in text_content:
        report.append("✅ Bullet/Numbered lists found")
    else:
        report.append("❌ Missing lists (Lists improve AI readability)")
        
    return report
