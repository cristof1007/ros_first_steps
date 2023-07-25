#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('int_sub_result', anonymous=True)	

def callback(valor):
    int_value=valor.data
    print("El valor es:",int_value)

sub = rospy.Subscriber("int_sp_sum_pub", Int32, callback)

rate = rospy.Rate(1) # 1hz --> 1/1hz=1s

while not rospy.is_shutdown():
    rate.sleep() # delay de 1 segundo