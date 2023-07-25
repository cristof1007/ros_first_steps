#!/usr/bin/env python3
# --------------suscriptor de Int32----------------
import rospy
from std_msgs.msg import Int32

# el codigo se identifica ante ros
rospy.init_node('int_sp_sum', anonymous=True)	

class sub:
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.sub = rospy.Subscriber("random_int", Int32, self.callback)
        self.sub1 = rospy.Subscriber("random_int1", Int32, self.callback1)

        self.pub = rospy.Publisher('int_sp_sum_pub', Int32, queue_size=1)

        self.rate = rospy.Rate(1) # 1hz --> 1/1hz=1s


    def callback(self, valor):
        self.valor1=valor.data

    def callback1(self, valor1):
        self.valor2=valor1.data

    def run(self):
        while not rospy.is_shutdown():
            suma = self.valor1 + self.valor2
            self.pub.publish(suma)
            print("valor1:",self.valor1, "aux:", self.valor2, "suma:", suma)
            self.rate.sleep() # delay de 1 segundo

obj = sub()
obj.run()