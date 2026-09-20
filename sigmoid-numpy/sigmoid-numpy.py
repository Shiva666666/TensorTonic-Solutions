import numpy as np
from math import e

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here

    if isinstance(x, float) or isinstance(x, int):
        return (1+(e**-x))**-1


    arr = np.array(x)

    return (1+np.exp(-arr))**-1
        
    pass