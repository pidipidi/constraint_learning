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

env.isRender=True
s = env.reset()
cnt,rsum = 0,0

p = env.robot._p
x_vel = p.addUserDebugParameter('x_vel', -env.robot.jdict['x_slider'].jointMaxVelocity, env.robot.jdict['x_slider'].jointMaxVelocity, 0)
y_vel = p.addUserDebugParameter('y_vel', -env.robot.jdict['y_slider'].jointMaxVelocity, env.robot.jdict['y_slider'].jointMaxVelocity, 0)
th_vel = p.addUserDebugParameter('th_vel', -env.robot.jdict['z_axis_joint'].jointMaxVelocity, env.robot.jdict['z_axis_joint'].jointMaxVelocity, 0)
#from IPython import embed; embed(); sys.exit()

while 1:
    cnt += 1 # increase counter

    # manual
    ## a = [p.readUserDebugParameter(x_vel),\
    ##      p.readUserDebugParameter(y_vel),\
    ##      p.readUserDebugParameter(th_vel)]
    
    a = env.action_space.sample()
    obs, r, done, _ = env.step(action=a)
    ## print (obs, r, done)
    rsum += r
    still_open = env.render(mode='human')
    ## print ("[%d] r:[%.2f] done:[%d]"%(cnt,r,done))
    if done:
        env.reset()
    ##     break
    time.sleep(0.01)
p.disconnect()
env.close()
print ("Done. ravg:[%.3f]"%(rsum/cnt))

