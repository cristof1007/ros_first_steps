#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
import random

rospy.init_node('pub_2_float', anonymous=True)
pub = rospy.Publisher('pub_2_float', Float64, queue_size=1)

rate = rospy.Rate(1) # 1hz --> 1/1hz=1s
while not rospy.is_shutdown():
    valor=round(random.uniform(10, 100), 2) #valor random con 2 decimales
    print(valor)
    pub.publish(valor) # se publica el valor
    rate.sleep() # delay de 1 segundo