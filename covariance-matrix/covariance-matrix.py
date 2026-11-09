import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here

    arr = np.array(X)
    mean = np.mean(arr, axis = 0)

    Xc = arr - mean

    return Xc.T @ Xc/(len(X)-1)
    pass