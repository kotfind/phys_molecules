import numpy as np

class Ball:
    def __init__(s, radius, pos, velocity):
        s.radius = radius
        s.pos = pos
        s.velocity = velocity

    def collides(s, plane):
        return plane.dist(s.pos) <= s.radius

    def reflect(s, norm):
        s.velocity = s.velocity - 2 * np.dot(s.velocity, norm) * norm

    def move(s, dtime):
        s.pos += s.velocity * dtime
