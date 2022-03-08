import numpy as np

class Plane:
    def __init__(s, pos, norm):
        s.pos = pos
        s.norm = norm
        s.momentums = []
        s.momentum = 0

    def dist(s, pos):
        return abs(np.dot(s.pos, s.norm) - np.dot(pos, s.norm))

    @staticmethod
    def cube(len = 1):
        res = []
        for i in range(3):
            for j in [1, 0]:
                pos = np.array([0] * 3)
                norm = np.array([0] * 3)
                norm[i] = 1 - 2 * j
                pos[i] = j
                res.append(Plane(pos, norm))
        return res

    def add_momentum(s, momentum):
        s.momentum += momentum

    def fix_momentum(s, time):
        s.momentums.append((time, s.momentum))
        s.momentum = 0
