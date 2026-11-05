from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    n = len(x)
    mean = sum(x) / n
    x.sort()
    median = x[n // 2] if n % 2 != 0 else (x[n // 2 - 1] + x[n // 2]) / 2
    mode = Counter(x).most_common(1)[0][0]

    return {"mean": mean, "median": float(median), "mode": float(mode)}