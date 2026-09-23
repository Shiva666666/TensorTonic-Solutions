import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    # Write code here
    n = len(y_true)
    arr = np.zeros(n)
    for i in range(n):
        arr[i] = -np.log(y_pred[i][y_true[i]])

    return np.sum(arr)/n if n != 0 else 0
    
    pass