import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    arr = np.array(x)
    arr = arr - np.max(arr, axis=-1, keepdims=True)
    exponent = np.exp(arr)
    return exponent/np.sum(exponent, axis = -1, keepdims=True)
    pass