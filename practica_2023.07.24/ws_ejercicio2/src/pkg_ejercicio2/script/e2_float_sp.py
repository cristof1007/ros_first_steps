#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

rospy.init_node('e2_float_sp', anonymous=True)
float_value=0.0

def callback(data):
	global float_value	
	float_value=data.data
	rospy.loginfo("I heard %f", float_value)

pub = rospy.Publisher('floatpub', Float64, queue_size=10)
sub = rospy.Subscriber("random_float", Float64, callback)

rate = rospy.Rate(10) 
while not rospy.is_shutdown():
	valor=float_value*float_value
	pub.publish(valor)
	print(valor)
	rate.sleep()