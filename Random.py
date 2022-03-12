from random import random
import numpy as np

def rand_vec():
    v = np.array([np.random.normal() for _ in range(3)])
    v /= np.linalg.norm(v)
    return v
