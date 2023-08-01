#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Point

rospy.init_node('sub_1_2_pub_point', anonymous=True)	

float_value= 0.0
float_value1= 0.0

def callback(data):	
    global float_value
    float_value=float(data.data)
    print("float_value",float_value)
def callback1(data):	
    global float_value1
    float_value1=data.data
    print("float_value1",float_value1)

sub = rospy.Subscriber("pub_1_int", Float64, callback)
sub1 = rospy.Subscriber("pub_2_float", Float64, callback1)


pub = rospy.Publisher('sub_1_2_pub_point', Point, queue_size=10)
rate = rospy.Rate(1) 
while not rospy.is_shutdown():
    float_value2 = float_value + float_value1
    pointmessaje = Point(float_value, float_value1, float_value2)
    pub.publish(pointmessaje)
    rate.sleep()
