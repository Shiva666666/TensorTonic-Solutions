import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    arr = np.array(x)@np.array(p)
    return float(arr)
    pass