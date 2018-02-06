#!/usr/bin/env python
import rospy
from std_msgs.msg import String

pub = rospy.Publisher('totalsum', String, queue_size=10)
saved_x = 0
saved_y = 0

def callback1(data):
	total = data.data + saved_y
	pub.publish(total)

def callback2(data):
	total = data.data + saved_2
	pub.publish(total)
        
def listener():
    rospy.init_node('calculator1', anonymous=True)
    rospy.Subscriber("x", Int32, callback1)
    rospy.Subscriber("y", Int32, callback2)
    rospy.spin()

if __name__ == '__main__':
    listener()
