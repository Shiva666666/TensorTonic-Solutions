import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    arr = np.array(matrix)

    eigenval = np.linalg.eigvals(arr)
    eigenval.sort()
    return eigenval
    pass