import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a, b = np.array(a), np.array(b)
    a_mod, b_mod = np.linalg.norm(a), np.linalg.norm(b)
    if a_mod == 0.0 or b_mod == 0.0:
        return 0.0
        
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))