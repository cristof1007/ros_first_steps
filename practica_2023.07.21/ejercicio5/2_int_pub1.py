#!/usr/bin/env python3
#--------------publicador de Int32--------------
import rospy
from std_msgs.msg import Int32
import random

rospy.init_node('2_int_pub1', anonymous=True)

pub = rospy.Publisher('random_int1', Int32, queue_size=1)

rate = rospy.Rate(1) 
while not rospy.is_shutdown():
    valor=random.randint(1,5)
    print(valor)
    pub.publish(valor) 
    rate.sleep() 