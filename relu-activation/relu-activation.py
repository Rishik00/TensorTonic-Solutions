import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    if isinstance(x, list):
        x = np.array(x)

    return np.asarray(np.maximum(0.0, x))