import json
import requests
import os
import re

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")

def generate_faq(page_text: str, use_mock=False):
    """
    Generates FAQs from page text using OpenRouter API.
    """
    if use_mock:
        return [
            {"question": "What is the main topic of this page?", "answer": "This page covers the core subject matter discussed in the extracted text."},
            {"question": "Why is this information important?", "answer": "It provides valuable insights and services related to the domain, structured for AI overviews."}
        ]
        
    prompt = (
        "Read this page.\n\n"
        "Generate 5 FAQs.\n"
        "Return ONLY a raw JSON array of objects, each with a 'question' and 'answer' key. Do not use markdown blocks.\n"
        "Use conversational language. Target Google AI Overviews.\n\n"
        "Page content:\n"
        f"{page_text[:4000]}"
    )
    
    import time
    for attempt in range(3):
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json"
                },
                data=json.dumps({
                    "model": "meta-llama/llama-3.3-70b-instruct:free",
                    "messages": [
                        {"role": "user", "content": prompt}
                    ]
                })
            )
            if response.status_code == 429:
                print(f"Rate limited. Retrying in 6 seconds... (Attempt {attempt+1}/3)")
                time.sleep(6)
                continue
            if response.status_code != 200:
                print(f"Error: {response.status_code} - {response.text}")
            response.raise_for_status()
            result_text = response.json()["choices"][0]["message"]["content"].strip()
            
            # Try to parse JSON directly
            try:
                return json.loads(result_text)
            except json.JSONDecodeError:
                # Fallback: try to extract JSON array using regex if the model included markdown formatting
                match = re.search(r'\[.*\]', result_text, re.DOTALL)
                if match:
                    return json.loads(match.group(0))
                return []
        except Exception as e:
            if attempt == 2:
                print(f"Error generating FAQ: {e}")
            else:
                time.sleep(2)
    return []
