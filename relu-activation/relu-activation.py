import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    if isinstance(x, int):
        return np.array(max(0, x))
    return np.maximum(0,x)
    pass