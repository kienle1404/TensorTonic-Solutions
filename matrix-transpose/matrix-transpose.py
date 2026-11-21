import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    m, n = len(A), len(A[0])
    res = np.zeros((n, m))
    for i in range(m):
        for j in range(n):
            res[j][i] = A[i][j]
    return res