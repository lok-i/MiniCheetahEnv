# MiniCheetahEnv
-  a pybullet-gym environment for Mini Cheetah


## ENV package structure

         ├── gym_MiniCheetahEnv
         │   └── envs
         │       ├── mini_cheetah_env.py  # main env file
         │       ├── rsc      # resource folder with URDF
         │       │   └── mini_cheetah
         │       │       ├── meshes
         │       │       │   ├── mini_abad.obj
         │       │       │   ├── mini_body.obj
         │       │       │   ├── mini_lower_link.obj
         │       │       │   └── mini_upper_link.obj
         │       │       ├── mini_cheetah_transp.urdf
         │       │       └── mini_cheetah.urdf
         │       └── src      # Source code folder
         │           ├── dynamics_randomization.py    # Dynamics Randomizer Class
         │           ├── mini_cheetah_class.py  # Mini Cheetah Robot model, parameters and functions
         │           └── world.py   # Main Simulation class with terraain paramters,setting and functions
         ├── media
         └── README.md





## FPV Camera (as Observation)

<p align="center">
   <img width="500" height="250" src="https://github.com/lok-i/MiniCheetahEnv/blob/main/gym-MiniCheetahEnv/media/FPVCam.gif">
</p>

## Verified Action space:

<p align="center">
   <img width="500" height="250" src="https://github.com/lok-i/MiniCheetahEnv/blob/main/gym-MiniCheetahEnv/media/TrajTrack.gif">

   <img width="500" height="250" src="https://github.com/lok-i/MiniCheetahEnv/blob/main/gym-MiniCheetahEnv/media/RandomAction.gif">

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

