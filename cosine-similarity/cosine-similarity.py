import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a, b = np.array(a), np.array(b)
    if not np.linalg.norm(a) * np.linalg.norm(b):
        return 0.0
    return float((a @ b) / (np.linalg.norm(a) * np.linalg.norm(b)))