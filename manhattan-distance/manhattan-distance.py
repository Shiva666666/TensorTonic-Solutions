import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    arr1 = np.array(x)
    arr2 = np.array(y)

    return float(np.sum(np.abs(arr1 - arr2)))
    pass