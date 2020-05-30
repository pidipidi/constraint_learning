import time,gym
gym.logger.set_level(40)
import numpy as np
import gym  # open ai gym
import pybulletgym  # register PyBullet enviroments with open ai gym
#import pybullet as p
from test_spinningup_cnn import *

#p.connect(p.DIRECT)
#env = gym.make("ReacherPyBulletEnv-v0")
#env = gym.make("InvertedPendulumPyBulletEnv-v0")
#env = gym.make("CuboidPegInHole2DPyBulletEnv-v0")
#env = gym.make("CuboidPegInShallowHole2DPyBulletEnv-v0")
## env = gym.make("GripperPegInHole2DPyBulletEnv-v0")
## env = ProcessFrame(env)
## env = ImageToPyTorch(env)

env = gym.make("GripperPegInHole2DPyBulletEnv-v1")
#env = gym.make("GripperPegInHole2DPyBulletEnv-v2")
#env = gym.make("GripperPegInHole2DPyBulletEnv-v3")
#env = gym.make("GripperPegInHole2DPyBulletEnv-v6")
_ = env.render(mode='human')
#_ = env.render(mode='rgb_array')
#from IPython import embed; embed(); sys.exit()

env.isRender=True
s = env.reset()
cnt,rsum = 0,0
#env.action_space = env.robot.action_space
#env.observation_space = env.robot.observation_space
#from IPython import embed; embed(); sys.exit()

## p = env.robot._p
## x_vel = p.addUserDebugParameter('x_vel', -env.robot.jdict['x_slider'].jointMaxVelocity, env.robot.jdict['x_slider'].jointMaxVelocity, 0)
## y_vel = p.addUserDebugParameter('y_vel', -env.robot.jdict['y_slider'].jointMaxVelocity, env.robot.jdict['y_slider'].jointMaxVelocity, 0)
## th_vel = p.addUserDebugParameter('th_vel', -env.robot.jdict['z_axis_joint'].jointMaxVelocity, env.robot.jdict['z_axis_joint'].jointMaxVelocity, 0)
## finger_pos = p.addUserDebugParameter('gripper_pos', 0.005, 0.04, 0.04)
## #from IPython import embed; embed(); sys.exit()

while 1:
    cnt += 1 # increase counter

    # manual
    ## a = [p.readUserDebugParameter(x_vel),\
    ##      p.readUserDebugParameter(y_vel),\
    ##      p.readUserDebugParameter(th_vel),\
    ##      p.readUserDebugParameter(finger_pos) ]
    
    a = env.action_space.sample()
    #a[-1] = 0.0
    ## a = [0,0,0,0]
    ## a[2] = -0.05
    obs, r, done, _ = env.step(action=a)
    ## print (a, obs[0],obs[2],obs[4],obs[6])
    
    rsum += r
    ## still_open = env.render(mode='human')
    still_open = env.render(mode='rgb_array')
    ## print ("[%d] r:[%.2f] done:[%d]"%(cnt,r,done))
    if done:
        env.reset()
    ##     break
    time.sleep(1./240.)
    #time.sleep(1./100.)
p.disconnect()
env.close()
print ("Done. ravg:[%.3f]"%(rsum/cnt))

