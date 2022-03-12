from Random import rand_vec
import numpy as np

print(np.sum(np.array([rand_unit_vec() for _ in range(int(1e5))]), axis=0))
