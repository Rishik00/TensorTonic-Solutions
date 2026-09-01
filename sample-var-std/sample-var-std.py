import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.array(x)
    mean = np.mean(x)

    var = 1 / (x.shape[0] - 1) * (np.sum((x - mean) ** 2))
    return {"variance": float(var), "standard_deviation": float(np.sqrt(var))}