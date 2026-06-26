def calculate_scores(metadata_report, headings_report, readability_report, has_schema, missing_links_count):
    """
    Calculates SEO, AEO, and GEO scores based on the analysis reports.
    """
    # Simple heuristics for demonstration
    seo_score = 100
    aeo_score = 100
    geo_score = 100
    
    # Penalize SEO
    if any("❌" in item for item in metadata_report):
        seo_score -= 15
    if any("❌" in item for item in headings_report):
        seo_score -= 10
        
    # Penalize AEO (Answer Engine Optimization)
    if not has_schema:
        aeo_score -= 20
    if any("❌" in item for item in readability_report):
        aeo_score -= 15
        
    # Penalize GEO (Generative Engine Optimization)
    if missing_links_count > 0:
        geo_score -= (missing_links_count * 2)
    
    return {
        "SEO": max(0, seo_score),
        "AEO": max(0, aeo_score),
        "GEO": max(0, geo_score)
    }
