from random import random
import numpy as np
from math import sin, cos, pi

def rand_vec():
    phi   = random() * pi * 2
    tetha = random() * pi * 2
    return np.array(
            [ cos(tetha) * sin(phi)
            , sin(tetha) * sin(phi)
            , cos(phi)
            ])
