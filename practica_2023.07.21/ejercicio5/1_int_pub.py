#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import random

rospy.init_node('1_int_pub', anonymous=True)

pub = rospy.Publisher('random_int', Int32, queue_size=1)

rate = rospy.Rate(1) 
while not rospy.is_shutdown():
    valor=random.randint(1,10)
    print(valor)
    pub.publish(valor) 
    rate.sleep() 