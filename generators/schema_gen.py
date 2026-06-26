import json

def generate_faq_schema(faq_list):
    """
    Generates a valid JSON-LD FAQPage schema from a list of FAQs.
    """
    if not faq_list:
        return None
        
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }
    
    for faq in faq_list:
        schema["mainEntity"].append({
            "@type": "Question",
            "name": faq["question"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq["answer"]
            }
        })
        
    return json.dumps(schema, indent=2)
