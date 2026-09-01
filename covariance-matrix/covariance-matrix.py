import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    x = np.array(X)
    x = x - np.mean(x, axis=0)

    sigma = x.T @ x / (x.shape[0] - 1)
    return sigma