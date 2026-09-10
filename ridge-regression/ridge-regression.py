import numpy as np

def ridge_regression(X: list, y: list, lam: float) -> list:
    """
    Returns the ridge-regression weight vector.
    """
    # Write code here
    X, y = np.asarray(X), np.asarray(y)
    I = np.eye(X.shape[1])
    w = np.linalg.inv(np.matmul(X.T, X) + lam * I) @ X.T @ y
    return w.tolist()