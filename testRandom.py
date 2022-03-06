from Random import rand_vec
from Plot import plot3d
import numpy as np

toplot = []
for i in range(1000):
    v = rand_vec()
    toplot.append([v, v * (1 + 2e-2)])

plot3d(toplot)
