#!/usr/bin/env python3
# --------------publicador-suscriptor de Int32--------------
import rospy
from geometry_msgs.msg import Point
from std_msgs.msg import Int32

rospy.init_node('3_int_sp_sum', anonymous=True)	
int_value=0
int_value1=0

#######################
 
def callback(data):
	global int_value	
	int_value=data.data
	rospy.loginfo("int_value", int_value)	

def callback1(data):
	global int_value1
	int_value1=data.data
	rospy.loginfo("int_value1", int_value1)	

sub = rospy.Subscriber("random_int", Int32, callback) 
sub1 = rospy.Subscriber("random_int1", Int32, callback1) 

#######################

pub = rospy.Publisher('3_int_sp_sum_pub', Point, queue_size=1)

def point_integrator():
	global int_value,int_value1
	sum = int_value + int_value1
	pointmessaje = Point(float(int_value), float(int_value1), float(sum))
	pub.publish(pointmessaje)


#######################

rate = rospy.Rate(1) 
while not rospy.is_shutdown():
	point_integrator()
	rate.sleep() 