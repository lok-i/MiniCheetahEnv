# MiniCheetahEnv
-  a pybullet-gym environment for Mini Cheetah


## To Do:

- [x] Check MPC implementation of pybullet, and the simulation bed configuration.
- [x] Import Mini Cheetah in the place of Laikago, do the requied system indentification and test the MPC controller.
- [x] Clean and develop the simulation bed into a gym env with approproate functions and classes.
- [x] Build a independent Domain Randomizer class, to work hand in hand with the env.
- [x] Integrate, test and verify env.
- [ ] Make it a gym package.
- [x] Add functions for capturing image as the observation.
- [ ] Implement utils and logger files for performace tracking and comparison .
- [ ] Add DR for the images aswell (if required).
- [ ] Add multi threading / make vectorized env for paralelized training.
- [ ] Add stable baselines support for training.
## MPC controller

### Installtion:
* Install the motion_imitation repository and all the requirements as per the instructions given [here](https://github.com/google-research/motion_imitation).
* Replace the existing "mpc_controller" folder with the folder in this repository.

### Run:
* To run the mini cheetah mpc controller(untuned) demo,

      cd mpc_controller
      python locomotion_controller_example.py



## References

### Papers:

1. From Pixels to Legs: Hierarchical Learning of Quadruped Locomotion. [Paper](https://arxiv.org/abs/2011.11722), [CoRL Presentation](https://youtu.be/o4PDEnqjT0I)
2. Vision-aided Dynamic Exploration of Unstructured Terrain(in Mini Cheetah). [Paper](https://ieeexplore.ieee.org/document/9196777), [Video](https://youtu.be/Tv7Vd-gF11s)

### Paper and Code:

1. [Previous Implementations - Github](https://github.com/topics/mini-cheetah)
2. [MPC Controller in Pybullet](https://github.com/google-research/motion_imitation/tree/master/mpc_controller)
3. [SlopedTerrainLinearPolicy(for DR)](https://github.com/StochLab/SlopedTerrainLinearPolicy)
4. [Sim-to-Real: Learning Agile Locomotion For Quadruped Robots(DR implementations of minatour)](https://github.com/bulletphysics/bullet3/tree/master/examples/pybullet/gym/pybullet_envs/minitaur/envs)
5. [Active Domain Randomization](https://paperswithcode.com/paper/active-domain-randomization)

