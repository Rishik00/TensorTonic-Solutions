import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    # Write code here
    X, y = np.asarray(X, dtype=np.float64), np.asarray(y, dtype=np.float64)
    w = np.linalg.inv(np.matmul(X.T, X)) @ X.T @ y
    return w.tolist()
    