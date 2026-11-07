import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    arr1 = np.array(a)
    arr2 = np.array(b)

    return float(np.dot(arr1,arr2)/((np.linalg.norm(arr1))*(np.linalg.norm(arr2))) if (np.linalg.norm(arr1)) and (np.linalg.norm(arr2)) else 0)
    pass