import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    res = []
    n = len(x)

    x.sort()
    for qu in q:
        r = qu/100*(n-1)
        l, u = math.floor(r), math.ceil(r)
        w = r - l
        p_q = (1-w)*x[l] + w * x[u]
        res.append(p_q)
    return np.array(res)
            