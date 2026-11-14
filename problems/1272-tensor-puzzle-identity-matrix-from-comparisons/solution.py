import numpy as np

def eye(n: int) -> np.ndarray:
    """n x n identity matrix without np.eye."""
    # Your code here
    return np.array([[1 if i == j else 0 for i in range(n)] for j in range(n)], dtype = np.float64)
