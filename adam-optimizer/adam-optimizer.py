import numpy as np

def adam_step(
    param: list,
    grad: list,
    m: list,
    v: list,
    t: int,
    lr: float = 1e-3,
    beta1: float = 0.9,
    beta2: float = 0.999,
    eps: float = 1e-8,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Returns (param_new, m_new, v_new) as NumPy arrays.
    """
    # Write code here
    param, grad, m, v = np.array(param), np.array(grad), np.array(m), np.array(v)

    m_t = beta1 * m + (1.0 - beta1) * grad
    v_t = beta2 * v + (1.0 - beta2) * (grad * grad)

    new_m = m_t / (1.0 - beta1 ** t)
    new_v = v_t / (1.0 - beta2 ** t)

    param_new = param - lr * (new_m / (np.sqrt(new_v) + eps))

    return param_new, m_t, v_t
    
    

    