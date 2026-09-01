import math
import numpy as np

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    n_k = math.factorial(n) / (math.factorial(n-k) * math.factorial(k))
    term = n_k * math.pow(p, k) * math.pow((1-p), (n-k))

    cdf = 0.0
    for i in range(k+1):
        n_i = math.factorial(n) / (math.factorial(n-i) * math.factorial(i))
        cdf += n_i * math.pow(p, i) * math.pow((1-p), (n-i))
        
    return {"pmf": float(term), "cdf": float(cdf)}