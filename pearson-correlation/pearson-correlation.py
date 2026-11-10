import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    arr = np.array(X, dtype=float)
    mean = np.mean(arr, axis=0, keepdims=True)
    
    centered = arr - mean
    cov = (centered.T @ centered) / (len(X) - 1)
    denom = np.sqrt(np.diag(cov))
    
    return cov / np.outer(denom, denom)
    pass