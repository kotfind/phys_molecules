from random import random
import numpy as np

def rand_unit_vec():
    v = np.array([np.random.normal() for _ in range(3)])
    v /= np.linalg.norm(v)
    return v

def rand_vec(min_len, max_len):
    return rand_unit_vec() * (random() * (max_len - min_len) + min_len)
