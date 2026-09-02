import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    pmf = (math.exp(-lam) * math.pow(lam, k)) / math.factorial(k)
    
    cdf = 0.0
    for i in range(k+1):
        cdf += (math.exp(-lam) * math.pow(lam, i)) / math.factorial(i)

    return {"pmf": float(pmf), "cdf": float(cdf)}