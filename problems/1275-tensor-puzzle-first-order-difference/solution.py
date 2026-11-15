import numpy as np

def diff(a: np.ndarray) -> np.ndarray:
    """out[0]=a[0]; out[i]=a[i]-a[i-1] for i>0."""
    # Your code here
    diff_1 = [a[i+1] - a[i] for i in range(len(a)-1)]
    diff_1.insert(0, a[0])
    return np.array(diff_1)
