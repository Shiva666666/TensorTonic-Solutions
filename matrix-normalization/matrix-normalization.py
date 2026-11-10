import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here

    arr = np.array(matrix)

    if norm_type == "l1":
        norms = np.sum(np.abs(arr), axis=axis, keepdims=True)
    elif norm_type == "l2":
        norms = np.linalg.norm(arr, axis=axis, keepdims=True)
    else:
        norms = np.max(np.abs(arr), axis=axis, keepdims=True)

    norms = np.where(norms == 0, 1, norms)
    return arr / norms
    pass