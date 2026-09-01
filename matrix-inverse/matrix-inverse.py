import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    # Write code here
    A = np.array(A)
    if np.linalg.det(A) == 0:
        return None
    return np.linalg.inv(A)