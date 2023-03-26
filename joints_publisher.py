#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def publisher_node():
    # Initialize the node
    rospy.init_node('joints_publisher', anonymous=True)
    
    # Create a publisher for the "/arm_control" topic
    pub = rospy.Publisher('/arm_control', Int32, queue_size=10)
    
    # Set the desired state of the robotic arm
    arm_state = 1
    
    # Publish messages to the "/arm_control" topic
    msg = Int32()
    msg.data = arm_state
    pub.publish(msg)

if __name__ == '__main__':
    while True:
        publisher_node()
