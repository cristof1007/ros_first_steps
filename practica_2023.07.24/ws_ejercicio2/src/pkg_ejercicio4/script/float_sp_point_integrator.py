#!/usr/bin/env python3
# --------------suscriptor de Float64----------------
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Point

# el codigo se identifica ante ros
rospy.init_node('float_sp_point_integrator', anonymous=True)	

float_value=0
float_value1=0
float_value2=0

#se crea la funcion para recibir el mensaje del topico
def callback(data):	
    global float_value
    float_value=data.data
    print("float_value",float_value)
def callback1(data):	
    global float_value1
    float_value1=data.data
    print("float_value1",float_value1)
def callback2(data):	
    global float_value2
    float_value2=data.data
    print("float_value2",float_value2)

sub = rospy.Subscriber("random_float", Float64, callback)
sub1 = rospy.Subscriber("random_float1", Float64, callback1)
sub2 = rospy.Subscriber("random_float2", Float64, callback2)


pub = rospy.Publisher('float_sp_point_integrator_pub', Point, queue_size=10)
rate = rospy.Rate(1) 
while not rospy.is_shutdown():
    pointmessaje = Point(float_value, float_value1, float_value2)
    pub.publish(pointmessaje)
    rate.sleep()
