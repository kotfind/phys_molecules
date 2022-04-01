import numpy as np
from copy import deepcopy
from math import *
from time import process_time
import multiprocessing as mp

from Plane import Plane
from Ball import Ball
from Plot import plot
from Random import rand_unit_vec, rand_vec

class Engine:
    def __init__(s):
        # Options
        s.max_time = 3
        s.delta_time = 1e-2
        s.min_ball_speed = 1e1;
        s.max_ball_speed = 1e2;
        s.ball_radius = 1e-10;
        s.balls_quantity = int(5e3)
        s.speed_bins = int(1e3)
        s.plot_trajectories = 1
        s.plot_momentums = 1
        s.plot_speeds = 1

    def build_scene(s):
        # Create planes
        s.planes = Plane.cube()

        # Create balls
        s.balls = [Ball(s.ball_radius, np.array([0.5] * 3), rand_vec(s.min_ball_speed, s.max_ball_speed)) for i in range(s.balls_quantity)]

    def run(s):
        start_time = process_time()

        cpus = mp.cpu_count()
        range_len = s.balls_quantity // cpus
        ball_ranges = [s.balls[range_len * i:range_len * (i + 1)] for i in range(cpus - 1)] + [s.balls[(cpus - 1) * range_len:]]

        pool = mp.Pool(cpus)
        ball_ranges = pool.map(s.process_balls_range, ball_ranges)
        pool.close()

        s.balls = [ball for ball_range in ball_ranges for ball in ball_range]

        print("Processed in %.3f seconds" % (process_time() - start_time))

    def process_balls_range(s, balls):
        frames = ceil(s.max_time / s.delta_time)
        for frame in range(frames):
            time = frame * s.delta_time
            for ball in balls:
                for plane in s.planes:
                    Engine.process_collision(ball, plane)
                ball.fix_trajectories()
                ball.move(s.delta_time)
            for plane in s.planes:
                plane.fix_momentum(time)
        return balls

    @staticmethod
    def process_collision(ball, plane):
        d = np.dot(ball.pos, plane.norm) - np.dot(plane.pos, plane.norm) - ball.radius
        if d < 0:
            ball.pos -= plane.norm * d
            plane.add_momentum(abs(np.dot(ball.velocity, plane.norm)))
            ball.velocity = rand_unit_vec() * np.linalg.norm(ball.velocity)
            if np.dot(ball.velocity, plane.norm) < 0:
                ball.velocity *= -1

    def plot(s):
        if s.plot_trajectories:
            plot([ball.trajectory for ball in s.balls],
                mode='3d',
                title='Trajectories',
                xlabel='x',
                ylabel='y',
                zlabel='z')

        if s.plot_momentums:
            plot([plane.momentums for plane in s.planes],
                colours=[(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1)],
                labels=["pos: %10s; norm: %10s" %
                    (np.array2string(plane.pos), np.array2string(plane.norm))
                        for plane in s.planes],
                title='Momentum distribution',
                xlabel='Time',
                ylabel='Momentum')

        if s.plot_speeds:
            plot([Ball.get_speeds(s.balls, s.min_ball_speed, s.max_ball_speed, s.speed_bins, coord_idx)
                    for coord_idx in range(3)],
                mode='hist',
                colours=['r', 'g', 'b'],
                labels=['x', 'y', 'z'],
                title='Speed distribution',
                xlabel='Speed',
                ylabel='Quantity')
