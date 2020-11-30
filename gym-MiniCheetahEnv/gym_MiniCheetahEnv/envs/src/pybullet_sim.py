import numpy as np
import gym
from gym import spaces
import math
import random
import time
import pybullet
import pybullet_data
from mini_cheetah_class import mini_cheetah

class Terrain():
    
    def __init__(self,render = True,on_rack = False, terrain_type = 'distorted'):
        self._is_render = render
        self._on_rack = on_rack

        if self._is_render:
            pybullet.connect(pybullet.GUI)
        else:
            pybullet.connect(pybullet.DIRECT)


        #Robot Positions
        self._robot_init_pos =[0,0,0.4]
        self._robot_init_ori = [0, 0, 0, 1]
        self.prev_feet_points = np.ndarray((5,3))


        #Simulation Parameters
        self.dt = 0.005
        self._frame_skip = 25
        pybullet.resetSimulation()
        pybullet.setPhysicsEngineParameter(numSolverIterations=int(300))
        pybullet.setTimeStep(self.dt/self._frame_skip)
        pybullet.setGravity(0, 0, -9.8)

        if(terrain_type == 'plane'):
            self.plane = pybullet.loadURDF("%s/plane.urdf" % pybullet_data.getDataPath())
            pybullet.changeVisualShape(self.plane,-1,rgbaColor=[1,1,1,0.9])

        elif(terrain_type == 'distorted'):
            numHeightfieldRows = 256
            numHeightfieldColumns = 256
            heightPerturbationRange = 0.06
            heightfieldData = [0]*numHeightfieldRows*numHeightfieldColumns 
            for j in range (int(numHeightfieldColumns/2)):
                for i in range (int(numHeightfieldRows/2) ):
                    height = random.uniform(0,heightPerturbationRange)
                    heightfieldData[2*i+2*j*numHeightfieldRows]=height
                    heightfieldData[2*i+1+2*j*numHeightfieldRows]=height
                    heightfieldData[2*i+(2*j+1)*numHeightfieldRows]=height
                    heightfieldData[2*i+1+(2*j+1)*numHeightfieldRows]=height
            
            terrainShape = pybullet.createCollisionShape(shapeType = pybullet.GEOM_HEIGHTFIELD, meshScale=[.05,.05,1], heightfieldTextureScaling=(numHeightfieldRows-1)/2, heightfieldData=heightfieldData, numHeightfieldRows=numHeightfieldRows, numHeightfieldColumns=numHeightfieldColumns)
            self.plane  = pybullet.createMultiBody(0, terrainShape)


        #Load Robot
        self.Mini_Cheetah = mini_cheetah(pybullet)

        #Set Camera
        self._cam_dist = 1.0
        self._cam_yaw = 0.0
        self._cam_pitch = 0.0
        pybullet.resetDebugVisualizerCamera(self._cam_dist, self._cam_yaw, self._cam_pitch, [0, 0, 0])

        if self._on_rack:
            self.Mini_Cheetah._set_on_rack()


    def _simulate(self):
        for _ in range(self._frame_skip):
            pybullet.stepSimulation()

    
    def _reset(self):
        pass
    
    def _vis_foot_traj(self):
        pass
	

if __name__ == "__main__":
    t = Terrain()
    while(True):
        t._simulate()
        time.sleep(t.dt)