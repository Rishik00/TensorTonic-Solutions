import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    x = np.array(x)
    s = np.sqrt(
        1 / (x.shape[0] - 1) * np.sum((x - np.mean(x)) ** 2)
    )
    
    num = np.mean(x) - mu0
    den = s / np.sqrt(x.shape[0])

    return float(num / den)
    