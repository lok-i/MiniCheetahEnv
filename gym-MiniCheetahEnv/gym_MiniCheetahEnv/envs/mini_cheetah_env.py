import numpy as np
import gym
from gym import spaces
import math
import random
import time
import pybullet
import pybullet_data


class MiniCheetahEnv(gym.Env):

	def __init__(self,render = True):
		self._action_dim = 60
		action_high = np.array([1] * self._action_dim)
		self.action_space = spaces.Box(-action_high, action_high)

		self._obs_dim = 10 # random
		observation_high = np.array([1] * self._obs_dim)
		observation_low = -observation_high
		self.observation_space = spaces.Box(observation_low, observation_high)

		pass
	def step(self):
		pass
	def reset(self):
		pass
	def _caclulate_reward(self):
		pass

	
		



