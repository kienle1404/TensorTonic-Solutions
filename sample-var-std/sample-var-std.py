import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    n = len(x)
    mean = np.mean(x)
    variance = sum([(i - mean)**2 for i in x]) / (n-1)
    std = variance**0.5
    return {"variance": float(variance), "standard_deviation": float(std)}