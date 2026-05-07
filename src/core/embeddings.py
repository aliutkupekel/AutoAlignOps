from sentence_transformers import SentenceTransformer
import numpy as np

# Yerel, tamamen ücretsiz ve oldukça hızlı çalışan hafif bir embedding modeli
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: str) -> np.ndarray:
    """Metni vektörel bir embedding'e dönüştürür."""
    return model.encode(text)

def calculate_cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """İki vektör arasındaki kosinüs benzerliğini hesaplar."""
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0.0
        
    return dot_product / (norm_vec1 * norm_vec2)