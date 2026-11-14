import numpy as np

def triu_ones(n: int) -> np.ndarray:
    """n x n upper-triangular matrix of ones (including diagonal)."""
    # Your code here
    return np.array([[0 if i < j else 1 for i in range(n)] for j in range(n)], dtype = np.float64)
