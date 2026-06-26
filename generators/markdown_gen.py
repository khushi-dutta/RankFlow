def generate_llm_markdown(page_name, original_md, schema_json, internal_links, rewritten_text):
    """
    Combines all generated components into a single LLM-friendly Markdown file.
    """
    lines = []
    lines.append(f"# {page_name}")
    lines.append("\n## AI-Optimized Content\n")
    lines.append(rewritten_text)
    
    if internal_links:
        lines.append("\n## Related Reading\n")
        for link in internal_links:
            lines.append(f"- [{link}]({link}.md)")
            
    if schema_json:
        lines.append("\n## JSON-LD Schema\n")
        lines.append("```json\n" + schema_json + "\n```")
        
    lines.append("\n## Original Content\n")
    lines.append(original_md)
    
    return "\n".join(lines)
