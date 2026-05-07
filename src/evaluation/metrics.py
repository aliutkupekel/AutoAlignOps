from src.core.embeddings import get_embedding, calculate_cosine_similarity

def calculate_adr(original_prompt: str, optimized_prompt: str) -> float:
    """
    Alignment Drift Rate (ADR) hesaplar.
    Formül: Kosinüs Uzaklığı = 1 - Kosinüs Benzerliği
    """
    emb_orig = get_embedding(original_prompt)
    emb_opt = get_embedding(optimized_prompt)
    similarity = calculate_cosine_similarity(emb_orig, emb_opt)
    
    # Benzerlik 1'e ne kadar yakınsa, drift o kadar 0'a yakındır.
    return 1.0 - similarity

def calculate_brr(failed_probes: int, total_probes: int) -> float:
    """
    Behavioral Regression Rate (BRR) hesaplar.
    Açıklama: Optimizasyon sonrası bozulan davranışsal testlerin (probes) yüzdesi.
    """
    if total_probes == 0:
        return 0.0
    return failed_probes / total_probes