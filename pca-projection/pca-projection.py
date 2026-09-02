import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    # Write code here
    X = np.array(X)
    X_c = X - np.mean(X, axis=0)
    n, d = X.shape
    cov = np.cov(X_c.T)
    eig, eigv = np.linalg.eigh(cov)
    idxs = np.argsort(eig)[::-1]
    eigv = eigv[:, idxs]
    W = eigv[:, :k]
    for j in range(k):
        max_idx = np.argmax(np.abs(W[:, j]))
        if W[max_idx, j] < 0:
            W[:, j] *= -1

    X_proj = X_c @ W
    return X_proj.tolist()