import requests
import json
import os

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")

def rewrite_for_ai(page_text: str, use_mock=False):
    """
    Rewrites the given page text to be more AI-friendly (short paragraphs, bullet lists).
    """
    if use_mock:
        return f"## Rewritten for AI Readability\n\n- Improved clarity\n- Added bullet points\n\n### Original Text (Snippet)\n{page_text[:200]}..."
        
    prompt = (
        "Rewrite this page. Rules:\n"
        "- Use short paragraphs.\n"
        "- Simple English.\n"
        "- Bullet lists where appropriate.\n"
        "- Tables where appropriate.\n"
        "- Question headings.\n"
        "- Natural keywords, no keyword stuffing.\n"
        "- Target AI search engines.\n"
        "- Keep meaning unchanged.\n\n"
        "Return ONLY the rewritten markdown content.\n\n"
        f"Original Page:\n{page_text[:4000]}"
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
            return response.json()["choices"][0]["message"]["content"].strip()
        except Exception as e:
            if attempt == 2:
                print(f"Error rewriting content: {e}")
            else:
                time.sleep(2)
    return "Error occurred during rewriting."
