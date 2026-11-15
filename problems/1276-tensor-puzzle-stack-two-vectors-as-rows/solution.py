import numpy as np

def vstack(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Stack 1-D arrays a and b as rows of a (2, n) matrix."""
    # Your code here
    mask_a = np.array([[1]*len(a), [0]*len(b)])
    mask_b = np.array([[0]*len(a), [1]*len(b)])

    return a*mask_a + b*mask_b
