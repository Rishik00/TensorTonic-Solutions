import numpy as np

def node_impurity(labels):
    if labels.size == 0:
        return 0.0

    counts = np.unique(labels, return_counts=True)[1]
    probs = counts/labels.size

    return float(1.0 - np.sum(probs ** 2))

def gini_impurity(y_left: list, y_right: list):

    left, right = np.asarray(y_left), np.asarray(y_right)

    total = left.size + right.size 
    if total == 0: return 0.0

    return float(
        (left.size * node_impurity(left) + right.size * node_impurity(right)) / total
    )