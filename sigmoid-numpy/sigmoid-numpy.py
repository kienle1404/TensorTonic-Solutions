import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    x_arr = np.asarray(x)
    res = 1 / (1 + np.exp(-np.abs(x_arr)))
    res = np.where(x_arr >= 0, res, 1 - res)
    
    return float(res) if np.isscalar(x) else res.tolist()