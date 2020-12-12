#!/usr/bin/env python

# make sure to use chmod +x swerve_logic.py to make to program runable by ros
# then should use rosrun swerve_logic.py to access python code

import math
#pi is math.pi
import rospy

class wheel:
    #strting speeds of wheels
    speed_fr = 0
    speed_fl = 0
    speed_rl = 0
    speed_rr = 0 

    #starting angles of wheels
    angle_fr = 0
    angle_fl = 0
    angle_rl = 0
    angle_rr = 0

class swerve_logic(object):
    
    #final speeds of the wheels to be stored in these variables
    fin_speed_fr = 0
    fin_speed_fl = 0
    fin_speed_rl = 0
    fin_speed_rr = 0

    #max speed of one of the wheels to normalize vector
    max_speed = 0

    #final angles of the wheels to be stored in these variables
    fin_ang_fr = 0
    fin_ang_fl = 0
    fin_ang_rl = 0
    fin_ang_rr = 0

    #set up the equations the wheels will depend on
    A = 0
    B = 0
    C = 0
    D = 0
    R = 0
    
    #call the wheel object class
    whl = wheel()

    def callback(data):
        #rospy.loginfo(rospy.get_caller_id() + "Gathering Data %s", data.data)
	print data.data

    def rad_to_deg(self, radians):
        #converts radian to degrees for easier calculations later

        degrees = radians * 180 / math.pi
        return degrees

    def __init__(self, width, length):

      #initialize these conditions when initializing the program
      #width = wheelbase, length = wheel length

      self._R = math.sqrt(pow(width, 2) + pow(length, 2))
      self._width = width
      self._length = length

      sub = rospy.Subscriber("controller_inputs", Float64MultiArray(), callback)
      rospy.spin

      #fin_speed_fr = 0, fin_speed_fl = 0, fin_speed_rl = 0, fin_speed_rr = 0, max_speed = 0
      #fin_ang_fr = 0, fin_ang_fl = 0, fin_ang_rl = 0, fin_ang_rr = 0

    def calcWheelVect(self, sub):
    #def calcWheelVect(self, x, y, ang_speed):
        #x and y of the wheel position vector and ang_speed	all should be given from controller input (Controller hould have a max and min we need to normalize to be between -1 and 1)
    	#math needed to calculate the vectors in the drive in Resources defined in PDF and swerveMath

	x = sub[0]
	y = sub[1]
	ang_speed = sub[2]

	pub = rospy.Publisher('wheels', String, queue_size=10, anonymous = True)
	rospy.init_node('calculations')
	rate = rospy.Rate(10) # 10hz

    	#calculate vectors needed to properly position wheels 

        self.A = x - ang_speed * (self._length / self._R)
        self.B = x + ang_speed * (self._length / self._R)
        self.C = y - ang_speed * (self._width / self._R)
        self.D = y + ang_speed * (self._width / self._R)

    	#calculates the wheel speeds needed based on the previously defined vectors
        self.fin_speed_fr = math.sqrt(pow(self.B, 2) + pow(self.C, 2))
        self.fin_speed_fl = math.sqrt(pow(self.B, 2) + pow(self.D, 2))
        self.fin_speed_rl = math.sqrt(pow(self.A, 2) + pow(self.D, 2))
        self.fin_speed_rr = math.sqrt(pow(self.A, 2) + pow(self.C, 2))
        self.max_speed = max(self.fin_speed_fr, self.fin_speed_fl, self.fin_speed_rl, self.fin_speed_rr)

    	#normalize speed based on fastest wheel to scale vector down if needed
        if self.max_speed > 1:
            self.fin_speed_fr /= self.max_speed
            self.fin_speed_fl /= self.max_speed
            self.fin_speed_rl /= self.max_speed
            self.fin_speed_rr /= self.max_speed
             
    	#find the angles to position the wheels at dependent on the vectors calculated earlier if not over max speed
        self.fin_ang_fr = self.rad_to_deg(math.atan2(self.B, self.C))
        self.fin_ang_fl = self.rad_to_deg(math.atan2(self.B, self.D))
        self.fin_ang_rl = self.rad_to_deg(math.atan2(self.A, self.D))
        self.fin_ang_rr = self.rad_to_deg(math.atan2(self.A, self.C))

    	#set the wheel speed to the speed normalized and found previously
        self.whl.speed_fr = self.fin_speed_fr
        self.whl.speed_fl = self.fin_speed_fl
        self.whl.speed_rl = self.fin_speed_rl
        self.whl.speed_rr = self.fin_speed_rr

    	#make sure proper angle is found given from 90 deg clockwise to new wheel location
        self.whl.angle_fr = self.fin_ang_fr
        self.whl.angle_fl = self.fin_ang_fl
        self.whl.angle_rl = self.fin_ang_rl
        self.whl.angle_rr = self.fin_ang_rr

	while not rospy.is_shutdown():
		wheel_outputs = "%s %s %s %s %s %s %s %s" % (self.whl.speed_fr, self.whl.speed_fl, self.whl.speed_rl, self.whl.speed_rr, self.whl.angle_fr, self.whl.angle_fl, self.whl.angle_rl, self.whl.angle_rr)

		rospy.loginfo(wheel_outputs)
		pub.publish(wheel_outputs)
		rate.sleep()

def main():
    test = swerve_logic(1, 1)
    test.calcWheelVect(1,-1,1)
    print(test._R)
    print('\n')

    print(test.whl.speed_fr)
    print(test.whl.speed_fl)
    print(test.whl.speed_rl)
    print(test.whl.speed_rr)

    print('\n')

    print(test.whl.angle_fr)
    print(test.whl.angle_fl)
    print(test.whl.angle_rl)
    print(test.whl.angle_rr)

#if __name__ == "__main__":
    #main()

if __name__ == '__main__':
    try:
        test = swerve_logic(2, 2) #2 inputs initialize the width and length of the robot in ft
	test.calcWheelVect(sub) #want the 3 inputs to come from controller node so subscribe to its topic
    except rospy.ROSInterruptException:
        pass
