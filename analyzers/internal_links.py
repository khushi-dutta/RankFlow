from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

def suggest_internal_links(pages_content_dict, top_k=3):
    """
    Given a dict of {page_name: page_text}, compute embeddings
    and suggest top_k internal links for each page.
    """
    if not pages_content_dict or len(pages_content_dict) < 2:
        return {}
        
    print("Loading SentenceTransformer model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    
    page_names = list(pages_content_dict.keys())
    page_texts = [pages_content_dict[name] for name in page_names]
    
    print("Computing embeddings...")
    embeddings = model.encode(page_texts)
    
    similarity_matrix = cosine_similarity(embeddings)
    
    suggestions = {}
    for i, name in enumerate(page_names):
        # Sort indices by similarity descending, excluding self
        similar_indices = similarity_matrix[i].argsort()[::-1]
        similar_indices = [idx for idx in similar_indices if idx != i]
        
        top_indices = similar_indices[:top_k]
        suggestions[name] = [page_names[idx] for idx in top_indices]
        
    return suggestions
