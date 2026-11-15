import numpy as np

def cumsum(a: np.ndarray) -> np.ndarray:
    """Inclusive cumulative sum of 1-D array a without np.cumsum."""
    # Your code here
    lower_tri = np.array([[1 if i<=j else 0 for i in range(len(a))] for j in range(len(a))], dtype = np.float64)
    return lower_tri @ a
