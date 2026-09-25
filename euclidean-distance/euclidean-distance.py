import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here

    arr1 = np.array(x)
    arr2 = np.array(y)

    return float(np.sqrt(np.sum(np.square(arr1 - arr2))))
    pass