import numpy as np

class Ball:
    def __init__(s, pos, velocity):
        s.pos = pos
        s.velocity = velocity
        s.radius = 1e-2 # XXX

    def collides(s, plane):
        return plane.dist(s.pos) <= s.radius

    def reflect(s, norm):
        s.velocity = s.velocity - 2 * np.dot(s.velocity, norm) * norm

    def move(s, dtime):
        s.pos += s.velocity * dtime
