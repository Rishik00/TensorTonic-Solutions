import numpy as np

def zscore_standardize(
    X: list, 
    axis: int = 0, 
    eps: float = 1e-12
) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    X = np.array(X) + eps
    std = np.std(X, axis=axis, keepdims=True)
    return (X - np.mean(X, axis=axis, keepdims=True)) / np.where(std > eps, std, 1.0)