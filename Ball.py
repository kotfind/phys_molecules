import numpy as np
from math import *
from copy import deepcopy

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
    def get_speeds(balls, max_ball_speed, delta_ball_speed, coord_idx=0):
        speed_frames = ceil(max_ball_speed / delta_ball_speed) + 1
        speeds = [0 for i in range(speed_frames)]
        for ball in balls:
            speeds[int(round(abs(ball.velocity[coord_idx]) / delta_ball_speed))] += 1

        return [(speed_frame * delta_ball_speed, speeds[speed_frame])
                for speed_frame in range(speed_frames)]
