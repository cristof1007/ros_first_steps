#!/usr/bin/env python3
#--------------publicador de Int32--------------
import rospy
from std_msgs.msg import Int32
import random

rospy.init_node('int_pub1', anonymous=True)

pub = rospy.Publisher('random_int1', Int32, queue_size=1)

rate = rospy.Rate(1) # 10hz --> 1/10hz=0.1s
while not rospy.is_shutdown():
    valor=random.randint(1,100)
    print(valor)
    pub.publish(valor) # se publica el valor
    rate.sleep() # delay de 1 segundo