from typing import List, Dict

def calculate_alignment_risk(probe_pass_rates: List[float]) -> float:
    """
    P(A) formülünün hesaplanması:
    P(A) = 1 - Product(P(B_k passes | Optimized Prompt))
    """
    product = 1.0
    for rate in probe_pass_rates:
        product *= rate
    return 1.0 - product

def calculate_token_efficiency(original_prompts: List[Dict], optimized_prompts: List[Dict]) -> float:
    """
    Delta E formülünün hesaplanması:
    Delta E = Sum(W_i * T_orig,i) - Sum(W_i * T_opt,i)
    T değeri: (Token Cost / Compliance Score) olarak normalize edilmiştir.
    """
    delta_e = 0.0
    # İki listenin aynı uzunlukta olduğunu varsayıyoruz
    for orig, opt in zip(original_prompts, optimized_prompts):
        w_i = orig.get('weight', 1.0)
        
        # Sıfıra bölünme hatasını engellemek için compliance score kontrolü
        comp_orig = orig.get('compliance_score', 1.0) or 1.0
        comp_opt = opt.get('compliance_score', 1.0) or 1.0
        
        t_orig = orig.get('token_cost', 0.0) / comp_orig
        t_opt = opt.get('token_cost', 0.0) / comp_opt
        
        delta_e += (w_i * t_orig) - (w_i * t_opt)
    
    return delta_e