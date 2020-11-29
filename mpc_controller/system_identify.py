import pybullet as p
import pybullet_data
import numpy as np
import time as t


p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

plane = p.loadURDF("%s/plane.urdf" % pybullet_data.getDataPath())
# laikago = p.loadURDF("laikago/laikago_toes_zup.urdf" )

miniChe = p.loadURDF('./mini_cheetah/mini_cheetah_transp.urdf',[0,0,0.34])


#for i in range(p.getNumJoints(laikago)):
# print("Laikago:",p.getDynamicsInfo(laikago,-1)[2])
print("MiniChe:",p.getDynamicsInfo(miniChe,-1)[2])



# for i in range(p.getNumJoints(miniChe)):
#     print("link",i,p.getLinkState(miniChe,i))
#     #print("Joint_",i,p.getJointInfo(miniChe,i))
p.setGravity(0,0,-9.8)




# p.createConstraint(miniChe, -1, -1, -1, p.JOINT_FIXED,
# 				[0, 0, 0], [0, 0, 0], [0, 0,1],parentFrameOrientation=p.getQuaternionFromEuler([0,0,0]))




def ruler(Link_A, Link_B):
    point_A = p.getLinkState(miniChe,Link_A)[0]
    point_B = p.getLinkState(miniChe,Link_B)[0]
    #point_B = [point_B[0],point_B[1],point_B[2] - 0.265]
    p.addUserDebugLine(point_A,point_B,[0,0,1],lineWidth=1000,lifeTime = 0.5)
    distance_vect = np.array(point_A) - np.array(point_B)
    print("distance",np.linalg.norm(distance_vect))


while(True):
    t.sleep(0.01)
    ruler(1,9)
    print("com_pos:",p.getBasePositionAndOrientation(miniChe)[0])
    p.setJointMotorControlArray(
        bodyIndex=miniChe,
        jointIndices=[0,1,2,
                      4,5,6,
                      8,9,10,
                      12,13,14],#np.random.randint(4,11),
        controlMode=p.POSITION_CONTROL,
        targetPositions =[0.0, -0.67, 1.25,
                          0.0, -0.67, 1.25,
                          0.0, -0.67, 1.25,
                          0.0, -0.67, 1.25,],#np.random.uniform(low=-np.pi,high=np.pi),
        targetVelocities=[0,0,0,0,0,0,0,0,0,0,0,0])

    p.stepSimulation()