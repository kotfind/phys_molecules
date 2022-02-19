import numpy as np

class Plane:
    def __init__(s, pos, norm):
        s.pos = pos
        s.norm = norm

    def dist(s, pos):
        return abs(np.dot(s.pos, s.norm) - np.dot(pos, s.norm))
