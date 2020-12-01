# MiniCheetahEnv
-  a pybullet-gym environment for Mini Cheetah


## ENV package structure


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




## FPV Camera (as Observation)

<p align="center">
   <img width="500" height="250" src="https://github.com/lok-i/MiniCheetahEnv/blob/main/gym-MiniCheetahEnv/media/FPVCam.gif">
</p>

## Verified Action space:

<p align="center">
   <img width="300" height="250" src="https://github.com/lok-i/MiniCheetahEnv/blob/main/gym-MiniCheetahEnv/media/TrajTrack.gif">

   <img width="300" height="250" src="https://github.com/lok-i/MiniCheetahEnv/blob/main/gym-MiniCheetahEnv/media/RandomAction.gif">

</p>



## Additional Terrains:

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

