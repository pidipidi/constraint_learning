## from spinup import ppo_tf1 as ppo
from spinup import ppo_pytorch as ppo
import torch
import gym
import pybulletgym

## env_name = 'LunarLander-v2'
env_name = 'CuboidPeginhole2DPyBulletEnv-v0'
#env_name = 'ReacherPyBulletEnv-v0'
env_fn   = lambda : gym.make(env_name)

ac_kwargs = dict(hidden_sizes=[64,64], activation=torch.nn.ReLU)

logger_kwargs = dict(output_dir=env_name, exp_name='test')

ppo(env_fn=env_fn, ac_kwargs=ac_kwargs, steps_per_epoch=5000, epochs=250, logger_kwargs=logger_kwargs)
#ppo(env_fn=env_fn, ac_kwargs=ac_kwargs, steps_per_epoch=500, epochs=25, logger_kwargs=logger_kwargs)
