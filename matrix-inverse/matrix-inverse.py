import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    # Write code here

    def matrix_of_minors(arr):
        n = arr.shape[0]
        minors = np.zeros_like(arr, dtype=float)
        
        for i in range(n):
            for j in range(n):
                rows = [r for r in range(n) if r != i]
                cols = [c for c in range(n) if c != j]
                submatrix = arr[np.ix_(cols, rows)]
                minors[i, j] = np.linalg.det(submatrix)

                minors[i,j] *= (-1)**(i+j)
        return minors
        
    det = np.linalg.det(A)
    
    if np.isclose(det, 0):
        return None

    res = matrix_of_minors(np.array(A))
    return res/det
    pass