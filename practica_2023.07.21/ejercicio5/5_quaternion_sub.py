#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Twist

rospy.init_node('5_quaternion_sub', anonymous=True)	

joint1_value = 0.0
joint2_value = 0.0
joint3_value = 0.0
joint4_value = 0.0
joint5_value = 0.0
joint6_value = 0.0

#######################

def callback(data):
	global joint1_value,joint2_value,joint3_value,joint4_value,joint5_value,joint6_value
	joint1_value = data.x
	joint2_value = data.y
	joint3_value = data.z
	joint4_value = data.w

	joint5_value = joint1_value + joint2_value + joint3_value + joint4_value
	joint6_value = joint5_value * joint5_value

	twist_integrator()
	
	
sub = rospy.Subscriber("4_point_pub", Quaternion, callback)   

#######################

pub = rospy.Publisher('5_quaternion_pub', Twist, queue_size=10)

def twist_integrator():
	global joint1_value,joint2_value,joint3_value,joint4_value,joint5_value,joint6_value

	twistmessaje = Twist()
    twistmessaje.linear.x =  joint1_value
    twistmessaje.linear.y =  joint2_value
    twistmessaje.linear.z =  joint3_value
    twistmessaje.angular.x = joint4_value
    twistmessaje.angular.y = joint5_value
    twistmessaje.angular.z = joint6_value
    pub.publish(twistmessaje)

#######################



rate = rospy.Rate(1) # 1hz
while not rospy.is_shutdown():
	rate.sleep()