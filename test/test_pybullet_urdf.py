import os
import pybullet as p
import pybullet_data
from time import sleep

## filename = "/home/dpark/git/development/husky/ur5_exp_test/src/worldmodel/world_model_data/data/worlds/lmco.urdf.xacro"
## eval("rosrun xacro xacro.py {} > model.urdf".format(filename))
dt = 1e-3

client = p.connect(p.GUI)
p.resetSimulation()
p.setPhysicsEngineParameter(enableFileCaching=0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -10)
p.setTimeStep(dt)

planeId = p.loadURDF("plane.urdf")
full_path = os.path.join(os.path.dirname(__file__), "hole.urdf")
hole_Id = p.loadURDF(full_path, basePosition=[0,0,0.0235], useFixedBase=1)
full_path = os.path.join(os.path.dirname(__file__), "peg.urdf")
peg_Id  = p.loadURDF(full_path, basePosition=[0,0,0.0235])


x_pos = p.addUserDebugParameter('x_pos', -0.5, 0.5, 0)
y_pos = p.addUserDebugParameter('y_pos', -0.5, 0.5, 0)
angle = p.addUserDebugParameter('angle', -3.14, 3.14, 0)

## jointFrictionForce = 1
## for joint in range(p.getNumJoints(peg_Id)):
#p.setJointMotorControl2(peg_Id, joint, p.POSITION_CONTROL, force=jointFrictionForce)
      
p.setRealTimeSimulation(1)
for i in range(10000):
    x = p.readUserDebugParameter(x_pos)
    y = p.readUserDebugParameter(y_pos)
    a = p.readUserDebugParameter(angle)
    
    p.setJointMotorControl2(peg_Id, 0, p.POSITION_CONTROL, targetPosition=x)#, force=jointFrictionForce)
    p.setJointMotorControl2(peg_Id, 1, p.POSITION_CONTROL, targetPosition=y)#, force=jointFrictionForce)
    p.setJointMotorControl2(peg_Id, 2, p.POSITION_CONTROL, targetPosition=a)#, force=jointFrictionForce)
    ## p.stepSimulation()
    sleep(1./240.)

## while True:
##     p.stepSimulation()
    
## number_of_joints = p.getNumJoints(client)
## for joint_number in range(number_of_joints):
##     info = p.getJointInfo(client, joint_number)
##     ## print(info)
##     print(info[0], ": ", info[1])
## sleep(30)


p.disconnect()
