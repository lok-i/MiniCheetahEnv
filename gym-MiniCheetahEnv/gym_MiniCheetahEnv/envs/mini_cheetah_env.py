import numpy as np
import gym
from gym import spaces
import math
import random
import time
from src.world import Terrain



class MiniCheetahEnv(gym.Env):

	def __init__(self,render = True, on_rack = False):

		# MDP yet to be formulated
		self._action_dim = 12
		action_high = np.array([200] * self._action_dim)
		action_low = np.array([150] * self._action_dim)
		self.action_space = spaces.Box(action_low, action_high)

		self._obs_dim = 10 
		observation_high = np.array([1] * self._obs_dim)
		observation_low = -observation_high
		self.observation_space = spaces.Box(observation_low, observation_high)

		# Initiatlize the world with the terrain as plane,distorted or stairs
		self.World = Terrain(on_rack = on_rack, terrain_type='stairs')

	def step(self,action):

		#assuming the actions are unnormalized, raw torque values
		self.World._simulate(torques=action)
		
		observation = self.World._get_observation()
		reward,done = self._caclulate_reward()
		return observation, reward, done,{}

	def reset(self):

		# send back initial state
		self.World._reset_world()
		observation = self.World._get_observation()
		reward,done = self._caclulate_reward()
		return observation, reward, done,{}

	def _caclulate_reward(self):
		# Yet to implement, it will aswell check for termination condition
		return 0,False
	

if __name__ == "__main__":
	
	no_of_episodes = 10
	episode_length = 400

	# the robot is kept fixed on a rack
	env = MiniCheetahEnv(on_rack=True)
	
	for episode in range(no_of_episodes):
		print("Episode No:",episode)
		env.reset()
		episode_returns = 0

		for _ in range(episode_length):
			#random torque sampled
			torques = env.action_space.sample()
			state,reward,done,_ =env.step(action=torques)
			episode_returns += reward

		print("Epidsode Return:",episode_returns)

	
		



