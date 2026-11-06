import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    pmf = lambda x : math.comb(n, x) * p**x * (1-p)**(n-x)
    cdf = sum([pmf(i) for i in range(k+1)])
    return  {"pmf": float(pmf(k)), "cdf": float(cdf)}