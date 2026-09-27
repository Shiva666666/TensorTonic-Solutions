import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    # Write code here

    n = len(y_pred)

    return np.sum(np.square(np.array(y_pred) - np.array(y_true)))/n if n != 0 else 0
    pass