# MiniCheetahEnv
-  a pybullet-gym environment for Mini Cheetah


## ENV package structure

The overall strucutre of the env package is listed below. The primary functions and classes governing the robot model and simulation are completed. Since the MDP is not yet formulated the main env file is yet to be completed, however the structure is done.

         ├── gym_MiniCheetahEnv
         │   ├── envs
         │   │   ├── __init__.py
         │   │   ├── mini_cheetah_env.py     # the main env file
         │   │   ├── rsc      # resource folder with URDF
         │   │   │   └── mini_cheetah
         │   │   │       ├── meshes
         │   │   │       │   ├── mini_abad.obj
         │   │   │       │   ├── mini_body.obj
         │   │   │       │   ├── mini_lower_link.obj
         │   │   │       │   └── mini_upper_link.obj
         │   │   │       ├── mini_cheetah_transp.urdf
         │   │   │       └── mini_cheetah.urdf # the URDF that is in use
         │   │   └── src
         │   │       ├── dynamics_randomization.py    # the dynamics Randomizer Class
         │   │       ├── mini_cheetah_class.py  # the mini cheetah robot model, parameters and functions
         │   │       ├── scrap.py   
         │   │       └── world.py   # the main simulation class with terraain paramters,pybullet setting and functions
         │   └── __init__.py
         ├── media
         ├── README.md
         └── setup.py

## For running a random action in the environment
Navigate to the mini_cheetah_env.py and run it as there is a example main() written for verification.

         cd MiniCheetahEnv/gym-MiniCheetahEnv/gym_MiniCheetahEnv/envs/
 
         python3 mini_cheetah_env.py


## Observation Space

The functions for capturing RGB-D images from a First Person Perspective of the robot has also been implemented. The images are displayed towards the left of the following gif.**Apart from this functions for capturing the imu data, robot and joint states is also available** [check in mini_cheetah_class.py](https://github.com/lok-i/MiniCheetahEnv/blob/main/gym-MiniCheetahEnv/gym_MiniCheetahEnv/envs/src/mini_cheetah_class.py)

<p align="center">
   <img width="500" height="250" src="https://github.com/lok-i/MiniCheetahEnv/blob/main/gym-MiniCheetahEnv/media/FPVCam.gif">
</p>

## Action space:

Currently the action space is the unormalized, raw joint torques. However, it would be changed to the commands of a low level controller in future as per the MDP formulation.[check in mini_cheetah_env.py](https://github.com/lok-i/MiniCheetahEnv/blob/main/gym-MiniCheetahEnv/gym_MiniCheetahEnv/envs/mini_cheetah_env.py)

<p align="center">
   <img width="300" height="250" src="https://github.com/lok-i/MiniCheetahEnv/blob/main/gym-MiniCheetahEnv/media/TrajTrack.gif">
   <img width="300" height="250" src="https://github.com/lok-i/MiniCheetahEnv/blob/main/gym-MiniCheetahEnv/media/RandomAction.gif">
   <br><i>Tracking a hand coded trajectory(Left), Random actions sampled from the action space(Right)</i><br>
</p>

## Dynamics Randomization:
An exclusive class has been implemented for dynamics radmomization. It uniformly sample friction and mass values (as of now) and adds it to the robot. In future we could also add other parameters like latency, decreasing of motor strength, inconsistent link dimensions, etc. We can also further randomize the domain parameters (i.e. terrrain and image feed) for robustness.[check in dynamics_randomization.py](https://github.com/lok-i/MiniCheetahEnv/blob/main/gym-MiniCheetahEnv/gym_MiniCheetahEnv/envs/src/dynamics_randomization.py)

## Additional Terrains:

Since we are targeting locomotion on discontinuous terrains, I have added other types of terrains which could be easily selected while initializing the env.[check in world.py](https://github.com/lok-i/MiniCheetahEnv/blob/main/gym-MiniCheetahEnv/gym_MiniCheetahEnv/envs/src/world.py)

### Stair Case:

<p align="center">
   <img width="300" height="220" src="https://github.com/lok-i/MiniCheetahEnv/blob/main/gym-MiniCheetahEnv/media/Stairs.png">
   <img width="300" height="220" src="https://github.com/lok-i/MiniCheetahEnv/blob/main/gym-MiniCheetahEnv/media/Stairs2.png">
</p>

### Rugged Terrain:

<p align="center">
   <img width="300" height="220" src="https://github.com/lok-i/MiniCheetahEnv/blob/main/gym-MiniCheetahEnv/media/RoughTerrain.png">
   <img width="300" height="220" src="https://github.com/lok-i/MiniCheetahEnv/blob/main/gym-MiniCheetahEnv/media/RoughTerrain2.png">
</p>

