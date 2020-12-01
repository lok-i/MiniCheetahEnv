from setuptools import setup

setup(name='gym_MiniCheetahEnv',
      version='0.0.1',
      python_requires= '~=3.6',
      install_requires=['gym~=0.17.2','pybullet>=3.6']  # And any other dependencies foo needs
)