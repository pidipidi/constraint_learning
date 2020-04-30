import time,gym
gym.logger.set_level(40)
import numpy as np
import gym  # open ai gym
import pybulletgym  # register PyBullet enviroments with open ai gym
#import pybullet as p


#p.connect(p.DIRECT)
#env = gym.make("ReacherPyBulletEnv-v0")
env = gym.make("CuboidPeginhole2DPyBulletEnv-v0")
#env = gym.make("InvertedPendulumPyBulletEnv-v0")
_ = env.render(mode='human')
print ("action is from %s to %s"%
       (env.action_space.low,env.action_space.high))

s = env.reset()
cnt,rsum = 0,0
while 1:
    cnt += 1 # increase counter
    a = env.action_space.sample()
    obs, r, done, _ = env.step(action=a)
    ## print (obs, r, done)
    rsum += r
    still_open = env.render(mode='human')
    ## print ("[%d] r:[%.2f] done:[%d]"%(cnt,r,done))
    if done:
        env.reset()
    ##     break
    time.sleep(0.04)
p.disconnect()
env.close()
print ("Done. ravg:[%.3f]"%(rsum/cnt))

