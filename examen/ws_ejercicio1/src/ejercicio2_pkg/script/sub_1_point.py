#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Point

rospy.init_node('sub_1_point', anonymous=True)	

float_value1 = 0.0
float_value2 = 0.0
float_value3 = 0.0

def callback(data):
    global float_value1,float_value2,float_value3	
    float_value1 = data.x;
    float_value2 = data.y;
    float_value3 = data.z;
    rospy.loginfo("x1: %f", float_value1)
    rospy.loginfo("y1: %f", float_value2)
    rospy.loginfo("z1: %f", float_value3)

sub = rospy.Subscriber("pub_1_twist_linear", Point, callback)

rate = rospy.Rate(1) # 1hz --> 1/1hz=1s
while not rospy.is_shutdown():
    rate.sleep() # delay de 1 segundo