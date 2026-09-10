import numpy as np
import math
from collections import Counter



def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    l = len(y)
    c = Counter(y)
    
    num_classes = len(list(c))

    for i in range(num_classes):
        c[i] = c[i] / len(y)

    H = 0.0
    for i in range(num_classes):
        if c[i] > 0:
            H = H + (c[i] * math.log2(c[i]))

    return -H