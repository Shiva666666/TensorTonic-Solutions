import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    arr = np.array(A)
    return np.trace(arr)
    pass