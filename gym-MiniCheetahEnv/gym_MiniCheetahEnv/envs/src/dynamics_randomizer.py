import random
import pybullet
import numpy as np


class DynamicsRandomizer():
    def __init__(self,pybullet_client,RobotClass):
        self.pybullet_client = pybullet_client
        self.robot = RobotClass.robot

    def _check_valid_index(self,link_index):
        if(link_index == -2):
            link_index = random.randint(0,self.robot._no_of_links)
        elif(link_index <-2 or link_index> self.robot._no_of_links):
            print("Invalid Index given")
            return False,-2
        return True, link_index


    def _add_random_mass(self, link_index = -2):

        _is_link,link_index = self._check_valid_index(self.robot,link_index)
        
        if(_is_link):
            # Add a random mass within 10% of the current mass
            current_mass = pybullet.getDynamicsInfo(self.robot,link_index)[0]
            current_mass += (random.uniform(-10.0,10.0)/100)* current_mass
            pybullet.changeDynamics(self.robot,link_index,mass = current_mass)
        
            
    def _vary_foot_friction(self) :
        _is_link,link_index = self._check_valid_index(self.robot,link_index)
        
        if(_is_link):
            # Vary friction by +-0.2
            current_friction = pybullet.getDynamicsInfo(self.robot,link_index)[1]
            current_friction += random.uniform(-0.2,0.2)
            current_friction = 0.0 if current_friction<0 else current_friction
            pybullet.changeDynamics(self.robot,link_index,lateralFriction = current_friction)