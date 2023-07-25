#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Point

rospy.init_node('e4_point_sub', anonymous=True)	

float_value1 = 0.0
float_value2 = 0.0
float_value3 = 0.0
float_value4 = 0.0

#######################
def callback(data):
    global float_value1,float_value2,float_value3,float_value4	
    float_value1 = data.x
    float_value2 = data.y
    float_value3 = data.z

    float_value4 = float_value1 + float_value2 + float_value3

    quaternion_integrator()
    
    rospy.loginfo("x: %f", float_value1)
    rospy.loginfo("y: %f", float_value2)
    rospy.loginfo("z: %f", float_value3)
    rospy.loginfo("v4: %f", float_value4)

sub = rospy.Subscriber("3_int_sp_sum_pub", Point, callback)
#######################

pub = rospy.Publisher('4_point_pub', Quaternion, queue_size=10)

def quaternion_integrator():
    global float_value1,float_value2,float_value3,float_value4	
    pointmessaje = Quaternion(float_value1, float_value2, float_value3, float_value4)
    pub.publish(pointmessaje)


rate = rospy.Rate(1) # 1hz --> 1/1hz=1s
while not rospy.is_shutdown():
    rate.sleep() # delay de 1 segundo