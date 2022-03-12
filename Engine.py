import numpy as np
from copy import deepcopy
from math import *
from time import process_time

from Plane import Plane
from Ball import Ball
from Plot import plot
from Random import rand_vec

class Engine:
    def __init__(s):
        # Options
        s.max_time = 3
        s.delta_time = 1e-2
        s.max_ball_speed = 1;
        s.ball_radius = 1e-10;
        s.balls_quantity = int(5e3)
        s.speed_bins = int(1e3)
        s.plot_trajectories = 0
        s.plot_momentums = 0
        s.plot_speeds = 1

        # Create planes
        s.planes = Plane.cube()

        # Create balls
        s.balls = [Ball(s.ball_radius, np.array([0.5] * 3), rand_vec() * s.max_ball_speed) for i in range(s.balls_quantity)]

    def run(s):
        start_time = process_time()

        frames = ceil(s.max_time / s.delta_time)
        for frame in range(frames):
            time = frame * s.delta_time
            for ball in s.balls:
                for plane in s.planes:
                    s.process_collision(ball, plane)
                ball.fix_trajectories()
                ball.move(s.delta_time)
            for plane in s.planes:
                plane.fix_momentum(time)

        print("Processed in %.3f seconds" % (process_time() - start_time))

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
            plot([Ball.get_speeds(s.balls, s.max_ball_speed, s.speed_bins, coord_idx)
                    for coord_idx in range(3)],
                mode='hist',
                colours=['r', 'g', 'b'],
                labels=['x', 'y', 'z'],
                title='Speed distribution',
                xlabel='Speed',
                ylabel='Quantity')

    def process_collision(s, ball, plane):
        d = np.dot(ball.pos, plane.norm) - np.dot(plane.pos, plane.norm) - ball.radius
        if d < 0:
            ball.pos -= plane.norm * d
            plane.add_momentum(abs(np.dot(ball.velocity, plane.norm)))
            ball.velocity = rand_vec() * np.linalg.norm(ball.velocity)
            if np.dot(ball.velocity, plane.norm) < 0:
                ball.velocity *= -1
