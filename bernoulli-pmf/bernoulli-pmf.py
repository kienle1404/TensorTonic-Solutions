import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    pmf = [p if val == 1 else 1-p for val in x]
    mean = p
    variance = p * (1-p)
    return {"pmf": np.array(pmf), "mean": float(mean), "variance": float(variance)}
    