import numpy as np
from math import *
from copy import deepcopy
from collections import Counter

class Ball:
    def __init__(s, radius, pos, velocity):
        s.radius = radius
        s.pos = pos
        s.velocity = velocity
        s.trajectory = []

    def reflect(s, norm):
        s.velocity = s.velocity - 2 * np.dot(s.velocity, norm) * norm

    def move(s, dtime):
        s.pos += s.velocity * dtime

    def fix_trajectories(s):
        s.trajectory.append(deepcopy(s.pos))

    @staticmethod
    def get_speeds(balls, max_ball_speed, speed_bins, coord_idx=0):
        delta_speed = max_ball_speed / speed_bins
        speeds = np.array([abs(ball.velocity[coord_idx]) for ball in balls])
        speeds = np.digitize(speeds, bins=np.cumsum(np.full(speed_bins - 1, delta_speed)))
        cntr = Counter(speeds)
        return [(bin_idx * delta_speed, cntr[bin_idx]) for bin_idx in range(speed_bins)]
