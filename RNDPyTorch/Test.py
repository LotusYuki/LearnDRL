import numpy as np
import os
from collections import deque
import gym
from gym import spaces
import cv2
import random
from envs import AtariEnvironment




env = gym.make("procgen:procgen-coinrun-v0")


action_space = env.action_space.n
input_size = env.observation_space.shape
print(action_space)
print(input_size)
env.reset()

'''
for step in range(100000):
    action = random.randint(0,14)
    _obs, rews, _dones, _infos = env.step(action)
    print("step", step, "rews", rews)
    env.render()
    if _dones:
        env.reset()
'''
    