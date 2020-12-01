import random


class DynamicsRandomizer():
    def __init__(self,pybullet_client,RobotClass):
        self.pybullet_client = pybullet_client
        self.robot = RobotClass

    def _check_valid_index(self,link_index):
        if(link_index == -2):
            link_index = random.randint(0,self.robot._no_of_links)
        elif(link_index <-2 or link_index> self.robot._no_of_links):
            print("\nInvalid Index given\n")
            return False,-2
        return True, link_index


    def _add_random_mass(self, link_index = -2):

        _is_link,link_index = self._check_valid_index(link_index)
        
        if(_is_link):
            # Add a random mass within 10% of the current mass
            current_mass = self.pybullet_client.getDynamicsInfo(self.robot.model,link_index)[0]
            current_mass += (random.uniform(-10.0,10.0)/100)* current_mass
            self.pybullet_client.changeDynamics(self.robot.model,link_index,mass = current_mass)
        
            
    def _vary_feet_friction(self) :
        
        for foot in self.robot._feet_id_list:
            # Vary friction by +-0.2
            current_friction = self.pybullet_client.getDynamicsInfo(self.robot.model,foot)[1]
            current_friction += random.uniform(-0.2,0.2)
            current_friction = 0.0 if current_friction<0 else current_friction
            self.pybullet_client.changeDynamics(self.robot.model,foot,lateralFriction = current_friction)
