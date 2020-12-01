import numpy as np
import gym
from gym import spaces
import math
import random
import time
from src.world import Terrain



class MiniCheetahEnv(gym.Env):

	def __init__(self,render = True):
		self._action_dim = 60
		action_high = np.array([1] * self._action_dim)
		self.action_space = spaces.Box(-action_high, action_high)

		self._obs_dim = 10 # random
		observation_high = np.array([1] * self._obs_dim)
		observation_low = -observation_high
		self.observation_space = spaces.Box(observation_low, observation_high)

		self.World = Terrain()

	def step(self):
		pass
	def reset(self):
		# send back initial state
		self.World._reset_world()

	def _caclulate_reward(self):
		pass

if __name__ == "__main__":
	env = MiniCheetahEnv()

	while True:
		env.World._simulate()
		time.sleep(env.World.dt)

	
		



