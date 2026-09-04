import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    y = np.array(y)
    n = y.shape[0]
    k = num_classes if num_classes != None else np.max(y) + 1
    
    one_hot = np.zeros(shape=(n, k))
    one_hot[np.arange(y.size), y] = 1.0
        
    return one_hot