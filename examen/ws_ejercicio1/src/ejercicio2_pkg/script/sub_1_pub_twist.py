#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point

rospy.init_node('sub_1_pub_twist', anonymous=True)	

joint1_value = 0.0
joint2_value = 0.0
joint3_value = 0.0
joint4_value = 0.0
joint5_value = 0.0
joint6_value = 0.0

def callback(data):
	global joint1_value,joint2_value,joint3_value,joint4_value,joint5_value,joint6_value
	joint1_value = data.linear.x
	joint2_value = data.linear.y
	joint3_value = data.linear.z
	joint4_value = data.angular.x
	joint5_value = data.angular.y
	joint6_value = data.angular.z

sub = rospy.Subscriber("pub_1_twist", Twist, callback) 

pub = rospy.Publisher('pub_1_twist_linear', Point, queue_size=1)
pub1 = rospy.Publisher('pub_1_twist_angular', Point, queue_size=1)
rate = rospy.Rate(10) # 10hz

while not rospy.is_shutdown():
	linearPoint = Point(joint1_value, joint2_value, joint3_value)
	angularPoint = Point(joint4_value, joint5_value, joint6_value)	

	pub.publish(linearPoint)
	pub1.publish(angularPoint)
	rate.sleep()