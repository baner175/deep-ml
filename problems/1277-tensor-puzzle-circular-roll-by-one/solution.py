import numpy as np

def roll(a: np.ndarray) -> np.ndarray:
    """Circular left shift by one."""
    # Your code here
    n = len(a)
    return np.array([a[(i+1)%n] for i in range(n)])
