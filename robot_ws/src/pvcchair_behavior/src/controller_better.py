#!/usr/bin/env python

import pygame
import time

import rospy
from std_msgs.msg import String

def controller():

	pub = rospy.Publisher('controller_input', Float64MultiArray, queue_size=3)
	data_to_send = Float64MultiArray()  # the data to be sent, initialise the array
	rospy.init_node('controller')
	rate = rospy.Rate(10) # 10hz (10x/s)

	pygame.init()
	pygame.joystick.init()

	done = False

	started = False

	#Runs when Controller is connected
	while not done:
		pygame.event.get()
		joystick_count = pygame.joystick.get_count()

	#no joystick found
	if joystick_count < 1:
		print('No Joystick')
		pygame.quit()

	#checking for joystick
	if not started:
		print('%s joystick(s) found:' % joystick_count)
		for i in range(joystick_count):
		    joystick = pygame.joystick.Joystick(i)
		    joystick.init()
		    name = joystick.get_name()
		    joystick_id = joystick.get_id()
		    print('Name: %s, ID: %s' % (name, joystick_id))
		started = True
		time.sleep(4)

	joystick = pygame.joystick.Joystick(0)
	joystick.init()
	print(joystick.get_name())
	x = joystick.get_axis(0)
	y = joystick.get_axis(1)
	z = joystick.get_axis(3)
	#print('%s, %s' % (x, y))

	while not rospy.is_shutdown():
		data_to_send.data = [x, y, z] # assign the array with the value you want to send
		#inputs = "%s, %s, %s" (x, y, z)
		rospy.loginfo(inputs)
		pub.publish(data_to_send)
		rate.sleep()

if __name__ == '__main__':
    try:
	controller()
    except rospy.ROSInterruptException:
	pass
