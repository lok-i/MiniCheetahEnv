import numpy as np
import gym
from gym import spaces
import math
import csv
import cv2
import random
import time
import pybullet
import pybullet_data
# from src.mini_cheetah_class import mini_cheetah
# from src.dynamics_randomization import DynamicsRandomizer

from mini_cheetah_class import mini_cheetah
from dynamics_randomization import DynamicsRandomizer

class Terrain():
    
    def __init__(self,render = True,on_rack = False, terrain_type = 'plane'):
        self._is_render = render
        self._on_rack = on_rack

        if self._is_render:
            pybullet.connect(pybullet.GUI)
        else:
            pybullet.connect(pybullet.DIRECT)


        #Robot Positions
        self._robot_init_pos =[0,0,0.4]
        self._robot_init_ori = [0, 0, 0, 1]


        #Simulation Parameters
        self.dt = 0.005
        self._frame_skip = 25
        pybullet.resetSimulation()
        pybullet.setPhysicsEngineParameter(numSolverIterations=int(300))
        pybullet.setTimeStep(self.dt/self._frame_skip)
        pybullet.setGravity(0, 0, -9.8)

        # Load Terrain
        if(terrain_type == 'plane' or terrain_type == 'stairs'):
            self.plane = pybullet.loadURDF("%s/plane.urdf" % pybullet_data.getDataPath())
            pybullet.changeVisualShape(self.plane,-1,rgbaColor=[1,1,1,0.9])
            if(terrain_type=='stairs'):
                boxHalfLength = 0.15
                boxHalfWidth = 1
                boxHalfHeight = 0.05
                sh_colBox = pybullet.createCollisionShape(pybullet.GEOM_BOX,halfExtents=[boxHalfLength,boxHalfWidth,boxHalfHeight])
                boxOrigin = 1
                n_steps = 15
                self.stairs = []
                for i in range(n_steps):
                    step =pybullet.createMultiBody(baseMass=0,baseCollisionShapeIndex = sh_colBox,basePosition = [boxOrigin + i*2*boxHalfLength,0,boxHalfHeight + i*2*boxHalfHeight],baseOrientation=[0.0,0.0,0.0,1])
                    self.stairs.append(step)
                    pybullet.changeDynamics(step, -1, lateralFriction=0.8)


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
        self.robot = mini_cheetah(pybullet)
        self.DynaRandom = DynamicsRandomizer(pybullet,self.robot)

        #Set Camera
        self._cam_dist = 1.0
        self._cam_yaw = 0.0
        self._cam_pitch = 0.0
        pybullet.resetDebugVisualizerCamera(self._cam_dist, self._cam_yaw, self._cam_pitch, [0, 0, 0])

        if self._on_rack:
            self.robot._set_on_rack()


    def _simulate(self):
        for _ in range(self._frame_skip):
            pybullet.stepSimulation()

    
    def _reset_world(self):

        # reset robot
        self.robot._reset_base()
        self.robot._reset_legs()

        # reset any disturbances in the terrain also (eg. obstacles)
        pass

    def _get_FPV_image(self):

        #FPV Camera Properties
        width = 128
        height = 128
        fov = 60
        aspect = width / height
        near = 0.02
        far = 20

        #View camera transformatios
        pos,ori = self.robot._get_base_pose()
        ori = -1*np.array(ori)
        camera_point, _ = pybullet.multiplyTransforms(pos, ori, [0.2+near,0,0], [0,0,0,1])
        target_point, _ = pybullet.multiplyTransforms(pos, ori, [0.2+far,0,0], [0,0,0,1])
        up_vector, _ = pybullet.multiplyTransforms(pos, ori, [0,0,1], [0,0,0,1])
        view_matrix = pybullet.computeViewMatrix(camera_point, target_point, up_vector)
        projection_matrix = pybullet.computeProjectionMatrixFOV(fov, aspect, near, far)

        # Get depth values using the OpenGL renderer
        images = pybullet.getCameraImage(width,
                                height,
                                view_matrix,
                                projection_matrix,
                                shadow=True,
                                renderer=pybullet.ER_BULLET_HARDWARE_OPENGL)
        #rgb and depth components
        rgb_opengl = np.reshape(images[2], (height, width, 4)) 
        depth_buffer_opengl = np.reshape(images[3], [width, height])
        depth_opengl = far * near / (far - (far - near) * depth_buffer_opengl)
        seg_opengl = np.reshape(images[4], [width, height]) * 1. / 255.

        # converting to openCV colour space
        rgb_image = cv2.cvtColor(rgb_opengl, cv2.COLOR_BGR2RGB)
        return rgb_image
	

if __name__ == "__main__":

    # To run this, remove src. the import of mini_cheetah and Dynamics Randomizer.
    t = Terrain(on_rack=False,terrain_type='plane')
    t._reset_world()

    while True:
        t._get_FPV_image()
        t._simulate()
        time.sleep(t.dt)


