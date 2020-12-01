#in mini_cheetah.py

    def track_foot_traj(self,line_thickness = 5,life_time =2):
        links_to_track =  [-1]+self._feet_id_list
        i=0
        for  link_id in links_to_track:
            if(link_id!=-1):
                current_point = self.pybullet_client.getLinkState(self.model,link_id)[0]
                self.pybullet_client.addUserDebugLine(current_point,self.prev_points[i],[1,0,0],line_thickness,lifeTime=life_time)
            else:
                current_point = self._get_base_pose()[0]
                self.pybullet_client.addUserDebugLine(current_point,self.prev_points[i],[0,0,1],line_thickness,lifeTime=life_time)
            self.prev_points[i] = current_point
            i+=1

    def trajectory_gen(self,theta):
        a = 0.1
        x = a*math.cos(theta)
        z = 0.18 + a*math.sin(theta)
        x_ninety = a*math.cos(theta+np.pi/2)
        z_ninety = 0.18 + a*math.sin(theta+np.pi/2)        
        ee_points = [[x,0,z],
                     [x_ninety,0,z_ninety], 
                     [x_ninety,0,z_ninety],
                     [x,0,z],
                    ]
        HIP_POSITIONS = [[0.18995, -0.1105, 0],
                                  [0.18995, 0.1105, 0],
                                  [-0.18995, -0.1105, 0],
                                  [-0.18995, 0.1105, 0]]
        ee_posns =[] 
        for i in range(4):
            ee_pos = [a+b for (a,b) in zip(ee_points[i],HIP_POSITIONS[i])]
            ee_posns.append(ee_pos)

        target_angles = np.array(pybullet.calculateInverseKinematics2(self.model,self._feet_id_list,targetPositions=ee_posns))        
        current_angles,current_vels = self._get_motor_states()
        current_angles = np.array(current_angles)
        current_vels = np.array(current_vels)
        target_vels = np.zeros(12)
        '''
        kp = np.full(12,100)
        kd = np.full(12,1)
        torques = np.multiply(kp,np.subtract(target_angles,current_angles))+ np.multiply(kd,np.subtract(target_vels,current_vels))
        print(torques)
        return torques
        '''
        self.pybullet_client.setJointMotorControlArray(
			bodyIndex=self.model,
			jointIndices=self._motor_id_list,
			controlMode=self.pybullet_client.POSITION_CONTROL,
            targetPositions = target_angles,
			targetVelocities=target_vels) 


# in World.py
if __name__ == "__main__":
    #To run this locally, remove "src."" from the import of mini_cheetah and Dynamics Randomizer.
    t = Terrain(on_rack=True,terrain_type='plane')
    t._reset_world()

    while True:
        thetas = np.arange(start=0,stop=-2*np.pi,step=-np.pi/5)
        for theta in thetas:
            t._get_FPV_image()
            t._simulate(torques=t.robot.trajectory_gen(theta))
            time.sleep(t.dt)

