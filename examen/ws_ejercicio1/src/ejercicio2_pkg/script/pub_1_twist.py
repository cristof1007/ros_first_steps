#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import random

rospy.init_node('pub_1_twist', anonymous=True)	
pub = rospy.Publisher('pub_1_twist', Twist, queue_size=10)
rate = rospy.Rate(1) # 1hz

while not rospy.is_shutdown():
    twistmessaje = Twist()
    twistmessaje.linear.x= round(random.uniform(10, 100), 2)
    twistmessaje.linear.y= round(random.uniform(10, 100), 2)
    twistmessaje.linear.z= round(random.uniform(10, 100), 2)
    twistmessaje.angular.x=round(random.uniform(10, 100), 2)
    twistmessaje.angular.y=round(random.uniform(10, 100), 2)
    twistmessaje.angular.z=round(random.uniform(10, 100), 2)
    pub.publish(twistmessaje)
    print(twistmessaje)
    rate.sleep()