import numpy as np

class Ball:
    def __init__(s, radius, pos, velocity):
        s.radius = radius
        s.pos = pos
        s.velocity = velocity

    def reflect(s, norm):
        s.velocity = s.velocity - 2 * np.dot(s.velocity, norm) * norm

    def move(s, dtime):
        s.pos += s.velocity * dtime
