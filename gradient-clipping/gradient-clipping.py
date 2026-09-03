import numpy as np

def clip_gradients(g: list, max_norm: float) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as g.
    """
    # Write code here
    g = np.array(g)

    g_norm = np.sqrt(np.sum(g ** 2))

    g_clipped = g if g_norm <= max_norm else g * (max_norm / g_norm)
    return g_clipped